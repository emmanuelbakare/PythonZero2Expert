class Web:
    def __init__(self, text=""):
        self.text=text
        
    def __str__(self):
        return self.text

class WebBuilder(Web):
    
    def tag(self,text, tag='div'):
        code=f'<{tag}> {text}</{tag}>'
        self.text+=code
        return self

    def cls(self,text):
        return self.tag
        
        
        
html=WebBuilder()
html.tag('This is a text','strong').tag('and another text')

print(html)  