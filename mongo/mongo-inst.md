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

## Course

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
