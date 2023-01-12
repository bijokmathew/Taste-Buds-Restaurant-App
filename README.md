# Tase Buds Restaurant Booking App

This restaurant booking application built using Django, and allows customer to register and make reservation requests. Customer can view, amend and delete later if it is required. Administrator of the restaurant can also able to accept or decline these requests and view all reservations in order to make business decisions. Key contact details, business hors and the restaurants menu are also provided within the application, as well as links to the companies social media accounts.It is the fourth project in the Code institute Full Stack Developer program.

![image of lighthouse results for desktop](static/images/)
___
## Table of Contents <a name='contents'></a>

* [User Experience (UX)](#userexperience)
* [Design](#design)
* [Development](#development)
* [Database Schema](#database)
* [Existing Features](#existingfeatures)
* [Features Left to Implement](#toimplement)
* [Testing](#testing)
* [Unfixed Bugs](#bugs)
* [Deployment](#deployment)
* [Create a Clone](#clone)
* [Technologies Used](#tech)
* [Credits](#credits)
___
### User Experience (UX) <a name='userexperience'></a>

**Site Goal**

* Overall goal of this website, give nice presentation and customers can easily use the wesite, that generates an interest and curiosity to the customer to visit the restaurant. Customers can see the menu items, shefs details, events and they can contact to the retaurant for further details. Cutomer can easily find the busniness hours and contact number from the webpage. Also they can visit restaurants social media accouts.

* This website gives options to Customer to create an account and they can signin to thier account for booking the table. Also cutomer can view all his booking and they can update/ delete booking in future.
     
* Website administrator can view all reservations and he can accept or decline reservations as per business requirements.

**Target Audience**
    
* There is a potentially large target audience for the site, as it may include anyone who wishes to eat at the Taste Buds. However, the venue is well established, chefs are well experienced, events, location and some pictures all are updated in the website. 

**Owner Goals**

* Owner want to run his business efficiently. He should able to view all the customer booking, owner can able to decline the booking request based on the business needs.

**How These Goals are Addressed**
    
* The ability to create, view, amend and cancel reservations is addressed through the use of account, super user creation and a booking form with various methods of validation which allows for efficient business running.

* Contact details and social media links are provided in the footer of the site, as per industry standard.

* The ability to accept or decline bookings is handled through the use of a site admin panel
  
* The website UI is designed with the help boostrap theme, account authentication achieved with help django allauth and all forms created with the help of cispy form

**Data Required**
    
* As intial paln to develop a MVP product so that very minimum data required is stored on the site, this includes the users name, email, gusts number, booking data and time. These fields are required for user authorization and making reservations. 

**Security Features**
    
* User authorization is handled via the django allauth package and a sign-in/sign-out feature. Only the registered site user can make booking and view, amend and cancel thei booking . The singed in status of the user is always highlighted as well.

* The csrf token is used on the booking form to prevent csrf attacks .


[Return to Table of Contents](#contents)
___
### Design <a name='design'></a>
