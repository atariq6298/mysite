python -m venv venv
call /venv/scripts/activate.bat
pip install -r /requirements.txt
set flask_app=flask_app.py
echo run
flask run
