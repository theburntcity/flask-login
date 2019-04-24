# Setting up flask-login with postgres 

This is a method to create a secure portion of your website.  
Any pages you want to secure, you just add @login_required under the @app.route.  
  
The ini file should look like this:  
[postgresql]  
host=localhost  
database=whatever your database name is  
user= whatever your username is  
password=whatever your password is  
  
[flask]  
secret_key=    
[this site](https://passwordsgenerator.net/) is a good password/key genraerator. 


