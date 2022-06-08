class WP:
    def __init__(self,word=""):
        self.__word=[]
        # self.__word.append("<p>"+word+"</p>")
        self.paragraph(word)
        # print(self.__word)
    
    def getWord(self):
        print( self.__word)
    

    
    def paragraph(self,parag):
        if parag:
            formated_paragrah="<p>"+parag+"</p>"
            self.__word.append(formated_paragrah)
            
        
    def paragraphs(self):
        allpara=""
        for parag in self.__word:
            allpara +=parag
        return allpara
    
    def heading(self,title,head="h1",):
        formated_heading= "<"+head+">"+title+ "<"+head+"/>" 
        self.__word.append(formated_heading)
        
            
            
            

project=WP()
project.heading(title="My Project")
project.paragraph("This is a paragraph")
project.paragraph("This is another paragraph")
project.heading(head="h2", title="Tell the Truth")
project.paragraph("This is another paragraph")

print(project.getWord())
print("*"*40)
print(project.paragraphs())