import os, tkinter, shutil, time, sched, sqlite3, datetime
from tkinter import * # Import all sub modules within this module



class ParentWindow(Frame): # I would suggest to place all of this in a class
    
    def __init__(self, master, *args, **kwargs): # Intialize the class object
        Frame.__init__(self, master, *args, **kwargs) # initialize the tkinter frame and associate to the class object
        conn = sqlite3.connect('item66a.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS registro (id INT, t INT)")
        c.execute("SELECT t FROM registro ORDER BY t DESC LIMIT 1")
        lista= tuple(c.fetchall())
        for x in lista:
            traducao = x[0]
    
        #------------(Building GUI)------------- # assign the parent frame's attributes
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text='Última Consulta: '+str(traducao))
        self.msg.pack ()
        

        self.master = master
        self.master.minsize(300,110) # width x height
        self.master.maxsize(300,110) # we can specify min and max to ensure that the user cannot expand window further.
        self.master.title('Transferir Arquivos')
        

        # Define a Tkinter string varible
        self.origintext = StringVar()
        self.destinationtext = StringVar()
        

        # Now set (assign) the default string values
        self.origintext.set('Selecione a pasta de origem')
        self.destinationtext.set('Selecione a pasta de destino')
        #quadro = tkMessageBox.showinfo(c.execute("SELECT t FROM registro ORDER BY t DESC LIMIT 1"))
               
        # Now place the GUI objects within the class object

       
        #Options for buttons
        self.button_opt = {'fill': tkinter.constants.BOTH, 'padx': 5, 'pady': 5}
        #Define asking ORIGIN directory button

        #NOW we assign the string variables we created above inplace of the TEXT. LIKE SO...
        self.originbut= tkinter.Button(self.master, textvariable = self.origintext, fg = 'black', command= self.ChooseOrigin)
        self.originbut.pack()
        #Define asking DESTINATION directory button

        #NOW we assign the string variables we created above inplace of the TEXT. LIKE SO...
        self.destbut = tkinter.Button(self.master, textvariable = self.destinationtext, fg = 'black', command= self.ChooseDestination) # use self. before function to pass self
        self.destbut.pack()
        #Define asking GO directory button
        self.gobut = tkinter.Button(self.master, text = 'Ir', fg = 'black', command= self.do_something)
        self.gobut.pack()

        #Define text showing the last register
        
        

    def ChooseOrigin(self): # requires self as a key to access the class's tkinter objects
        pastafonte = tkinter.filedialog.askdirectory(parent=root,initialdir='/home/',title=self.origintext) 
        self.originbut["text"]= str(pastafonte) if pastafonte else self.origintext
        # we could do something cool like, change the labels to reflect what the user has selected. Like so:
        self.origintext.set(pastafonte)
        

    def ChooseDestination(self):
        pastadestino = tkinter.filedialog.askdirectory(parent=root, initialdir='/home/', title=self.destinationtext) 
        self.destbut["text"] = str(pastadestino) if pastadestino else self.destinationtext
        # we could do something cool like, change the labels to reflect what the user has selected. Like so:
        self.destinationtext.set(pastadestino)


    def do_something(self):
        conn = sqlite3.connect('item66a.db')
        c = conn.cursor()
        c.execute("SELECT t FROM registro ORDER BY t DESC LIMIT 1")
        lista= tuple(c.fetchall())
        for x in lista:
            traducao = x[0]
            formato=datetime.datetime.strptime(traducao,'%Y-%m-%d %H:%M:%S.%f')
            lastmove = time.time() - datetime.timedelta.total_seconds(datetime.datetime.now()-formato)
        # Now we can get (retrieve) the current selected path stored in the corresponding stringvars
            src = self.origintext.get()
            dst = self.destinationtext.get()
            now = datetime.datetime.now()
            for arquivo in os.listdir(src):
                fonte = os.path.join(src, arquivo)
                dest = os.path.join(dst, arquivo)
                if os.path.getmtime(fonte) >= lastmove:
                    current_register=((1,now))
                    shutil.move(fonte, dest)
                    conn = sqlite3.connect('item66a.db')
                    c = conn.cursor()
                    c.execute("INSERT INTO registro VALUES(?,?)",current_register)
                    conn.commit()
                    c.execute("SELECT t FROM registro ORDER BY t DESC LIMIT 1")
                    print(fonte, dest)
                

        #Let's give the user an indication that the process has been completed.
        messagebox.showinfo("Process completed","There are no more qualifying files to check. Try again at a later time.")



if __name__ == '__main__': # Python will check here before it looks at anything else and will run the functions listed in order
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

