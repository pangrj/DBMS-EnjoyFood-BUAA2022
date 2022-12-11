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
            print(1)
            self.data = dict(self.data, **data)
        print(3)

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
