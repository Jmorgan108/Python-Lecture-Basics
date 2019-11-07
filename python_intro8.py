#classes 

class Multiply:
    def __init__(self):  #the name __init__ is reserved and designares the class constructor
        pass

    def __del__(self):   #the name __del__ is reserved and designates the class destructor 
        pass             #we don't need to do anything in the constructor / Destructor 
                         #but all python methods and functions must contain something, so we have included 'pass'
                         #command, which indicates there is nothing to be done
    
    def these_numbers(self, number1, number2):
        return number1 * number2

if __name__ == '__main__':
    multiply = Multiply()

    print(multiply.these_numbers(2,2))