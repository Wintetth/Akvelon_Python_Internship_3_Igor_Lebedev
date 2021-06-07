# Personal finances

_MVC application for managing personal finances for money planning_

## Architecture
The application is stored in project root directory folder called `app/`. The `app/` contains 3 subdirectories: 
* `controllers/` - interprets user actions, notifying the model of the need for changes;
* `models/` - provides data and responds to controller commands, changing its state;
* `utilities/` - additional code.

The application is implemented with Flask Web framewor and data table created using PostgreSQL.
There is a `test.http` file, which contains test get and post requests.
