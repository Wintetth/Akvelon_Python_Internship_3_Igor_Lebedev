# Personal finances

_MVC application for managing personal finances for money planning_

## Architecture
The application is stored in project root directory folder called `app/`. The `app/` contains 3 subdirectories: 
* `controllers/` - interprets user actions, notifying the model of the need for changes;
* `models/` - provides data and responds to controller commands, changing its state;
* `utilities/` - additional code.

The application is implemented with Flask Web framewor and data table created using PostgreSQL.
There is a `test.http` file, which contains test get and post requests.

The `utilities/` also have a Fibonacci sequence nth number getting function.


Here are some screenshots of json response, as a results of application working:
* _fibonacci_
![image](https://user-images.githubusercontent.com/65975247/121085873-1a743f00-c7eb-11eb-9bd8-1db92f793aa8.png)

* _view_all_transaction_
![image](https://user-images.githubusercontent.com/65975247/121085944-3677e080-c7eb-11eb-819c-7bc569a25c6b.png)

* _grooped_
![image](https://user-images.githubusercontent.com/65975247/121085963-3d9eee80-c7eb-11eb-9e55-414492f320c9.png)

* _trying to create user, which already exists_
![image](https://user-images.githubusercontent.com/65975247/121086076-61facb00-c7eb-11eb-935b-dd218fd83409.png)
