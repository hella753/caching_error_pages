# Django Caching & Error Pages

## Description 
Fruit and Vegetable shop website made with free template.
The Project uses Django and sqlite3 database. 
There are several records in the database for testing.


## **What's New This week** ##
### **New Features** ###
* Implemented low level caching for store:category_listings and template caching for navbar which is in templates/reusable_components <3.
* Added handlers for errors in settings and two views for it. One is a template view for 404 and one is manually raising an exception to test the server error. You can access the page on "test500/"
* Added Email configuration settings, forms.py in store and made the contact FormView. Now you can Send an email with the help of smtp.
* :D:D Email is before passwords now in registration </3


## URLS
  * Home - is accessible on route `/`
  * Shop - is accessible on route `category/` or `category/category name/`. Change the category name with the actual category slug. You can access the root categories from the dropdown menu in navbar as well.
  * Detail - is accessible on route `product/jolo/`. Change 'jolo' with product slug if needed. You can access the detail page from the shop when you click on the product as well. 
  * Contact - is accessible on route `contact/`
  * Cart - is accessible on route `order/cart/`. You can also access this page by clicking the cart icon in the navbar 
  * Checkout - is accessible on route `order/checkout/`. You can also access this page by clicking the 'Proceed to Checkout' button on the cart page.
  * Admin Panel - is accessible on `admin/`. SuperUser username is '**admin**' and password is '**admin**'.
  * Login Page - is accessible on `accounts/login/` and by clicking on the კაცუნა icon in the navbar.
  * Registration Page - is accessible on `accounts/register/` and by clicking the 'დარეგისტრირდი' link on the login page at the end of the form.


## **Older Features** ##
* with the help of `order/forms.py`s `CartItemForm()` and AddToCartView which inherits from CreateView new product is added in the cart.
* AddToCartDeleteView which inherits from DeleteView is responsible for deleting the cart item when you press the X button.
* `CartItem` object is created every time the user presses the **"Add to Cart"** button either from the **shop** page or **product detail** page. User's cart is assigned to CartItem. Before the item gets added, program checks if there is products of this amount left in the stock.
* Custom template tag `pagination_filtering.py` which is in `store/templatetags/` makes sure that the pagination works with filtering, search and sorting as well.
* store/category for testing has 2 root categories. They are both displayed in dropdown menu in navbar and have their urls but use the same view as shop. dropdown menu is dynamic so if the new root category gets added it will be displayed as well.
* Cart items count is displayed on the navbar cart icon on every page.
* Slug is automatically generated with the help of Custom ModelAdmin in `store/admin.py`. Custom ModelAdmins are in other apps as well.
* Registration and authorization is implemented with the help of three views.
* `context_processors.py` in utils directory for global context variables.
* `middleware.py` in middlewares directory for updating the last_active_datetime and session's expiry date.
* Added 'LoginRequiredMixin' in views order app to prevent unauthorized users from accessing the pages connected to cart.
* Added 'SearchMixin' in mixins directory to not repeat code for modal search functionality on every view.


## **Components** ##
* **store** - This app contains 5 models(Product, Category, ProductReviews, ShopReviews and ProductTags). Models are self-explanatory. Has 4 Class based views for homepage, contact, product detail and shop.
* **order** - This app contains the models(Checkout(which is the order basically), Cart and CartItems) and 4 class based views for the cart, checkout, one for adding the item to the cart and one for deleting.
* **media** - All user uploaded images go to the media folder.
* **static** - for static files: JS, CSS, Images that is being used are all stored there.
* **user** - Custom User app.
* **utils** - For functions and context processors.
* **templates** - available templates.
* **db.sqlite3** - Database file.
* **mixins** - Custom mixins are stored in this directory.
* **middlewares** - Custom middlewares are stored in this directory.


## Templates
  * cart - in this directory there are components for cart, base_cart.html and cart.html.
  * checkout - in this directory there are components for checkout and base_checkout.html and checkout.html.
  * contact - in this directory there are components for contact and base_contact.html and contact.html.
  * homepage - in this directory there are components for homepage and base_index.html and index.html.
  * product_detail - in this directory there are components for product_detail and base_detail.html and shop-detail.html.
  * shop - in this directory there are components for shop and base_shop.html and shop.html.
  * reusable_components - Here are some reusable components that I'm using through templates and apps such as navbar, spinner and search.
  * base.html - The main base html file where all the shared code is which then is inherited in other templates.
  * footer.html - Footer component
  * registration - This directory contains the html for registration and authorization


## Dependencies
* **Python 3.X**
* **Django 5.1.1**
* **Pillow 11.0.0** - Python Imaging Library adds image processing capabilities to your Python interpreter.
* **Django-debug-toolbar** - Configurable set of panels that display various debug information about the current request/response.
* **Django-mptt** - Reusable Django app which aims to make it easy for you to use MPTT(a technique for storing hierarchical data in a database).
* **django-versatileimagefield~=3.1**
* **python-magic-bin**


## Usage
Clone the repository:
```bash
git clone https://github.com/hella753/caching_error_pages
cd caching_error_pages
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
