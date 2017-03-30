#PyUniSend
PyUniSend is a simple API wrapper for interacting with [unisender.com](http://www.unisender.com/ru/?a=112233)

##Requirements
Python 3 or later.
A UniSend.com account and API key. You can see your API keys [here](https://www.unisender.com/ru/user_info/?a=112233).

##Installation
    https://github.com/qari/pyunisend.git

##Usage
    from pyunisend import PyUniSend
    api = PyUniSend('YOUR APIKEY')
    api.getLists()

    # For SMS
    from pyunisend import PyUniSend
    api = PyUniSend('YOUR APIKEY')
    api.sendSms(phone='******', sender='***', text='Test')

## Notes
API parameters must be passed by name. For example:  

    api.createList(title='NewList')

##Copyrights

* Copyright (c) 2017 Klimin Mikhail + MG. Please see LICENSE.txt for details.