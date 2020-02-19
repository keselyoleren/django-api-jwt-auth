# django-api-jwt-auth 

## instalation 

```
$ git clone https://github.com/keselyoleren/django-api-jwt-auth.git
```

```
$ cd django-api=jwt-auth 
```

``` 
$ pip install -r requirements.txt
```
```
$ python manage.py runserver
```

### example 
```
$ curl -X POST -d '{"username": "keselyoleren","password": "qweasd"}' -H 'Content-Type: application/json'  http://127.0.0.1:8000/api/login/
{"username":"keselyoleren","access_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTgyMTIwMTYzLCJqdGkiOiJjMTY4ZGM3MDM0ZjI0MmQ1YjU4NmU5YzU4ZDlkOTc2OSIsInVzZXJfaWQiOjF9.724oxAvx5fENJ6LULnkBXwvDOJOjiswhh-5X4YOSWrQ","refresh_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU4MjIwNjI2MywianRpIjoiYzA0MzRkZjA1YjhhNGFmODg2YzQ3NDQxMDE5YjQzZTUiLCJ1c2VyX2lkIjoxfQ.zA4iyqd9MdHjrJfyjIhXfzyrWwsB0VeURgluZJkTgRc"}
```
