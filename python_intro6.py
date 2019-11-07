#looping
if __name__ == '__main__':
    number_list = [1,2,3,4,5] #list of numbers
    for number in number_list: #number iterates through number_list
        print(number, end=" ") #end = " " overwrites "\n", so all is printed in one line

    print() #print without any parameters moves the cursor to next line
            #the following code is the same as the above: demonstrates equivelance
    index = 0
    while index < len(number_list):
        print(number_list[index], end= " ")
        index =+ 1
    print()

    #LOOPS 2 OVER AND OVER 