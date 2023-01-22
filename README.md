 Tase Buds Restaurant Booking App

This restaurant booking application built using Django, and allows customer to register and make reservation requests. Customer can view, amend and delete later if it is required. Administrator of the restaurant can also able to accept or decline these requests and view all reservations in order to make business decisions. Key contact details, business hors and the restaurants menu are also provided within the application, as well as links to the companies social media accounts.It is the fourth project in the Code institute Full Stack Developer program.

![image of lighthouse results for desktop](static/images/)
___
- ## Table of Contents

  - [User Experience (UX)](#user-experience-ux)
    - [Site Goal](#site-goal)
    - [User stories](#user-stories)
    - [Target Audience](#target-audience)
    - [Owner Goals](#owner-goals)
    - [Data Required](#data-required)
    - [Security Features](#security-features)
  - [Design](#design)
    - [Wireframes](#wireframes)
    - [Database Schema](#database-schema)
  - [Development](#deployment)
  - [Existing Features](#existing-features)
    - [Landing Page](#landing-page)
    - [TopBar](#topbar)
    - [Navigation](#navigation)
    - [Footer](#footer)
    - [User Creation](#user-creation)
    - [User SignIn/SignOut](#user-signinsignout)
    - [About](#about)
    - [Menu](#menu)
    - [chef](#chefs)
    - [Gallery](#gallery)
    - [Book a Table](#book-a-table)
    - [My Booking](#my-booking)
    - [Delete Booking](#delete-booking)
  -[Future Features](#future-features) 
  -[Testing](#testing)
    -[User Stories](#user-stories)
    -[Testing User Stories from User Experience (UX) Section](#testing-user-stories-from-user-experience-ux-section)
    -[Fixed issues](#fixed-issues)
    -[Remaing issues](#remaining-issues)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks & Toolkits](#frameworks--toolkits)
    - [Database](#database)
    - [Cloud Services](#cloud-services)
    - [Server](#server)
    - [Version Control](#version-control)
    - [Libraries, Packages and Applications](#libraries-packages-and-applications)
    - [Programs](#programs)
  - [Deployment](#deployment)
  - [Deploying with Heroku](#deploying-with-heroku)
    - [Create a Local Clone ](#create-a-local-clone-)
    - [Forking the GitHub Repository](#forking-the-github-repository)
___
## User Experience (UX)
### Site Goal

* Overall goal of this website, give nice presentation and customers can easily use the wesite, that generates an interest and curiosity to the customer to visit the restaurant. Customers can see the menu items, shefs details, events and they can contact to the retaurant for further details. Cutomer can easily find the busniness hours and contact number from the webpage. Also they can visit restaurants social media accouts.

* This website gives options to Customer to create an account and they can sign-in to thier account for booking the table. Also cutomer can view all his booking and they can update/ delete booking in future.
     
* Website administrator can view all reservations and he can accept or decline reservations as per business requirements.

### User stories

  #### First Time Visitor Goals
   * As a first time visitor I can find business hours , contact details, address.
   * As a first time visitor I can find out what kind of food they serve from their menu.
   * As a first time visitor I can find information about how to make a reservation at the restaurant.
   * As a first time visitor I can send a message to the restaurant for any specific information
        
  #### Frequent Visitor Goals
   * As a frequent visitor I can create an account so that I can make a reservation online.
   * As a frequent visitor I can view the menu before booking the table.
   * As a frequent visitor I can login and find my current bookings.
   * As a frequent visitor I can change or cancel my prevoius booking

 ### Target Audience
    
* There is a potentially large target audience for the site, as it may include anyone who wishes to eat at the Taste Buds. However, the venue is well established, chefs are well experienced, events, location and some pictures all are updated in the website. 

### Owner Goals

* Owner want to run his business efficiently. He should able to view all the customer booking, owner can able to decline the booking request based on the business needs.

**How These Goals are Addressed**
    
* The ability to create, view, amend and cancel reservations is addressed through the use of account, super user creation and a booking form with various methods of validation which allows for efficient business running.

* Contact details and social media links are provided in the footer of the site, as per industry standard.

* The ability to accept or decline bookings is handled through the use of a site admin panel
  
* The website UI is designed with the help boostrap theme, account authentication achieved with help django allauth and all forms created with the help of cispy form

### Data Required
    
* As intial paln to develop a MVP product so that very minimum data required is stored on the site, this includes the users name, email, gusts number, booking data and time. These fields are required for user authorization and making reservations. 

### Security Features
    
* User authorization is handled via the django allauth package and a sign-in/sign-out feature. Only the registered site user can make booking and view, amend and cancel thei booking . The singed in status of the user is always highlighted as well.

* The csrf token is used on the booking form to prevent csrf attacks .


[Return to Table of Contents](#table-of-contents)
___

## Design

* The theme for the project were chosen in accordance with the intended target market in mind for the restaurant. With its fancy 
  looks and feel, dark colors and luxurious details and effects, the theme fits perfect for the goal of giving the visitor the impression that this is a very high quality restaurant.

* Colors  
  
  The main colors are overall dark shade of grey, white and Sea Buckthorn to provide an elegant look and feel. Furthermore, elements such as buttons, icons, symbols, links and headings are made in gold color that follows the pattern of elegance and adds to the premier look and feel of the webpage.

* Font
  The fonts in the theme are clear and modern and contribute perfectly to the overall elegant setting.

* Images  
  The images in the theme provide great content and presentation of the restaurant and serves as an enticement for the visitors.  

## Wireframes  
* A separate document for the wireframes can be viewed here: 
    - [For Desktop view](docs/)
    - [For Mobile view](docs/)    

## Database Schema  
  The database design schema can be viewed below. It consists of a Booking model with a foreignKey of User that relates to the Django standard User model class.  
    ![dbschema](docs/img/)  

[Return to Table of Contents](#table-of-contents)
___

## Development

* The project was developed with the help agile methodology. During the design process collect the project requirements and write epics broken down into user stories with well defined acceptance criteria and tasks list. Based on the priority move those user stories in to different project sprint cycle like First cycle, Second cycle and Third Cycle in order to achieve MNP.Once finished the user stories moved those stories into closed state and if all issues related to the sprint closed then move the sprint cycle also in to closed state. During the development time got an enhancement ideas, create stories and moved in to backlog with priorities.

- **Product Backlog**
    * The product backlog for the project can be found [here](https://github.com/bijokmathew/Taste-Buds-Restaurant-App/milestone/4)

    * Project's all user stories on board can be found [here](https://github.com/users/bijokmathew/projects/7)
    * Project all spring cycle can be found [here](https://github.com/bijokmathew/Taste-Buds-Restaurant-App/milestones?state=closed)
   
- **First Cycle**
    * The First Cycle milestone can be found [here](https://github.com/bijokmathew/Taste-Buds-Restaurant-App/milestone/1?closed=1)
    ![image of the First Cycle board](static/images/)

- **Second Cycle**
    * The Second Cycle milestone can be found [here](https://github.com/bijokmathew/Taste-Buds-Restaurant-App/milestone/2?closed=1)
    ![image of the iteration 2 board](static/images/)

- **Third Cycle**
    * The Third Cycle milestone can be found [here](https://github.com/bijokmathew/Taste-Buds-Restaurant-App/milestone/3?closed=1)
    ![image of the iteration 3 board](static/images/)

[Return to Table of Contents](#table-of-contents)
___

## Existing Features

   ### Landing Page

  * The landing page features a hero image with a brief description of the restaurant, it's facilities and accessibility level. The landing page is fully responsive built using bootstrap. Landing page is designed with carousel feature and uses three images.
    
    ![landing page image](static/images/)

   ### TopBar
    
   * TopBar is fully responsive and designed with black color and transparent bacgroud property.Restaurent business details like opening hours and contact number are displayed on topbar.While scrolling or moving to different page then the top bar will disappear and push the navigation bar in the place of topbar   
        
     ![topbar image](static/images)

   ### Navigation
   
   * The navigation bar is fully responsive and responds to the authorization status of the user. If a user is not signed then navbar shows signUp and signIn options and hide signOut and MyBooking option from the navbar.If user is try to book a table without signIn then it shown message to the user that user need to signIn?signUp first.The MyBooking and logout tab are only visible to authorized users.The restaurant name is always displayed to the left hand side for all screen. The navbar is present across all pages of the website, as it provides main source of navigation between content. 

     ![image of the navigation bar with authorized user](static/images/)
     ![image of the navigation bar with non authorized user](static/images/)

   ### Footer
    
   * The footer contains address of the restaurant and social media links to get the updates about the restaurent from social apps. Built to be fully responsive
        
     * [Business Details of Restaurant](https://github.com/bijokmathew/Taste-Buds-Restaurant-App/issues/5)
     ___ 
     ![footer image](static/images/)

   ### User Creation

   * User creation uses the django-allauth package to collect the necessary information needed by the company for account creation.
        
     * [Account Registration](https://github.com/bijokmathew/Taste-Buds-Restaurant-App/issues/1)
     ___
     ![image of the user sign up form](static/images/)

   ### User SignIn/SignOut
   * User can SignIn and SignOut by using the SignIn and SignOut page.
  
     ![image of the user sign in form](static/images/)
     ![image of the user sign out page](static/images/)

   ### About
   * About section built in fully responsive and contain details about the restaurant like seating capacity, special food etc.
     Also contain video link about the restaurant.
      
     ![image of the about section](static/img/)

   ### Menu
   * The menu section present all available menu items in restaurant with image description. Also group the food items on category based like starter, salads etc and category tab is displayed on the top of the menu so that user can easly navigate.
       
     * [view all restaurant menu items](https://github.com/bijokmathew/Taste-Buds-Restaurant-App/issues/8)
     ___
     ![image of the menu section](static/img/)
   ### Chefs
   * The chef section built in full responsive and present main chefs details like name, role and social links
     ![image of the chefs section](static/img/)

   ### Gallery
   *  Gallery section built in full responsive and display some images of restaurant.
     ![image of the gallery section](static/img/)

   ### Book a Table
   * Booking table option takes the user to booking form to collects all the information needed for the venue to make a reservation request.User not allowed to book a table for previous dates and this is achived by adding the validation check on date and time fields.Double bookings are prevented via a unique constraint on the user, date and time fields from within the model and any validation error send back and displayed in the booking form field.
        
     * Date - Validation to ensure it's a future date 
     * Time - Validation to ensure the requested time future time.
     * Amend Reservation - Ensures the user attempting to alter the reservation is the owner.
     ___
     * [Book a table](https://github.com/bijokmathew/Taste-Buds-Restaurant-App/issues/2)
     * [Double Bookings](https://github.com/bijokmathew/Taste-Buds-Restaurant-App/issues/7)
    
     ---
     ![image of the booking form](static/images/)

   ### My booking
   * My booking display all the future booking details of the user.It wont display the past booking details and it is achieved by filter the booking data from the model with current data and time.Also My booking given option for modifying or canceling the current booking. Modifying the existing booking will follow the same process of book a table.
     * [Manage My Booking](https://github.com/bijokmathew/Taste-Buds-Restaurant-App/issues/4)
     * [View all table Bookings](https://github.com/bijokmathew/Taste-Buds-Restaurant-App/issues/3)
     * [Edit My booking details](https://github.com/bijokmathew/Taste-Buds-Restaurant-App/issues/6)
     ---
     ![image of the my booking ](static/images/)
     ![image of the edit booking ](static/images/)

   ### Delete booking
   * When user select on the "delete" button in booking details of the mybookings page, a warning message is shown to prevent Customers from deleting their bookings by mistake. 

     ![image of the delete booking](static/img/)

[Return to Table of Contents](#table-of-contents)
___
## Future Features

  * The product backlog can be viewed [here](https://github.com/bijokmathew/Taste-Buds-Restaurant-App/milestone/4).

   ### Admin can manage Menu Items

   * Admin should have control to add, delete or modify the menu items by using admin panel. Currently the menu items are hard coded in the application.In furure we have to create a Model for managing the menu items. I already created an issue and added to the backlog
     [Admin can manage Menu](https://github.com/bijokmathew/Taste-Buds-Restaurant-App/issues/14)

   ### Admin can manage the seating capacity

   * Admin should able to add, modify or delete the table capacity by using admin panel. Currently there is no such option in the application. In future , create a model for managing the table capacity and linked to the existing Booking model. I already created an issue and added to the backlog
     [Admin able to manage the seating capacity](https://github.com/bijokmathew/Taste-Buds-Restaurant-App/issues/13)

   ### Automated Emails

   * User receives automated emails whenever their booking is accepted.I already created an issue and added to the backlog.
     [Email notification regarding the booking status](https://github.com/bijokmathew/Taste-Buds-Restaurant-App/issues/11)

   ### Remember Me 

   * User able to set remember me option while login so that he no need to eneter the credential again by visiting the page in the same device. Currently this feature is disabled. In futute we need to implement by using django-allauth.I already created an issue and added to the backlog
     [Remember Me functionality in Login Page](https://github.com/bijokmathew/Taste-Buds-Restaurant-App/issues/9)

   ### Password Reset

   * Build a feature which gives users the ability to reset the password on their account.I already created an issue and added to the backlog
  
     [Password Reset](https://github.com/bijokmathew/Taste-Buds-Restaurant-App/issues/10)

[Return to Table of Contents](#table-of-contents)
___

## Testing
* Testing done throughout the process while developing the project by the use of Django debug pages and printing statements to check that the code functioned accordingly. In addition, thorough testing has been performed and is described below, it contains of manual test to check that all user stories and acceptance criteria are met, as well as testing and validating the code with different online tools as presented below.


### Test Cases 
### User Stories
&nbsp;
#### Menu page

| Description  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Customer can view menu page | Test menu link and child links within the menu page | Being able to open and browse the menu without errors | PASS |
| Customer can view menu categories | Test menu categories on the menu page | Being able to open and browse the menu categories without errors | PASS |
&nbsp;
#### Home page

| Description  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Customer can view home page | Open the webpage link in the browser | Being able to lanuch the homepage and user has to scroll the homepage without any issues   | PASS |
| Customer can view restaurant details like contact, opening hours and address etc | Open the webpage link in the browser and check the topbar, footer, gallery, about, etc | User able to find the address, contact, opening hours in the homepage.Also he can browse and read other items on the homepage without any issues | PASS |
&nbsp;
#### Registration 

| Description  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Customer signup page | Select SignUp link from navbar| Customer should directed to the signup page | PASS |
| Customer signup - Empty Form validation | Submit empty form | Form validation error should display to the user | PASS |
| Customer signup - Email Field validation | Submit invalid email address | Email filed validation error should display to the user | PASS |
| Customer signup - password field validation | Submit invalid password | Passwoed field validation error should display to the user | PASS |
| Customer signup - password  mismatch validation | Submit non matching passwords | password mismatch validation error should display to the user | PASS |
| Customer signup - Existing user validation | Submit already existing username | username already exists validation error should display to the user | PASS |
| Customer SignIn page | Select SignIn link from navbar | Customer should directed to the login page | PASS |
| Customer SignIn - Empty Form validation | Submit empty form | Empty Form validation error should display to the user | PASS |
| Customer SignIn - Incorrect password validation | Submit incorrect password | Password field validation error should display to the user | PASS |
| Customer SignIn - Incorrect name validation | Submit incorrect name | Name field validation error should display to the user | PASS |
| Customer SignOut page | Select SignOut link from navbar | User should ask confirmation about logged out | PASS |
| Customer SignOut confirmation alert | Select SignOut from the confirmation | User should logged out and go to homepage | PASS |
&nbsp;
#### Bookings 
| Description  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Customer Booking page | Select booking a table from navbar | Customer should direct to the booking page | PASS |
| Form validation Booking page | Check that each required field is working correctly in the form | Form validation error should display to the user if any validation failed | PASS |
| Submit button Booking page | Click the submit button to check that the booking details is saved in to DB | Sucess message and redirect to mybooking page | PASS |
| Double booking | Try to book with already existing date and time | Booking should not saved, shows an alert to user for double booking  | PASS |
| Booking for previous date | Try to bbok a table for previous date | Booking should not saved, shows an alert to user for invalid date of booking  | PASS |
| Bookings are shown on mybookings page | Check that each booking for a user are shown on the mybookings page | Individual cards of each booking is shown with the corresponding booking details | PASS |
| previos dates Bookings on mybookings page | Check previous dated booking listed on the mybooking page  | Mybooking page should not display the previous dated bookings | PASS |
| Bookings can be edited | Check that the edit button works and that the updated booking is submitted to the mybooking page when edited | Booking is updated with the corresponding booking details | PASS |
| Bookings can can be deleted | Check that the delete button works and that the deleted booking is removed from the mybooking page when deleted | Mybooking list is updated | PASS |
&nbsp;
#### Navbar
| Description  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Navbar | Check that each link is working correctly | Customer is able to open each link to browse the webpage for information about the restaurant | PASS |
&nbsp;
#### Admin
| Description  | Steps | Expected Outcome | Results |  
| - | - | - | - |
| Admin login - Form password validation | Submit incorrect password | Password validation error should display to the user | PASS |
| Admin login - Form name  validation | Submit incorrect name | Name validation error should display to the user | PASS |
| Admin login - Empty Form validation | Submit empty form | Empty Form validation error should display to the user | PASS |
| Admin panel update booking | Go to Admin page and try to update bookings | Booking should updated with the corresponding booking details | PASS |
| Admin panel delete booking | Go to Admin page and try to delete bookings | Booking should removed from current booking list and from Model | PASS |
| Admin panel view booking | Go to Admin page and check the booking listed with specified details | Booking should list with staus, name , date of booking, time  | PASS |
| Admin panel filter  booking | Go to Admin page and check filter options are working | Admin can filter the booking list based booked-status, booked time, user, | PASS |
| Admin panel search for booking | Go to Admin page and check search funtion is working | Admin can search in the booking list based name, booked time, number of guest | PASS |
| Admin panel filter for booking | Go to Admin page and check filter options are working | Admin can filter the booking list based booked-status, booked time, user | PASS |
| Admin panel accept/decline booking | Go to Admin page and check accept/decline options are working | Admin can accept/decine the booking and booking status should updated accordingly | PASS |
&nbsp;
### Testing User Stories from User Experience (UX) Section
  #### First Time Visitor Goals
   * As a first time visitor I can find business hours , contact details, address.
      * User can find the business hours, cotact details on topbar and address on the footer  
   * As a first time visitor I can find out what kind of food they serve from their menu.
      * User can go to food menu from the navbar as well as from the hearo section.In menu page food catogeries also listed
   * As a first time visitor I can find information about how to make a reservation at the restaurant.
      * User can find Book a Table option on navbar and hero section.If user not signIn then ask to SignIn or SignUp for booking 
   * As a first time visitor I can send a message to the restaurant for any specific information
      * User can go to contact form from navigation link and user can enter the details and message to send to restaurant 
        
  #### Frequent Visitor Goals
   * As a frequent visitor I can create an account so that I can make a reservation online.
      * User can create account by using SignUp link from the navbar  
   * As a frequent visitor I can view the menu before booking the table.
      * User can go to food menu from the navbar as well as from the hearo section.In menu page food catogeries also listed 
   * As a frequent visitor I can login and find my current bookings.
      * User can login by using SignIn link from navbar and can view booking by using mybooking link in navbar 
   * As a frequent visitor I can change or cancel my prevoius booking
      * User can find option delete/edit on indivijual booking deatils


&nbsp;
### Fixed Issues


|Issues Details | Solution | Status |
|----|:---------|:-------|
|navigation links are not working from new page like signIn, signOut, signUp, mybooking pages| updated the urls like home urls+navigation list id  | Fixed |
|My booking layout for cards to display the booking details are not same height| By using flex display and align-item-stretch property  | Fixed |
|Past booking details displaying on my booking page | Filter the booking data from db based on current date and time | Fixed |
|A user can delete another user's bookings| Add authorization check to the delete_booking function | Fixed |
|A user can update another user's bookings| Add authorization check to the edit_booking function | Fixed |
|A user can show another user's bookings| Add authorization check to the mybookings_page function | Fixed |


### Remaining Issues
  - No known ssues

[Return to Table of Contents](#table-of-contents)
---

## Technologies Used

- ### Languages Used

    * HTML
    * CSS
    * JAVASCRIPT
    * PYTHON
    * MARKDOWN

- ### Frameworks & Toolkits

    * **[Django 3.2](https://www.djangoproject.com/download/).**
        * Python based web framework, used to build the application.
    
    * **[Bootstrap 5.2](https://getbootstrap.com/).**
        * Bootstrap restaurant app themes used in this project.
    
    * **[Font Awesome](https://fontawesome.com/).**
        * Icon set and toolkit used across the application.

- ### Database
    
    * **[PostgreSQL](https://www.postgresql.org/).**
        * The relational database management system used.

- ### Cloud Services

    * **[Heroku](https://id.heroku.com/login).**
        * Used to deploy project.

    * **[Cloudinary](https://cloudinary.com/).**
        * A cloud-based image and video management service. Used due to Heroku using an ephemeral file system. 

- ### Server

    * **[Gunicorn](https://gunicorn.org/).**
        * The server used to run Django on Heroku.

- ### Version Control
    
    * **Git.**
        * Git was used for version control by utilizing the GitPod terminal to commit to Git and Push to GitHub.

    * **[GitHub](https://github.com/).**
        * GitHub is used to store the projects code.
    
    * **[Gitpod](https://www.gitpod.io/docs/).**
        * The IDE used to build the project.

- ### Libraries, Packages and Applications

    * **[dj_database_url](https://pypi.org/project/dj-database-url/).**
        * A PostgreSQL supporting library. Allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
    
    * **[pyscopg2](https://www.psycopg.org/docs/).**
        * PostgreSQL database adapter for the Python programming language.
    
    * **[dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/).**
        * a Django package that facilitates integration with Cloudinary.
    
    * **[allauth](https://django-allauth.readthedocs.io/en/latest/installation.html).**
        * Used for creation and maintenance of user accounts.
    
    * **[crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/index.html).**
        * Used for rendering the booking form from the model.
    
    * **[coverage](https://coverage.readthedocs.io/en/6.3/).**
        * Used to access the coverage of automated tests for the python code i've wrote.
        
- ### Programs

    * **Slack.**
        * Specifically the peer-code_review channel on Code Institutes Slack workspace. Used to increase the scope of my testing.
    
    * **Balsamiq.** 
        * Used to create the wire frames during the development process.
       
[Return to Table of Contents](#table-of-contents)
___

## Deployment

### Deploying with Heroku

- The site is deployed via [Heroku](https://heroku.com/). The steps to deploy are as follows:

    * Create the GitHub repository for the project and make the intial setup.*

    * Django project is setup as intended, necessary dependencies like cloudinary, dj-database-url, django-allauth, django-crispy-forms, gunicorn, psycopg2 etc installed with all apps required added to the INSTALLED_APPS variable within settings.py.*

    * Ensure all requirements for the project are added to the requirements.txt file prior to deployment by using the command **pip3 freeze --local > requirements.txt**.*

    * STAGE ONE - Create a New App in Heroku

        1: From the dashboard on Heroku, select New and then Create new app.
        
        2: Enter an individual app name into the text box, select a relevant region from the dropdown and then press Create app.
        
        3: A Heroku app has now been created.
    
    ---
    
    * STAGE TWO - Create and add a postgresql database

        1: Open elephantsql.com site.

        2: create a new instance and select plan and region.
        
        3: Copy the database url from the created database instance.

        4: In heroku, add 'DATABASE_URL' Config Vars with copied database url string.

        5: Create a env.py file within the project and use the copied database url to create a DATABASE_URL environment variable. The Python OS module will be required for this to run the project locally from gitpod.

        *The env.py file is used to protect keys which should only be viewed by the developer. This file will not be pushed to GutHub for public display.*

    ---
    
    * STAGE THREE - Create a SECRET_KEY

        1: Within the env.py file, create a SECRET_KEY environment variable. The string for this variable is decided by the developer.

        2: On the settings tab of the Heroku app, reveal config vars and add the SECRET_KEY variable along with the corresponding string.

    ---
    
    * STAGE FOUR - Update the settings.py file

        1: Import dj_database_url and env.py into the settings.py file within the project.

            import dj_database_url
            if os.path.isfile('env.py'):
                import env

        2: Update the default SECRET_KEY variable provided by Django to the SECRET_KEY environment variable.

            SECRET_KEY = os.environ.get('SECRET_KEY')

        3: Using an if/else statement update the DATABASES dictionary for the deployed project to use the DATABASE_URL environment variable, the dj_database_url library is utilized here.

            if development:
                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': BASE_DIR / 'db.sqlite3',
                    }
                }
            else:
                DATABASES = {
                    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
            }
        
        *The database for developing the project remains as the sqlite one provided*

        4: Preform a migration.

        *The Heroku database is now being used as the backend, within the resources tab of the app, the Heroku Postgres link will bring up a window demonstrating this.*

    ---

    * STAGE FIVE - Connect app to Cloudinary

        * Create a Cloudinary account.*

        1: On the Cloudinary website, copy the API environment variable string.

        2: Within the projects env.py file create a CLOUDINARY_URL environment variable equal to this copied string.

        3: Within the Heroku app, on the settings tab, update the config vars to contain this variable.

        *For initial deployment, a variable called DISABLE_COLLECTSTATIC is also created within the config vars at this point with a value of 1, this is simply to get the skeleton project deployed for testing purposes and removed when deploying the completed project*

        4: Within the Heroku app, on the settings tab, add 'PORT' config var with value '8000'.

        4: Within the settings.py file on the project, under INSTALLED_APPS, 'cloudinary_storage' and 'cloudinary' must be added.

        5: Django must then be told to use Cloudinary to store media and static files, this is done by adding the below variables to the relevant section of the settings.py file:
            
            STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
            STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
            STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
            MEDIA_URL = '/media/'
            DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
        
        *The app is now linked to Cloudinary*
    
    ---
     
    * STAGE SIX - Tell Django where the templates are stored

        1: Under the BASE_DIR on settings.py, add in the below templates directory. 
        
            TEMPLATES_DIR =  os.path.join(BASE_DIR, 'templates')
        
        2: Then within the TEMPLATES setting, update the DIRS key to point towards this variable.

            'DIRS': [TEMPLATES_DIR]
    
    ---
    
    * STAGE SEVEN - Update ALLOWED_HOSTS
        
        1: Create 'DEVELOPMENT' variable with value True in env.py file

        2: In setting.py try to assign the 'DEVELOPMENT' value from env, if it is no defined then assign value as False
           
           development = os.environ.get('DEVELOPMENT', False)

        3: At this point, within settings.py, set the DEBUG variable to development.

        4: Using an if/else statement update the ALLOWED_HOSTS variable for the deployed project to be the name of your Heroku app with ".herokuapp.com" appended to the end.

            DEBUG = development

            if development:
                ALLOWED_HOSTS = [
                    'localhost',
                ]
            else:
                ALLOWED_HOSTS = ['taste-buds-restaurantapp.herokuapp.com']

        *For development the host is set to localhost, so that the project can be ran locally. This is also a good point to add the Media, Static and Template directories, these folders should be added at the top level.*
    
    ---
    
    * STAGE EIGHT - Create a Procfile

        1: Create a Procfile at the top level of the directory.

        2: Within this file, declare the below command. This command ensures gunicorn is used as the web server.

            web: gunicorn tastebuds.wsgi
        
        *Add, commit and push to the repository at this point*
    
    ---
    
    * STAGE NINE - Connect the GitHub repository to the Heroku App

        1: Within the Deploy tab on the Heroku app, choose GitHub as the deployment method.

        2: Search for the correct repository and connect.

        3: At the bottom of the deployment section there is an option to chose which branch to deploy. Chose the main branch and allow the build log to complete.

        4: Once complete, chose to allow automatic deployment from here onwards.

        *The app has now been deployed successfully. The live link can be found here - [Taste-Buds-Restaurant-App](https://taste-buds-restaurantapp.herokuapp.com/)*

        **B, from this point onwards, all changes made to the database in development will have to be migrated to the deployed database separately in order to take effect. This can be done by changing the DATABASES dictionary in the settings.py file to point directly at the heroku database, DO NOT commit to GitHub with this setting saved.**

    ---
[Return to Table of Contents](#table-of-contents)
___

### Create a Local Clone <a name ='clone'></a>

- Follow the steps below in order to create a local clone using HTTPS.

    * STEP ONE - Navigate to the GitHub repository for the project. Located [here](https://github.com/bijokmathew/Taste-Buds-Restaurant-App).
    
    * STEP TWO - From the tabs displayed, click the **Code** tab. This presents a drop down menu.

    * STEP THREE - Ensure this menu is on the **HTTPS** tab and copy the URL.

    * STEP FOUR - On your chosen IDE open Git Bash, Change the current working directory to the location where you want the cloned directory.
    
    * STEP FIVE - Type git clone, and then paste the URL you copied earlier.

            $ git clone https://github.com/bijokmathew/Taste-Buds-Restaurant-App.git
    
    * STEP SIX - Press Enter to create your local clone.

    *If GitPod is your chosen IDE from the link above the Gitpod button can be clicked to open up the repository code on your local machine* 

[Return to Table of Contents](#table-of-contents)
___

### Forking the GitHub Repository

- Follow the steps below in order to fork the project from github.

    * STEP ONE - Navigate to the GitHub repository for the project. Located [here](https://github.com/bijokmathew/Taste-Buds-Restaurant-App).
    
    * STEP TWO - In the right most top menu, click the "Fork" button.

    * STEP THREE - There will now be a copy of the repository in your own GitHub account.
   
[Return to Table of Contents](#table-of-contents)
___
