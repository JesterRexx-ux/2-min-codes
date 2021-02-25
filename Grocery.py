"""Grocery calculator """
class grocery:
    def __init__(self,dict,li):
        self.dict=dict
        self.li=li
     

    def print_men(self):
        self.tota=0
        print('Here is your list you choose to buy-->>')
        for i in self.li:
            if i in self.dict:
                self.tota=self.dict[i]*self.li[i]
                print({i:self.tota})
        print('------------')

    def calculate(self):
        self.total=0
        self.total_1=0
        for i in self.li:
            if i in self.dict:
                self.total=self.dict[i]*self.li[i]
                self.total_1+=self.total
            else:
                print(i,'not found , Try another store')
       
 

    def pay(self):
        print('Your total is Rs.',self.total_1)
        print('Here are the options to pay--->>>')
        print('Phonepe')
        print('GPay')
        print('UPi')
                


dic={
            'maggi':25,
            'pizza':90,
            'momos':70,
            'chai':35,
            'samosa':20,
            'bread pakoda':20,
            'paratha':35
        }

def your_list():
    x={}
    print('How many elements you wanna buy??')
    for i in range(int(input('Here: '))):
        gro=input('Grocery: ')
        quan=int(input('Enter quan: '))
        x.update({gro:quan})

    return x

li=your_list()

gro=grocery(dic,li)
gro.print_men()
gro.calculate()
gro.pay()
