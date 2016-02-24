## Requirements
1. latest Python 2.*
2. vagrant vm correctly installed
3. Flask installed
4. Flask-WTF installed
5. Flask-Seasurf installed
6. you have created your own web app in google and facebook and obtained Id and secret
7. make sure your callback url is http://localhost:8000
8. download your google app secret json and rename it as "g_client_secrets.json"
9. make your own facebook client secrets file follow the example_fb_client_secrets.json and rename it as fb_client_secrets.json

## Quick Start:
1. Clone the repository
2. Launch the Vagrant VM, ssh into the VM
3. Run `database_setup.py` to set up sqlite database
4, Run `lotsofitems.py` to populate items into database
5. Run the `project.py` to start the web server
6, Open your browser in incognito window and enter `localhost:8000`

## Basic Functionality

##### `Google and Facebook login`: 
* You can login using Google or Facebook account.

##### `View categories and items information`: 
* You can view all categories and items information. 

##### `Add, Edit, Delete item`: 
* You can add item once you login.
* You can edit or delete the items you create once you login

##### `Json API to access all categories and its items information`: 
* A Json API is provided to access all categories and its items information. the url for it is: http://localhost:8000/catalog.json

##### `XML API to access all categories and its items information`: 
* A XML API is provided to access all categories and its items information. the url for it is: http://localhost:8000/catalog.xml

## Enhancements
1. Allow user to add item image
2. Provide csrf protection in the item add, edit and delete page

## Comments

To test the functionality, you can refer to: https://storage.googleapis.com/supplemental_media/udacityu/3487760229/P3ItemCatalog-GettingStarted.pdf