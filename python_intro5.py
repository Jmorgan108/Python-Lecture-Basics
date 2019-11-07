#Strings
if __name__ == '__main__':
    first_string = "ab"     #by default, python strings are also immutable,
                            #which makes direct string manipulation impossible

    second_string = list(first_string)  #one solution to this is to first convert the string into a list
                                        #then change it and then convert it back into a string
                                        #and then since the type of conversion process has to make copies along the way,
                                        #we don't have to worry about the possibility of referencing occuring
    second_string[0] = 'b'
    second_string = "".join(second_string)

    print("\nString assignment example:")
    print("second_string =", second_string, "first_string =", first_string)
