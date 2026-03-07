## Install

brew tap mongodb/brew
brew install mongodb-community@8.0

## Start

mongod --config /opt/homebrew/etc/mongod.conf --fork

## Shutdown

mongosh
use admin
db.shutdownServer()

MongoDB Documentation link: https://www.mongodb.com/docs/v8.0/tutorial/install-mongodb-on-os-x/

## Usuario

crear database:
`use databaseName`

crear usuario:

```
db.createUser({
  user: 'sasa',
  pwd: 'caty',
  customData: { startDate: new Date() },
  roles: [
    { role: 'clusterAdmin', db: 'admin' },
    { role: 'readAnyDatabase', db: 'admin' },
    'readWrite'
  ]
})

db.getUsers()
db.dropUser('jon')
```

ver users:
`db.getUsers()`

Eliminar user:
`db.dropUser("jon")`

## Colecciones (Tablas)

crear colecciones
`db.createCollection("books")`

ver colecciones
`show collections`

## Agregar documentos

```js
db.books.insertOne({
  name: "OOP Programming",
  publishedDate: new Date(),
  authors: [{ name: "Jon Snow" }, { name: "Ned Stark" }],
});
```

## Insertar muchos documentos

```js
db.books.insertMany([
  {
    name: "Confident Ruby",
    publishedDate: new Date(),
    authors: [{ name: "Avdi Grimm" }],
  },
  {
    name: "The War of Art",
    publishedDate: new Date(),
    authors: [{ name: "Steven Pressfield" }],
  },
  {
    name: "Blink",
    publishedDate: new Date(),
    authors: [{ name: "Malcolm Gladwell" }],
  },
]);
```

## Solicitar (Query) todos los documentos con find()

`db.books.find()` Ahora devuelve .pretty por defecto

`db.books.find().pretty()`

## Query un documento especifico

El comando .find() retorna uno o varios documentos con la misma query.
El comando .findOne() retorna sólo el primer documento, si buscamos en un array que esta anidado envolvemos la llave en el `string`

`db.books.find( {name: "OOP Programming"} )`

`db.books.findOne( {"authors.name": "Kobu"} )`

## Proyecciones en MongoDB

### Elementos por incluir o no en una query

Son queries con .find() donde enviamos el segundo objecto con campos que nos devuelve, osea, en un documento con muchas entradas podemos retornar sólo las solicitadas. Si no queremos una entrada simplemente no s emenciona menos la de iD, que si no la queremos ponemos `_id = 0`

```js
db.books.find(
  {
    name: "Confident Ruby",
  },
  {
    _id: 0,
    name: 1,
    "authors.name": 1,
  },
);
```

SQL equivalente: `SELECT name, authors FROM books WHERE name = 'Confident Ruby'`

### query con un array anidado usando $slice

Slice ocuoa la posicion en un array, 1 o 2 o -1 son indices de array regular como JS

```js
db.books.find(
  {
    name: "Blink",
  },
  {
    publishedDate: 1,
    name: 1,
    authors: { $slice: -1 },
  },
);
```

### Eliminando documentos (.remove)

```js
db.books.remove({ name: "Ghost Writer" }, 1);
```

DeprecationWarning: Collection.remove() is deprecated. Use deleteOne, deleteMany, findOneAndDelete, or bulkWrite.

Remove un solo docuemnto

```js
db.books.deleteOne({ name: "Ghost Writer" });
```

Remueve todos los documentos

```js
db.books.deleteMany({ name: "Ghost Writer" });
```

### Query parte de string usando expresiones regulares

```js
db.books.findOne({ name: /.*deep work.*/i });
```

## Chequear si un campo existe en un documento usando `$exists`

```js
db.books.find({ reviews: { $exists: true } });
```
