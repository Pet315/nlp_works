from Assistant import Assistant


class Customer:
    @staticmethod
    def speech(vars=None, repeat_message=''):
        if vars is None:
            vars = []
        value = input()
        value = str(value)
        value = value.lower()
        while 1:
            for var_i in vars:
                if value == var_i:
                    return value
            Assistant.speech(repeat_message)
            value = input()
            value = str(value)
            value = value.lower()