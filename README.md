# Author 
  ## awonali14@gmail.com

# Property 
  ## [Syed Awon Ali](https://github.com/awon14)   


## Installation

Open terminal select current directory and do following in same order:

* create virtual environment using command ```python3 -m venv env ```
* activate virtual environment by command ```source env/bin/activate```

### Use the package manager [pip](https://pip.pypa.io/en/stable/) and perform following.
* ```pip install --upgrade pip```
* ```pip install -r requirements.txt```
* ```python manage.py makemigrations (No need for this command) ``` 

## Database setup
Now, open up mysite/settings.py. It’s a normal Python module with module-level variables representing Django settings.
If you wish to use another database, install the appropriate database bindings and change the following keys in the DATABASES 'default' item to match your database connection settings:
* [ENGINE](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-DATABASE-ENGINE) – 'django.db.backends.postgresql',Other backends are also available.
* [NAME](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-NAME) – The name of your database. If you’re using SQLite, the database will be a file on your computer; in that case, NAME should be the full absolute path, including filename, of that file. The default value, BASE_DIR / 'db.sqlite3', will store the file in your project directory.
* USENAME
* PASSWORD

If all went well till now then run ```python manage.py migrate``` , and tour database is set to go live with application . Make sure to test it by ```python manage.py runserver```

## License
[MIT](https://choosealicense.com/licenses/mit/)
