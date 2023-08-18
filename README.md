# AirBnB Clone

---

A clone of the popular booking website AirBnB, made with Python. This 
project covers the basic, building block of a web application --
creating, updating and deleting objects. A digital illustration of how this 
project will develop is below:

![Web Development Map](web_dev_console1.png)
To launch the console, run `./console.py`. An interactive prompt will be 
displayed like this:
```
$ ./console.py
(hbnb)
```
Type `help` to see the list of available commands:
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) 
```
To see the documentation of each command, type `help <topic>`. For example:
```
(hbnb) help all
`all`Usage: all or all <class>
        Display string representations of all instances of a given class.
(hbnb) 
```

To create an object, type `create <class name>`. It will print out the id
of the new object. For example:
```
(hbnb) create User
4cae2ff5-1232-4d72-a047-e9cf73dbd523
(hbnb) 
```
To show the properties of a specific object, use `show <class name> <id>` 
or `<class name>.show(<id>)`. For instance:
```
(hbnb) show BaseModel f1c788df-5ee7-4f11-92fc-6256ca044db8
[BaseModel] (f1c788df-5ee7-4f11-92fc-6256ca044db8) {'id': 'f1c788df-5ee7-4f11-92fc-6256ca044db8', 'created_at': datetime.datetime(2023, 8, 10, 10, 54, 1, 443027), 'updated_at': datetime.datetime(2023, 8, 10, 10, 54, 1, 443041)}
(hbnb) 
```
To list all objects of a specific class, type `all <class name>` or `<class 
name>.all()`. For instance:
```
(hbnb) all
[BaseModel] (eb3d25bc-8d37-4a32-8485-f6e1d4c570a7) {'id': 'eb3d25bc-8d37-4a32-8485-f6e1d4c570a7', 'created_at': datetime.datetime(2023, 8, 10, 11, 0, 52, 422636), 'updated_at': datetime.datetime(2023, 8, 10, 11, 0, 52, 422660)}
[User] (54ee0e34-3c3c-4721-8602-6efc294571e0) {'id': '54ee0e34-3c3c-4721-8602-6efc294571e0', 'created_at': datetime.datetime(2023, 8, 10, 11, 0, 52, 422655), 'updated_at': datetime.datetime(2023, 8, 10, 11, 0, 52, 425458)}
[BaseModel] (adc73b35-16d7-4d57-a925-0971d98fe758) {'id': 'adc73b35-16d7-4d57-a925-0971d98fe758', 'created_at': datetime.datetime(2023, 8, 10, 11, 0, 52, 449806), 'updated_at': datetime.datetime(2023, 8, 10, 11, 0, 52, 449811)}
[User] (567cd891-e9e6-4fa1-bf25-4d4d853ae7ca) {'id': '567cd891-e9e6-4fa1-bf25-4d4d853ae7ca', 'created_at': datetime.datetime(2023, 8, 10, 11, 0, 52, 449833), 'updated_at': datetime.datetime(2023, 8, 10, 11, 0, 52, 449834)}
[User] (ccb72b9b-6daf-47ab-b7a8-270c4056c035) {'id': 'ccb72b9b-6daf-47ab-b7a8-270c4056c035', 'created_at': datetime.datetime(2023, 8, 10, 11, 0, 52, 453729), 'updated_at': datetime.datetime(2023, 8, 10, 11, 0, 52, 453760)}
[User] (2c85fef7-be79-49d0-8134-41451f28d201) {'id': '2c85fef7-be79-49d0-8134-41451f28d201', 'created_at': datetime.datetime(2023, 8, 10, 11, 0, 52, 457743), 'updated_at': datetime.datetime(2023, 8, 10, 11, 0, 52, 457748), 'email': 'AirBnB@gmail.com', 'first_name': 'AirBnB', 'password': 'AirBnB123'}
[User] (d12cb79b-454b-4364-893d-fdeaf59853d7) {'id': 'd12cb79b-454b-4364-893d-fdeaf59853d7', 'created_at': datetime.datetime(2023, 8, 10, 11, 0, 52, 458905), 'updated_at': datetime.datetime(2023, 8, 10, 11, 0, 52, 458920)}
(hbnb) 
```

To delete an object, type `destoy <class name> <id>` or `<class name>.
destroy(<id>)`. For instance:
```
(hbnb) destroy User 4cae2ff5-1232-4d72-a047-e9cf73dbd523
(hbnb) 
(hbnb) User.destroy("4cae2ff5-1232-4d72-a047-e9cf73dbd523")
(hbnb)
```
To update an object, you may use one of the following syntaxes: `update` 
<class name> <id> <attribute name> <attribute value>`, `<class name>.update
(<id>, <attribute name>, <attribute value>)` or `<class name>.update(<id>, 
<dict>)` where `<dict>` is a Python dictionary with attribute name and value 
pairs. For example:

```
(hbnb) show User d12cb79b-454b-4364-893d-fdeaf59
853d7
[User] (d12cb79b-454b-4364-893d-fdeaf59853d7) {'id': 'd12cb79b-454b-4364-893d-fdeaf59853d7', 'created_at': datetime.datetime(2023, 8, 10, 11, 0, 52, 458905), 'updated_at': datetime.datetime(2023, 8, 10, 11, 0, 52, 458920)}
(hbnb) update User d12cb79b-454b-4364-893d-fdeaf59853d7 first_name "AirBnB"
(hbnb) show User d12cb79b-454b-4364-893d-fdeaf59853d7
[User] (d12cb79b-454b-4364-893d-fdeaf59853d7) {'id': 'd12cb79b-454b-4364-893d-fdeaf59853d7', 'created_at': datetime.datetime(2023, 8, 10, 11, 0, 52, 458905), 'updated_at': datetime.datetime(2023, 8, 10, 11, 40, 59, 39554), 'first_name': 'AirBnB'}
(hbnb) 
```