# PyCode

##About PyCode
PyCode is a naive application that runs python code on the web. It downloads the python code, installs any
modules specified, runs it in a virtual environment, and then returns a result.

##Running PyCode
- Install Flask
- Install virtualenv
- Run app.py

##Classes, decorators, higher order functions
I'm using two classes and a decorator. The classes are found in app.py and the decorator can be found in runcode.py

##2x requirements
I used a list comprehension as well as a dictionary comprehension.

##Module requirements
- Flask 2 points
- virtualenv 1 point

##TODO somepoint in the future:
These are features that I would implement if I had time in the future...
- [ ] Saving sessions
  - [ ] Mongo to save code
    - [option one](https://docs.mongodb.org/ecosystem/tutorial/write-a-tumblelog-application-with-flask-mongoengine/)
    - [option two] (https://flask-pymongo.readthedocs.org/en/latest/)
    - [option three] (http://flask.pocoo.org/docs/0.10/patterns/mongokit/)
  - [ ] Setup new route that catches url parameter and passes it to mongo to retrieve code
  - [ ] Refactor to create new py files based on mongo id (mongo id should be name of py file)
- [ ] Creating virtual environments
  - [ ] Create virtualenv for each program
  - [ ] Delete upon session finshing
- [ ] Installing/importing modules
  - [ ] Adding input to specify modules to install
  - [ ] Installing modules on server
- [ ] Using multiple files
- [ ] Quiz integration (detecting output and comparing)
