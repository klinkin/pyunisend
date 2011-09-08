#!/usr/bin/env python
#-*-coding:utf8-*-

import urllib
import urllib2
try:
    import simplejson as json
except ImportError:
    import json

class PyUniSend(object):
    errorMessage = ''
    errorCode = ''

    def __init__(self, api_key='', lang='ru', secure=False, format='json', test_mode=False, extra_params = {}):
        """
            Cache API key, lang, secure, format and address.
        """
        self.api_key = api_key
        self.lang = lang
        self.secure = secure
        self.format = format
        self.test_mode  = test_mode

        self.default_params = {'api_key':api_key, 'format':format, 'test_mode':test_mode}
        self.default_params.update(extra_params)
        if secure:
            self.base_api_url = 'https://www.unisender.com/%s/api/' % (self.lang)
        else:
            self.base_api_url = 'http://api.unisender.com/%s/api/' % (self.lang)

    def call(self, method, params = {}):
        url = self.base_api_url + method
        params.update(self.default_params)

        params = urllib.urlencode(self.http_build_query(params), doseq=True)

        request = urllib2.Request( url, params, {"User-Agent": "PyUniSender 0.1.0"})
        response = urllib2.urlopen(request)

        result = json.loads(response.read())

        try:
            if 'error' in result:
                self.errorMessage = result['code']
                self.errorCode = result['error']
        except TypeError:
            pass # exception for non-iterable (boolean) types

        return result

    def __getattr__(self, method_name):

        def get(self, *args, **kwargs):
            params = dict((i,j) for (i,j) in enumerate(args))
            params.update(kwargs)
            return self.call(method_name, params)

        return get.__get__(self)

    def http_build_query(self, params, key=None):
        """
        Re-implement http_build_query for systems that do not already have it
        """
        ret = {}

        for name, val in params.items():
            name = name

            if key is not None and not isinstance(key, int):
                name = "%s[%s]" % (key, name)
            if isinstance(val, dict):
                ret.update(self.http_build_query(val, name))
            elif isinstance(val, list):
                ret.update(self.http_build_query(dict(enumerate(val)), name))
            elif val is not None:
                ret[name] = val

        return ret