# Documentation CSV-Only Repository App

This web app is a sample project built using Python 3 and the Flask microframework. The intent is to create a simple-to-use web application that can upload size-restricted csv only files to a database, allow the user to view the names of stored csv files, and download as needed. It has been designed with employees who do not regularly write code but work with data through a graphic user interface in mind. 

## GETTING STARTED

As this is a proof of concept, you will find that the database has been created as well as the first table populated with several csv files. However, an additional python script was included so this quick-start database would not be necessary.

First, launch your preferred virtual environment as we have a txt file with requirements necessary for running the web app. If this is your first time building and activating a virtual environment, you can find a cheat sheet of the three most popular at the link below. https://conda.io/docs/_downloads/conda-pip-virtualenv-translator.html

Once your virtual environment has been set up and activated, install the python packages required for the app via the requirements txt file. 

From the command line:

cd to the directory where you saved the app. Ensure requirements.txt is in the same directory.

activate your virtual environment if you have not done so already

`pip install -r requirements.txt`

## FROM SCRATCH

If you wish to have a clean start, there is a python script “firstrun.py” which will create your database and build the schema. This is included for convenience and to provide the option of a different database than the one provided. The app will work using either method. 

`python firstrun.py`

The script is fast and will notify you that the SQL database has been created and you may now launch the app.

### LAUNCHING THE APP

`python app.py`

You are now ready to open your browser and head to the following URL:

http://localhost:5000

This is the homepage for the app. At the top of the page, you will see a navigation bar with links to the home page, an about page, and a dashboard. The “about” page gives a brief description of the web app project along with a link for additional information about the Flask microframework. The dashboard will render a table of all the csv files currently in the database.

### LOADING A NON-CSV FILE

Should you attempt to upload a non-csv file, you will be redirected to an error page explaining that the app only works with small csv files. Additionally, csv files over the preset size parameters will render a 413 error. 

### LOADING A CSV FILE

Click the “Choose File” button and select a small csv file. For the purposes of this demonstration, several csv files have been included.

Click the blue “Upload csv file” and the app will alert you that the upload was successful on the dashboard page.

### DASHBOARD

You can navigate to the dashboard either by successfully loading a small csv file or by clicking on “Dashboard” on the navigation bar. The dashboard is a simple table of all the csv files successfully loaded into the database. A user simply needs only to click on their file of their choosing in order to download the csv file. The green “Upload a CSV File” button will take the user back to the homepage.

### NAVIGATING STORED DATA

For the coders, the data in the database can be accessed from the command line using sqlite3

`sqlite csvtodbapp.db`

you can see the tables and schema with the following commands:

`.tables`

`.schema`

For a quick query, you can run the following:

`select * from csv_file where record_id=1;`
