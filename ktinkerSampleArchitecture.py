import tkinter as tk
import uuid

class Model:
    uuid=[]

class TkView:
    def setup(self, controller):
        #setup Tkinker
        self.root=tk.Tk()
        self.root.geometry("400x400")
        self.root.title("GENUUID")
        
        #create the GUI
        self.frame=tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH,expand=1)
        self.label=tk.Label(self.frame, text="Result:")
        self.label.pack()
        self.list=tk.Listbox(self.frame)
        self.list.pack(fill=tk.BOTH,expand=1)
        self.generate_uuid_button=tk.Button(self.frame, text="Generate UUID", command=controller.handle_click_generate_uuid)
        self.generate_uuid_button.pack()
        self.clear_button=tk.Button(self.frame, text="Clear List", command=controller.handle_click_clear_list)
        self.clear_button.pack()
        
    def insertList(self):
        self.list.insert(tk.END,self.uuid[-1])
        
        
class Controller:
    
    def __init__(self,model,view):
        self.model=model 
        self.view = view
        
    def handle_click_generate_uuid(self):
        self.uuid.append(uuid.uuid4())
        self.list.insert(tk.END,self.uuid[-1])
    
    def handle_click_clear_list(self):
        self.uuid = []
        self.list.delete(0,tk.END)
            
class UUIDGen():
    def __init__(self):
        #setup Tkinker
        self.root=tk.Tk()
        self.root.geometry("400x400")
        self.root.title("GENUUID")
        
        #create the GUI
        self.frame=tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH,expand=1)
        self.label=tk.Label(self.frame, text="Result:")
        self.label.pack()
        self.list=tk.Listbox(self.frame)
        self.list.pack(fill=tk.BOTH,expand=1)
        self.generate_uuid_button=tk.Button(self.frame, text="Generate UUID", command=self.handle_click_generate_uuid)
        self.generate_uuid_button.pack()
        self.clear_button=tk.Button(self.frame, text="Clear List", command=self.handle_click_clear_list)
        self.clear_button.pack()
        
        #initialize the uuid list
        self.uuid=[]
        
        #start the loop
        self.root.mainloop()
        
    def handle_click_generate_uuid(self):
        self.uuid.append(uuid.uuid4())
        self.list.insert(tk.END,self.uuid[-1])
    
    def handle_click_clear_list(self):
        self.uuid = []
        self.list.delete(0,tk.END)
            
# start the application
u=UUIDGen()
        