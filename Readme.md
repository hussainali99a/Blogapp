##### Create Virtual Environment
```
python -m venv env
```

##### Activate Virtual Environment
```
.\env\Scripts\activate
```

##### Install Dependencies
```
pip install -r requirements.txt
```

##### Prepare DataBase
```
python manage.py makemigrations
python manage.py migrate
```

##### Run the project
```
python manage.py runserver
```

###### [Visit Project](http://127.0.0.1:8000/)