class RET:
    def __init__(self, code, message):
        self.code = code
        self.message = message
        self.data = {}

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
