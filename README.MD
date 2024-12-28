## Testing APIs with Pytest

***conftest.py*** 
- This is a spicific file in the root of your project where you can put fixtures and other setup/teardown code that should be run for all tests in the project.
- If we have a folder within tests folder inside that folder we can have another conftest.py file.This is very usefull for scoping fixtures to specific test modules.

### Run the commands to run tests...
```python
pytest filePath --disable-warnings -v # To run specific file based test
pytest --disable-warnings -v # Gives Test results without warnings
pytest --disable-warnings -v -x # Stops Testing when faces an error.



```



