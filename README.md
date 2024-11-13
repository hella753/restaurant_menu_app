# restaurant_menu_app

## Description 
Django Rest Framework Project backend for restaurant menus. Uses ViewSets, routers and JWT authentication.

## Endpoints
* Categories listing: /api/category/
* Subcategories listing: /api/subcategory/
* Subcategory Detail: /api/subcategory/id/
* Restaurants listing: /api/restaurants/
* Menu listing: /api/menu/
* User Registration: /api-register-users/
* JWT Authentication token: /api/token/
* JWT Authentication refresh token: /api/token/refresh/

## Components
* Models for Category, Subcategory, Dish, Ingredient, Restaurant, Menu and User are located in restaurant/models/ and user/models.py
* ViewSets for Category, Subcategory, Restaurant and Menu in restaurant/views.py. UserViewSet is in the user/views.py
* utils folder for custom filter backend and filtersets.
* Serializers for restaurant and user are in the apps in serializers.py.


## Features
* Registration functionality.
* Registered user can add a new restaurant.
* User can create a menu and assign it to a restaurant.
* Menu contains dishes.
* Dishes contain ingredients.
* Unauthorized user can access menu listing as well as category, subcategory and restaurant listings.
* In Subcategory detail DishSerializer is used for dish listings and custom filter backend is applied to use different filterset for the dishes. Dishes can be filtered by name and subcategories can be filtered by either dish name or parent category.

## Dependencies
* **Python 3.X**
* **Django 5.1.1**
* **Pillow 11.0.0** - Python Imaging Library adds image processing capabilities to your Python interpreter.
* **Django-debug-toolbar** - Configurable set of panels that display various debug information about the current request/response.
* **django-versatileimagefield**
* **python-magic-bin**
* **Django Rest Framework**
* **Simple JWT**



## Usage
Clone the repository:
```bash
git clone https://github.com/hella753/restaurant_menu_app
cd restaurant_menu_app
```
To install the dependencies, use the following command in your terminal:
```bash
pip install -r requirements.txt
```
To run the development server, use the following command in your terminal:
```bash
python manage.py runserver
```
To access the application, open your browser and go to http://127.0.0.1:8000/
