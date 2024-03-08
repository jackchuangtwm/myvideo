del /S /Q results\*
C:\Users\JackChuang\AppData\Local\Programs\Python\Python311\python -m virtualenv venv
.\venv\Scripts\pip.exe install -r requirements.txt --target=.\venv\Lib\site-packages --upgrade
.\venv\Scripts\python.exe -m pytest -n 2  --alluredir=./results --reruns 3 -p no:faulthandler -k "test" --tb=long
