#File IO - Text file

class TxtFile:
    def __init__(self):
        self.fileloaded = False         #flag to indicate whether a file has been loaded
        self.txt = []                   #a list will be used to contain contents of file

    def load(self, filename):
        '''load txt file from current directory'''
        self.fileloaded = False
        try:                                #try/ except used to see if file exists
            txtfile = open(filename, "r")
        except IOError:                     #if IOError is raised, file could not be loaded 
            print("txt file does not exist!")
            return
        for line in txtfile:                #loop through the lines in the file
            self.txt.append(line)           #and add them to the list
        self.fileloaded = True
        txtfile.close()

    def save(self, filename):
        '''save txt file from current directory'''
        if not self.fileloaded:             #check to see if file has been loaded
            print("Error: no file has been loaded!")
            return
        try:                                #try/ except used to check to see if file exists
            txtfile = open(filename, "w")   #warning : "w" option will overwrite existing file contents
        except IOError:                     #if IOError is raised, file could not be loaded 
            print("Error: no file could not be saved!")
            return
        for line in self.txt:               #loop through the lines in the file
            txtfile.write(line)             #could have used writelines without loop
        txtfile.close()

    def display(self):
        if not self.fileloaded:             #check to see if file has been loaded
            print("Error: no file has been loaded!")
            return
        for line in self.txt:               #loop through list to display contents
            print(line, end = "")

if __name__ == '__main__':
    txtfile = TxtFile()
    txtfile.load("test.txt")
    txtfile.display()
    txtfile.save("test.txt")