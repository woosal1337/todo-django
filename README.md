# 🐲 To-do app using Django
 
 ### To run the app
 ```
 python manage.py runserver
 ```
 
 
 ### To create a new app
 ```
 python manage.py startapp app_name
 ```
 
 ### App configurations
 ```
 1) urls.py in the app directory
 2) include the app name in the main generated app settings.py -> INSTALLED_APPS list
 3) include the app url path in the main general app urls.py -> urlpatterns list `path("tasks/", include("tasks.urls"))`
 4) Create `templates` named folder in the new generated app's path
 5) Add `index.html` / `styles.css` files in the given `templates` directory
 ```
 
## Templates

### urls.py Template
```
from django.urls import path  
  
from . import views  
  
urlpatterns = \[  
    path("", views.index, name\="index")  
\]
```

### views.py Template
```
from django.shortcuts import render, HttpResponse  
  
# Create your views here.  
def index(request):  
    return HttpResponse("Hello, World!")
```
