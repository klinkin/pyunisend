#PyUniSend
PyUniSend is a simple API wrapper for interacting with https://www.UniSender.com
##Requirements
Python 2.7 or later.  
A UniSend.com account and API key. You can see your API keys [here](https://www.unisender.com/ru/user_info).
##Installation
    pip install pyunisend
##Usage
    from pyunisend import PyUniSend
    api = PyUniSend('YOUR APIKEY')
    api.getLists()

## Notes
API parameters must be passed by name. For example:  

    api.createList(title='NewList')

##Copyrights

* Copyright (c) 2011 Klimin Mikhail. Please see LICENSE.txt for details.