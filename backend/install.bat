set "PYTHON=%~dp0venv\Scripts\python.exe"
FOR %%i IN ("pypi\%1*") DO Set FileName="%%i"
Echo %FileName%
%PYTHON% -m pip install %FileName%