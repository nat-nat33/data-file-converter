import csv, json #imports needed libraries for conversion

with open('data/bootcamp_data.csv') as f: #python's with statement reads in the csv file and stores to the variable f now I can just call f within this statement
    reader = csv.DictReader(f) #using DictReader and passing in file stored as f, will automatically read top row as field names
    rows = list(reader) #Converts iterable (tuple, string, set, dictionary) to a list. In this case I passed in my file 

with open('data/bootcamp_data.json', 'w') as n: # with statement that writes a file (whatever name I want) to the path I want in my project directory
    json.dump(rows, n) #writes each object in string(json form) tells it where to dump it, in this case my file stored in n
    n.write('/n') #after each row in my list it will create a /n - new line, making it a separate json object