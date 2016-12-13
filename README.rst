Parsons Programming Puzzles
===========================
This is a web application for solving Parsons Programming Puzzles in Python.


Prerequisites for development
-----------------------------
The project uses Docker and Docker Compose.

Visit the `Docker Engine install-page <https://docs.docker.com/engine/installation/>`_
and follow the instructions for your OS (Linux and macOS is highly recommended).

Visit the `Docker Compose install-page <https://docs.docker.com/compose/install/>`_
and follow the instructions.


Enough already! I want to develop!
----------------------------------
Before you can start the application with Docker you have to create a `.env`
file in the project root directory. At the moment it can be empty.

To start the application with all dependencies with Docker you run
:code:`docker-compose up` in the root directory of the project.

The command :code:`docker-compose run web <command>` will be useful to run
commands inside the web container. The `manage.py` script could be run this way.

When the containers have started you should be able to view the application
with your web browser at `127.0.0.1:5000 <http://127.0.0.1:5000>`_.


Common gotchas
--------------
When making significant changes to the project, it's a good idea to rebuild the docker containers.
:code:`docker-compose up --build` let you build and restart in one command.
