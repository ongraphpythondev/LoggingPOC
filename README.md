# LoggingPOC
Prerequisites:
You will need the following programmes properly installed on your computer.
Python 3.7+
django 2.2+
Virtual Environment
To install virtual environment on your system use:

pip install virtualenv

or

pip3 install virtualenv #if using linux(for python 3 and above)

Installation and Running :
git clone https://github.com/ongraphpythondev/LoggingPOC.git
cd LoggingPOC

virtualenv venv or virtualenv venv -p python3 #if using linux(for python 3 and above)

venv\Scripts\activate # for windows or source venv/bin/activate # for linux

install required packages for the project to run
pip install -r requirements.txt

python manage.py runserver

Test Url at local system
http://127.0.0.1:8000/test/
