## Alembic setup
- Alembic provides for the creation, management, and invocation of change management scripts for a relational database table, using SQLAlchemy as the underlying engine.

- Explanation :
- Alembic is a migration tool for SQLAlchemy. It is used to create,manage,and invoke change management scripts for a relational database table.
- It is a part of the SQLAlchemy project and is used to manage database schema changes.


###  installation:

```python

 pip install alembic
 alembic init alembic # this command will create a folder named alembic in your project directory then you can create revisions and work with them.
 alembic revision -m "your descriptive message" # this command will create a new revision in the alembic folder
 alembic revision --autogenerate -m "your descriptive message" # this command will create a new revision in the alembic folder and will automatically generate the migration depend on your models
 alembic upgrade head # To run upgreade function of head revision
 alembic downgrade base # To run downgrade function of base revision
 
 fastapi dev app/main.py # To run on development
 gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 app.main:app # To run on production