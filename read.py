with open('file1.txt') as file:
    # print(file.read()) 
    linenum=0
    for line in file:
        linenum+=1
        print(linenum, line.strip("\n"))
