# YaMDB | REST API Service
#### developed by the team of Yandex Practicum Students (back-end, K38):
- Alexander B. (role - team-lead, developer)
- Ivan Zykov (role - developer)
- Victoria Kuzmina (role - developer, data-manager)

##### Yatube API Final is a Sprint 10 Final task,
##### in which following goals are reached & discovered:
- to prepare a web-application containing REST API, custom JWT-authorization
- to improve soft-skills: team work, project coordination
- to improve Git skills
- data management (CSV - export to a database)

##### Short summary of the project's key features:
- User registration with verification via confirmation code
- Custom user roles set: user, moderator, admin, superuser (covering admin rights)
- Custom JWT authorization
- Advanced models development, incl. Custom User model

[![DRF_LOGO](https://www.django-rest-framework.org/img/logo.png)](https://www.django-rest-framework.org/)

| Features | How it works |
| ------ | ------ |
| JWT token authorization | Custom (based on Simple JWT) |
| Viewsets and serializers | Standard DRF |
| Pagination | Standard DRF |
| Filters & Search | Standard DRF |
| Permissions | Custom (based on rest_framework.permissions) |
| User model | Custom (based on AbstractUser) |
| Data models amount | 5 (with ForeignKeys) |
| User registration verification | Custom (via confirmation code) |
| Confirmation code generation | Cryptographically strong |
| User roles | user, moderator, admin, superuser (covering admin rights) |
| Ability to implement extra API versions | Maintained |
| Actual API version | v1 |

### JWT details
##### Endpoints & JSON examples

| Enpoint | Type | Request Body | API Answer | Comment |
| ------ | ------ | ------ | ------ | ------ |
| ```api/v1/auth/signup/``` | POST | ```{"username": "user","email": "user@yamdb.fake"}``` | Request mirroring |  Confirmation code transfer via email |
| ``` api/v1/auth/token/ ``` | POST | ``` {"username": "5rr4", "confirmation_code": "9bTg8N95"} ``` | ``` {"token":"eyJ0eXAiO..."} ``` | - |
| ```api/v1/users/me/``` | GET | - | ``` {"username": "user", "email": "user@yamdb.fake", "first_name": "Mike", "last_name": "Smith", "bio": "Student", "role": "user"} ``` | User can't change its role

### VENV minimal requirements:
```
Django==2.2.16
pytest==6.2.4
pytest-pythonpath==0.7.3
pytest-django==4.4.0
djangorestframework==3.12.4
djangorestframework-simplejwt==4.7.0
Pillow==8.3.1
PyJWT==2.1.0
requests==2.26.0
```

### VENV full recommended requirements:
```
atomicwrites                  1.4.1    
attrs                         22.1.0   
certifi                       2022.6.15
charset-normalizer            2.0.12   
colorama                      0.4.5    
Django                        2.2.16   
django-filter                 21.1     
djangorestframework           3.12.4   
djangorestframework-simplejwt 4.7.0    
idna                          3.3      
importlib-metadata            4.2.0    
iniconfig                     1.1.1    
mccabe                        0.7.0    
packaging                     21.3     
pip                           22.2.2   
pluggy                        0.13.1   
py                            1.11.0   
pycodestyle                   2.9.1    
pyflakes                      2.5.0    
PyJWT                         2.1.0    
pyparsing                     3.0.9 
pytest                        6.2.4 
pytest-django                 4.4.0 
pytest-pythonpath             0.7.3 
pytz                          2022.1
requests                      2.26.0
setuptools                    39.0.1
singledispatch                3.7.0
six                           1.16.0
sqlparse                      0.4.2
toml                          0.10.2
typing_extensions             4.3.0
urllib3                       1.26.11
zipp                          3.8.1
```
### Import CSV
```
sqlite3.exe db.sqlite3
.mode csv
.import  <model_name>.csv <app _name>_< model_name>
```
[![Python_Powered_Logo](https://www.python.org/static/community_logos/python-powered-w-200x80.png)](https://www.python.org/)
> Markdown easy expirience is powered by `Dillinger`
