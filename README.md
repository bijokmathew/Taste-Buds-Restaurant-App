 Tase Buds Restaurant Booking App

This restaurant booking application built using Django, and allows customer to register and make reservation requests. Customer can view, amend and delete later if it is required. Administrator of the restaurant can also able to accept or decline these requests and view all reservations in order to make business decisions. Key contact details, business hors and the restaurants menu are also provided within the application, as well as links to the companies social media accounts.It is the fourth project in the Code institute Full Stack Developer program.

![image of lighthouse results for desktop](static/images/)
___
- ## Table of Contents

  - [User Experience (UX)](#user-experience-ux)
    - [Site Goal](#site-goal)
    - [Target Audience](#target-audience)
    - [Owner Goals](#owner-goals)
    - [Data Required](#data-required)
    - [Security Features](#security-features)
  - [Design](#design)
  - [Wireframes](#wireframes)
  - [Database Schema](#database-schema)
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

[Return to Table of Contents](#contents)
___

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
