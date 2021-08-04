class Example:
    def __init__(self):
        self.a = 1  # public
        self._b = 2  # protected
        self.__c = 3  # private
        print("a= {}, b= {}, c= {}".format(self.a, self._b, self.__c))

    def call(self):
        print("Called!")

    def _call(self):
        print("protected")

    def __call(self):
        print("private")


example = Example()
print(example.a)
print(example._b)

try:
    print(example.__c)
except AttributeError as e:
    print("Error: ", e)

print(dir(example))
print(getattr(example, "_Example__c"))
