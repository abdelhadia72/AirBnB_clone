  <h1 align="center">AirBnB clone - The console </h1>

![hbnb](https://camo.githubusercontent.com/a8cd2eef2325c425519095dc2501111e630a77eddb454938c527cb82ea9c3aeb/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67)

## About Project

The AirBnB Clone Console is the initial phase of a project simulating an Airbnb application. In this phase, we implement a system to manage the modules that our webpage will utilize by interacting with a JSON-format database. Utilizing object-oriented programming, Python data translation, and command interpretation, we provide a local database that can be modified through command inputs.

## Installation

Clone the repository and navigate to the project directory:

```python
git clone https://github.com/abdelhadia72/AirBnB_clone.git
```
## Run

Run the console using:


```python
./console.py
```
## Usage

### Available Commands

|Command|Explanation|
|---|---|
|create|Creates a new instance of `BaseModel`, saves it (to the JSON file), and prints the `id`. Example: `$ create BaseModel`|
|show|Prints the string representation of an instance based on the class name and `id`. Example: `$ show BaseModel 1234-1234-1234`|
|all|Prints all string representations of all instances based or not on the class name. Example: `$ all BaseModel`|
|update|Updates an instance based on the class name and `id` by adding or updating an attribute (saves the change into the JSON file). Example: `$ update BaseModel 1234-1234-1234 email "aibnb@bnb.com"`|

### Normal Command Input

|Command|Example|
|---|---|
|create|create [class name]|
|show|show [class name] [id]|
|all|create [class name] [id]|
|update|create [class name] [id] [arg_name] [arg_value]|

### Alternative Command Input

|Command|Example|
|---|---|
|[class name].all()|User.all()|
|[class name].count()|User.count()|
|[class name].show(id)|User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")|
|[class name].destroy(id)|User.destroy("38f22813-2753-4d42-b37c-57a17f1e4f88")|
|[class name].update(id, attribute name, value)|User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "first_name", "John")|
|[class name].update(id, dictionary)|User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})|

### Available Classes

Every model inherits attributes from BaseModel:

- Attributes
- BaseModel
- User
- State
- City
- Amenity
- Place
- Review

## How to Start

Run the following command:

```python
$ ./console.py
```

Then, create a user instance using:


```python
(hbnb) create User
```

The ID of the created model will be visible in the standard output. To display the attributes of the created model, use:


```python
(hbnb) show User [id]
```

For a list of usable commands, type:


```pyton
(hbnb) help
```

To exit, press Ctrl+D or type the command `quit`.