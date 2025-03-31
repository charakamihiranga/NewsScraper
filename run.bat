@echo off

:: Optional: Activate your virtual environment if you have one
call venv\Scripts\activate.bat  :: Adjust the path if needed (for example, use your actual environment folder)

:: Run your Python project entry point (e.g., main.py)
python main.py  :: Replace 'main.py' with the entry point of your project

:: Optional: Deactivate the virtual environment
deactivate
