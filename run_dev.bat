python -m venv venv
call ./venv/scripts/activate.bat
python install -r ./requirements.txt
set flask_app=flask_app.py
flask run