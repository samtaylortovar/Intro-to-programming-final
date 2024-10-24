First you need to add ilovecalanderssomuch@gmail.com to your chrome account the password is Byui123!

go to this website: https://developers.google.com/calendar/api/quickstart/python
scroll down till you see the blue button that says "Go to Credentials" and click on the button, make sure that you are logged in as ilovecalanderssomuch
![image](https://github.com/user-attachments/assets/dc101997-0327-40be-b7f7-a1609af64f57)
you'll see this layout.
click on create credidentials then oauth client ID
then on the drop down you should see desktop application as one of the choices, choose that.
the name doesn't matter, you could use your own name if you'd like
Click Create. The OAuth client created screen appears it shows your new Client ID and Client secret.
Click OK. The newly created credential appears.

Save the downloaded JSON file as credentials.json it is REALLY important that its named credentials, and move the file to your working directory (your working directory is wherever you save your code).

Second you need to install the google client library into your console --  where you put user inputs for code ->
copy this into the console:

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

once it installs you can run the code called quickstart.py, i put it as one of the files in github.
if everything works well it should list the next 10 events from google calander into the console...

and thats it!
 if you want to you can try to add an event to the calander using the calanderproject.py and editing the code to make your own event. its really easy.

