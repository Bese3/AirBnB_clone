# AirBnB Clone

---

A clone of the popular booking website AirBnB, made with Python. This 
project covers the basic, building block of a web application --
creating, updating and deleting objects. A digital illustration of how this 
project will develop is below:

![Web Development Map](web_dev_console.png)
This first version of the console uses JSON to store objects.

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
Prints all string representation of all instances based on or not
        on the class name
        Usage: all <class_name>
               all
        Example: all BaseModel
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
(hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}
(hbnb)
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```

To list all objects of all types, type `all` in the prompt. For instance:
```
(hbnb) all
["[User] (58bc83c4-16bf-4a9f-af5c-c7aef712544b) {'id': '58bc83c4-16bf-4a9f-af5c-c7aef712544b', 'created_at': datetime.datetime(2022, 1, 30, 18, 7, 36, 314659), 'updated_at': datetime.datetime(2022, 1, 30, 18, 7, 36, 314672), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", 
"[User] (6cf1e2d4-bb7a-42d1-a483-3e743dd3ca96) {'id': '6cf1e2d4-bb7a-42d1-a483-3e743dd3ca96', 'created_at': datetime.datetime(2022, 1, 30, 18, 8, 23, 48249), 'updated_at': datetime.datetime(2022, 1, 30, 18, 8, 23, 48260), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", 
"[User] (d6c71a9b-1499-46ad-80b8-0f56ef630680) {'id': 'd6c71a9b-1499-46ad-80b8-0f56ef630680', 'created_at': datetime.datetime(2022, 1, 30, 18, 8, 23, 48433), 'updated_at': datetime.datetime(2022, 1, 30, 18, 8, 23, 48439), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}",
"[User] (c331d99f-26dd-4c16-abf0-8f3ef83be302) {'id': 'c331d99f-26dd-4c16-abf0-8f3ef83be302', 'created_at': datetime.datetime(2022, 1, 30, 20, 8, 21, 752223), 'updated_at': datetime.datetime(2022, 1, 30, 20, 8, 21, 752235), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}",
"[Amenity] (27a5cbec-2a5b-4528-888f-45ed7499d18d) {'id': '27a5cbec-2a5b-4528-888f-45ed7499d18d', 'created_at': datetime.datetime(2022, 1, 30, 21, 14, 38, 525535), 'updated_at': datetime.datetime(2022, 1, 30, 21, 14, 38, 525591)}"]
(hbnb) 
```
To list all objects of a specific class, type `all <class name>` or `<class 
name>.all()`. For 
instance:
```
(hbnb) all Amenity
["[Amenity] (27a5cbec-2a5b-4528-888f-45ed7499d18d) {'id': '27a5cbec-2a5b-4528-888f-45ed7499d18d', 'created_at': datetime.datetime(2022, 1, 30, 21, 14, 38, 525535), 'updated_at': datetime.datetime(2022, 1, 30, 21, 14, 38, 525591)}"]
(hbnb) Amenity.all()
["[Amenity] (27a5cbec-2a5b-4528-888f-45ed7499d18d) {'id': '27a5cbec-2a5b-4528-888f-45ed7499d18d', 'created_at': datetime.datetime(2022, 1, 30, 21, 14, 38, 525535), 'updated_at': datetime.datetime(2022, 1, 30, 21, 14, 38, 525591)}"]
```


To delete an object, type `destoy <class name> <id>` or `<class name>.
destroy(<id>)`. For instance:
```
(hbnb) destroy User 4cae2ff5-1232-4d72-a047-e9cf73dbd523
(hbnb) 
(hbnb) User.destroy("4cae2ff5-1232-4d72-a047-e9cf73dbd523")
(hbnb)
```

To update an object, you may use one of the following syntaxes: `update 
<class name> <id> <attribute name> <attribute value>`, `<class name>.update
(<id>, <attribute name>, <attribute value>)` or `<class name>.update(<id>, 
<dict>)` where `<dict>` is a Python dictionary with attribute name and value 
pairs. For example:

```
(hbnb) update Place 27427d92-574c-4ce3-876b-66a63f956edf "description" "Elegant"
(hbnb) Place.update("27427d92-574c-4ce3-876b-66a63f956edf", "max_guests", 3)
(hbnb) Place.update("27427d92-574c-4ce3-876b-66a63f956edf", {"number_rooms": 2, "number_bathrooms": 1})
(hbnb)
(hbnb) show Place 27427d92-574c-4ce3-876b-66a63f956edf
[Place] (27427d92-574c-4ce3-876b-66a63f956edf) {'id': '27427d92-574c-4ce3-876b-66a63f956edf', 'created_at': datetime.datetime(2022, 1, 31, 2, 39, 20, 963183), 'updated_at': datetime.datetime(2022, 1, 31, 2, 45, 6, 189666), '"description"': 'Elegant', 'max_guests': 3, 'number_rooms': 2, 'number_bathrooms': 1}
```