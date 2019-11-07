#Numbers And Assignment

if __name__ == '__main__':
    first_number = 1    #by default, python integers can thought of as immutable values, this means that whatever an integer variable
                        #needs to change, a new value is assigned rather changing what is there.
                        #Consequently, integers will always operate under a 'by value' principle
                        #i.e. copies are always made when transfering values between variables.

    second_number = first_number
    second_number += 1  #here, only second_value is incremented becasue it took a 'copy'
                        #first_value

    print("\nInteger assignment example:")
    print("second_number =", second_number, "first_number =", first_number)

    first_list = [1]
    second_list = first_list    #by default, python lists references
    second_list[0] += 1         #here, both first_list and second_list are incremented because they both reference the same list

    print("\nDefault list assignment example")
    print("second_list =", second_list, "first_list =", first_list)

    first_list[0] = 1
    second_list = first_list[:] #[:] is the python slice operator
                                #it can be used to make sub lists, but crucially it also makes a copy
    second_list[0] += 1         #here, only second_list is incremented because it merely took a copy of first_list

    print("\nSliced (copied) list assignment example")
    print("second_list =", second_list, "first_list =", first_list, "\n")