class InputOutString():
    def __init__(self):
        self.s = ''

    #def set_string(self, str):
     #   self.s = str

    def get_string(self):
        self.s = raw_input("Input:")
        #return self.s

    def print_string(self):
        print(self.s.upper())

o = InputOutString()
# strs = raw_input("Input: ")
o.get_string()
o.print_string()
