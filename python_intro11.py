#File IO - csv file

class CsvFile:
    def __init__(self):
        self.fileloaded = False         #flag to indicate whether afile has been loaded
        self.csv = []                   #a list will be used to contain contents of file

    def load(self, filename):
        '''load csv file from current directory'''
        self.fileloaded = False
        try:                                #try/ except used to check to see if file exists
            csvfile = open(filename, "r")
        except IOError:                     #if IOError is raised, file could not be loaded
            print("csv file does not exist!")
            return
        for line in csvfile:                #loop through the lines in the file 
            self.csv.append(list(map(int, line.split(","))))    #and add them to the list
        self.fileloaded = True
        csvfile.close()

    def save(self, filename):
        '''save csv file from current directory'''
        if not self.fileloaded:         #check to see if file has been loaded
            print("Error: no file has been loaded!")
            return
        try:                                #try/ except used to check to see if file exists
            csvfile = open(filename, "w")   # warning: "w" option will overwrite existing file contents
        except IOError:                     #if IOError is raised, file could not be saved
            print("Error: csv file could not be saved!")
            return
        for line in self.csv:               #loop through the lines in the file
            csvfile.write("".join([str(number)+"," for number in line])[:-1]+"\n")
        csvfile.close()

    def display(self):
        if not self.fileloaded:             #check to see if file has been loaded
            print("Error: No file has been loaded!")
            return
        for line in self.csv:               #loop through list to display contents
            print(line)

if __name__ == '__main__':
    csvfile = CsvFile()
    csvfile.load("test.csv")
    csvfile.display()
    csvfile.save("test.csv")