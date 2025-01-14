# 20230807-11-sqlalchemy-alembic-migrations-relations-cli

## Review
- Questions
    - What is an ORM?
        - [ORM Visualization](https://www.figma.com/file/Udbuyi0ezpGhxNPL6qmWrK/ORM-Visual?type=whiteboard&node-id=0%3A1&t=n1rntyz68uDGdvge-1)
    - What is a Python module?
    - What is a Python package?
    - What is `PyPi`?
        - [The Python Package Index (PyPI) is a repository of software for the Python programming language.](https://pypi.org/#:~:text=The%20Python%20Package%20Index%20(PyPI)%20is%20a%20repository%20of%20software%20for%20the%20Python%20programming%20language)
    - What is `pipenv`
        - Pipenv docs: [What is pipenv?](https://pipenv.pypa.io/en/latest/#:~:text=Pipenv%20is%20a%20Python%20virtualenv%20management%20tool%20that%20supports%20a%20multitude%20of%20systems%20and%20nicely%20bridges%20the%20gaps%20between%20pip%2C%20python%20(using%20system%20python%2C%20pyenv%20or%20asdf)%20and%20virtualenv.)
    - What is a virtual environment?
        - [Virtual Environment Visualization](https://www.figma.com/file/ej3qo3FLhS78eipGApigmH/Virtual-Environments-Visualization?type=whiteboard&node-id=0%3A1&t=n1rntyz68uDGdvge-1)

## Where are we going?

- CLI todo list - [Demo CLI Repo](https://github.com/codetombomb/taskmaster-5000)

## SWBATs

- [ ]  Create a Virtual Env with `pipenv` and install dependencies
   1.  pipenv --python 3.8.13
- [ ]  Initialize migrations with `alembic`
    3. alembic init migrations
- [ ]  Configure `alembic` to work with our DB
    2. pipenv install alembic sqlachemy
- [ ]  Create a schema and migrate the DB

- [ ]  Use migrations to:
    - create/drop tables
    - rename tables
    - add/remove columns
    - rename columns
    - modify constraints