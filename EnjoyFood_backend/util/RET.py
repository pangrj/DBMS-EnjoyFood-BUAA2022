import re


class RET:
    def __init__(self, code, message):
        self.code = code
        self.message = message
        self.data = {}

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

    def get_message(self):
        return self.message

    def set_message(self, message):
        self.message = message

    def get_data(self):
        return self.data

    def load_data(self, data):
        if type(data) == dict:
            self.data = dict(self.data, **data)

    def json_type(self):
        ret = {
            'code': self.code,
            'message': self.message
        }
        ret = dict(ret, **self.data)
        return ret

    def Http_error(self):
        self.code = -1
        self.message = 'HTTP Method Error!'


def get_instance():
    return RET(-1, 'Have not initial the ret message')


def get_time(time):
    print(time)
    matchObj = re.match('(\d+)-(\d+)-(\d+)\D(\d+):(\d+):(\d+).*', time, re.M | re.I)
    ret_time = "{}-{} {}:{}".format(matchObj.group(2), matchObj.group(3), matchObj.group(4), matchObj.group(5))
    print('1111              ', ret_time)
    return ret_time
