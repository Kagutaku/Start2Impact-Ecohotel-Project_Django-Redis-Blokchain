ECOHOTEL WEBAPP (USING DJANGO, REDIS AND ETHEREUM BLOCKCHAIN) 

🚀 Goal of the project

The aim of the project is to implement a system to record the energy generated and used by the Eco Hotel Pomelia's solar panels, using Django, Redis and the Ethereum Blockchain Testnet Goerli.

REQUIREMENTS:

• Data entry of generated and utilized energy in JSON format with POST method

• Record Data on the Blockchain

• Create a homepage to display this information for the logged in user

• Create a web page only for admins that displays specific analytics

• A login system that shows if an admin user logs into the web app from a different IP 

________________________________________

💻 Implemented Features

The implemented features in this project are:

• Registration and login form for users

• A homepage, accessible only to logged-in users, displaying the table with the values in question and the transaction hash

• A page, accessible only to administrators, where you can see the total energy used and generated

• A logging system to store the last IP that accessed the platform for a specific admin user, so as to display a warning message when this differs from the previous one 

________________________________________

🔎 How to run this project:

1- Create a Virtual Environment

2- Clone the repository and install requirements in ecohotel/requirements.txt

3- Make database migrations

4- Install and run Redis Database Server

5- Run python manage.py runserver

6- Open http://127.0.0.1:8000/ in your browser

________________________________________

✉️ Email: bashuri.emanuele1@gmail.com
