import random, string

class Test():
    def getAlphaNumeric(self, length, type='letters'):
        """
        Get random string of characters

        Required Parameters:
            length: Length of string, number of characters string should have

        Optional Parameters:
            type: Type of characters string should have. Default is letters
            Provide lower/upper/digits for different types

        Returns:
            None
        """
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))


    def getValidPort(self, count=4):
        """
        Get a valid port number

        Required Parameters:
            None

        Optional Parameters:
            count: Number of digits in a port. Default is 4.

        Returns:
            None
        """
        port = self.getAlphaNumeric(count, 'digits')
        if int(port) > 65535:
            print("65535")
        return self.getAlphaNumeric(count, 'digits')

t = Test()
t.getValidPort(count=6)