#Char assignment
if __name__ == "__main__":
    first_char = 'a'    #by default, python chars can be thought of as immutable values
                        #this means that whenever a char variable needs to change, a new value is assigned rather than changing
                        #what is there. Consequently, chars will always operate under a 'by value' principle
                        #i.e. copies are always made when transfering values between variables
    second_char = first_char
    second_char = chr(ord(first_char) + 1)  #ord function returns ascii value of char
                                            #chr converts ascii value into char here, only second_value is incremented
                                            #because it 'copied' first_value
    print("\nChar assignment example:")
    print("second_char =", second_char, "first_char =", first_char)

    first_list = ['a']
    second_list = first_list    #by default, python lists are references
    second_list[0] = chr(ord(second_list[0]) + 1)
                                #here, both first_list and second_list are incremented, because they both reference the same list
    print("\nDefault list assignment example")
    print("second_list =", second_list, "first_list =", first_list)

    first_list[0] = 'a'
    second_list = first_list[:] #[:] is the python slice operator that can be used to make sub lists
                                #but, crucially, it also makes a copy
    second_list[0] = chr(ord(second_list[0]) + 1)
                                #here, only second_list is incremented because it merely took a copy of the first_list
    print("\nSliced (copied) list assignment example")
    print("second_list =", second_list, "first_list =", first_list, "\n")