with open('myfile1.txt','r') as file:
    codeline=0
    search=""
    while(search!="-x-"):
        search=input("Enter Your Search: ")
        if not len(search):break
        for line in file:
            if len(line) >2: 
                codeline+=1
                if search in line:
                    print("Line No:",codeline)
                    print(line)
        file.seek(0)
        codeline=0 