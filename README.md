# SMC App (v1.0)
This app utilizes flask to create a simulated auction site that utilizes SMC to safely monitor the transfer of biddings and communication between bidders

## Takeaways
* Flask is used to create a web interface. Understanding is required of how flask interacts with templates and HTTP Methods.
* Pickle files are used (.pkl) that includes encrypted username/password. These can be modified to suit a developers requirements. These files are used to represent a database, since our demo wishes to focus on SMC and interaction between users and the server we have used these to minimize complexity.
* To run the app:
  1. Install all requirements (see requirements.txt)
  2. Run 'python app.py'. This will start the flask app.

* The following files are included/used in the project:
  * app.py: Main Flask app and backend "server"
        * Provides interactions as seen as "Application" in the sequence diagrams
  * createaccount.py: Used to create new accounts and assign keys to each user (Stores in UserDB.pkl)
  * yaotest.py: Used to test Yao's millionare problem (and for some server functionality)
  * static/: Library for css and js
  * templates/: HTML files
        * auction.html: Main file for auction homepage, does cookie management and javascript of the client-side application (user-based bid verification)

  * .pkl and .ini files are used as "database" representation (for data storage). In the future this would be modified to be a secure database but for simplicity we used .pkl files. 


**Note:** This is a personal application not designed for commercial or widespread use. The code is an initial draft of the application for educational purposes.
