import urllib.request
import json


class PyUniSend:
    errorMessage = ''
    errorCode = ''

    def __init__(self, api_key='', lang='ru', secure=False, format_='json', test_mode=False, extra_params={}):
        """
        Cache API key, lang, secure, format and address.
        """
        self.api_key = api_key
        self.lang = lang
        self.secure = secure
        self.format = format_
        self.test_mode = test_mode

        self.default_params = {'api_key': api_key, 'format': format_}

        if test_mode:
            self.default_params['test_mode'] = test_mode
        self.default_params.update(extra_params)

        self.base_api_url = 'https://api.unisender.com/{lang}/api/'.format(lang=lang)

    def call(self, method, params={}):

        url = self.base_api_url + method
        params.update(self.default_params)
        params = urllib.parse.urlencode(self.http_build_query(params)).encode("utf-8")
        request = urllib.request.Request(url, params, {'User-Agent': 'PyUniSender PY > 3'})

        response = urllib.request.urlopen(request)
        result = json.loads(response.read().decode('utf8'))

        try:
            result = result['result']
            if 'error' in result:
                self.errorMessage = result['error']
                self.errorCode = result['code']
        except TypeError:
            pass  # exception for non-iterable (boolean) types

        return result

    def __getattr__(self, method_name):

        def get(self, *args, **kwargs):
            params = dict(enumerate(args))
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
                name = '%s[%s]' % (key, name)
            if isinstance(val, dict):
                ret.update(self.http_build_query(val, name))
            elif isinstance(val, list):
                ret.update(self.http_build_query(dict(enumerate(val)), name))
            elif val is not None:
                ret[name] = val

        return ret
