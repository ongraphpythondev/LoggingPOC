
# LoggingPOC
<br><h1>Prerequisites:</h1><br><br>
You will need the following programmes properly installed on your computer.
Python 3.7+
django 2.2+
Virtual Environment
To install virtual environment on your system use:

pip install virtualenv

or

pip3 install virtualenv #if using linux(for python 3 and above)

<br><h1>Installation and Running :</h1><br><br>
git clone https://github.com/ongraphpythondev/LoggingPOC.git
cd LoggingPOC

virtualenv venv or virtualenv venv -p python3 #if using linux(for python 3 and above)

venv\Scripts\activate # for windows or source venv/bin/activate # for linux

<br><h1>install required packages for the project to run</h1>
pip install -r requirements.txt

python manage.py runserver

<h1>Test Url at local system</h1>
http://127.0.0.1:8000/test/
