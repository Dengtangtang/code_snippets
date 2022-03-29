## Ubuntu commands

#### Add a new user
```
adduser [username]
```

#### Add a user to a group (e.g., sudo group)
```
usermod -aG [sudo] [username]
```
where "aG" option tells the system to **append** the user to the specified **group**.

#### Show a user's groups
```
groups [username]
```

#### Change password of a user
```
passwd [username]
```

#### Count the number of files in a directory
```
ls [directory] | wc -l
```
