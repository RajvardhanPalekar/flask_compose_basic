db.createUser(
    {
        user: "admin",
        pwd: "adminpass",
        roles: [ "readWrite", "admin" ]
    },
    {
      user: "appuser",
      pwd: "dbpass",
      roles: [ "readWrite", "quotes_db" ]
    }
 )