
class PK:
    """Base PK class"""

    type_pk: str = 'Desktop'

    def __init__(self, processor: str = 'x64', memory: int = 8, preinstalled_os: bool = False):

        self.processor = processor
        self.memory = memory
        self.preinstalled_os = preinstalled_os

    def __repr__(self):
        return 'representation используется для представления объектов класса в виде строки'

    def __call__(self):
        return 'вызывается при обращении к экземпляру как к функции'

    @property
    def t_os(self):
        return self.preinstalled_os

    @t_os.setter
    def t_os(self, value: bool = False):
        self.preinstalled_os = value

    @t_os.deleter
    def t_os(self):
        del self.preinstalled_os

    @classmethod
    def change_type_pk_of_class(cls, value: str = 'Desktop'):
        cls.type_pk = value

    @staticmethod
    def staticmethod_test():
        return 'Это вроде обычной функции, определенной внутри класса, которая не имеет доступа к экземпляру, поэтому ее можно вызывать без создания экземпляра класса'




# init obj
pk1 = PK()

# repr
print(PK())
# call
print(pk1())

# classmethod
print(pk1.type_pk)
pk1.change_type_pk_of_class('Notebook')
print(pk1.type_pk)

# staticmethod
print(PK.staticmethod_test())
print(pk1.staticmethod_test())

# get
print('property - get ', pk1.t_os)
# set
pk1.t_os = True
print('property - set ', pk1.t_os)
# print vars
print(vars(pk1))
# del
del pk1.t_os
print(vars(pk1))
