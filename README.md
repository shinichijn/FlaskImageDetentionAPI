# flask_api  
This is a web API service only works for machines on the same local network
Tested in PyCharm

# Requirements  
Python 3.6 or higher  
Flask `pip install flask`  
Pillow `pip install pillow`  
Keras `pip install keras`  
Tensorflow `pip install tensorflow`  
  
If they don't work please do `sudo pip install` instead  

# Setup  
Create a folder called 'models' where app.py is  
Download the model from [GoogleDrive](https://drive.google.com/open?id=1T6rzv3NnYFlWCwDeMwfYm7DKNFGtWNr-) or [DropBox](https://www.dropbox.com/s/zliw6rgr6w1zope/model10.h5?dl=0)  
Put model in the models folder  
like this:  
`models/model10.h5`  

# Run the web service  
In the terminal execute `python app.py`  