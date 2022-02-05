'''
pip install tk
'''

import tkinter as tk
from findCEP import searchCEP

class Gui():
    def __init__(self,height,width):
        self.__height = height # The height of the calculator
        self.__width = width # The widht of the calculator
        self.__root = tk.Tk() # Instantiate the library Tkinter


    def createContainers(self):
        # Container for the phrase that says what is to write
        self.__container1 = tk.Frame(self.__root,width=self.__width,highlightbackground="green")
        self.__container1.pack(padx=5,pady=5,anchor="w")

        # Container for the input CEP, and to the search button
        self.__container2 = tk.Frame(self.__root,width=self.__width,highlightbackground="red",bg="#212529")
        self.__container2.pack(padx=8,anchor="w")

    def copyAdressBtn(self): # Function who tells what the widget will do (copy the adress)
        # Just copy the adress to clipboard
        self.__root.clipboard_append(f'{self.__street}, {self.__nbhg}, {self.__town}/{self.__state}, {self.__cep}')

        # Visual alterations on the button, just to tell for the user, that address has been successfully 
        self.__copyBtn['bg'] = "white"
        self.__copyBtn['foreground'] = "#212529"
        self.__copyBtn['text'] = "Copiado ✓"
        self.__copyBtn['state'] = "disabled"
        return

    def search(self): # Function that call the library Pycep, and do the research
        self.__cep = self.__entryData.get() # Just get the data from the entry
        searcher = searchCEP(self.__cep) 
        self.__data = searcher.consulting()

        if not self.__data: # If the CEP is not found, then he don't do anything
            self.__entryData.delete(0,tk.END)
            return
        
        try:
            self.__container3.destroy() # Just clear the container, if have content inside him
            self.__container4.destroy()
            self.__entryData.delete(0,tk.END)
        except:
            pass

        # Container for the adress in the window
        self.__container3 = tk.Frame(self.__root,width=self.__width,highlightbackground="red")
        self.__container3.pack(padx=5,pady=5,anchor="w")

        # Separating in variables the Adress, to put in a label
        self.__street = self.__data['logradouro']
        self.__nbhg = self.__data['bairro'] # Neighborhood from the adress
        self.__town = self.__data['cidade']
        self.__state = self.__data['uf']
        self.__labelAdress = tk.Label(self.__container3,anchor="e",text=f'{self.__street}, {self.__nbhg}, {self.__town}/{self.__state}, {self.__cep}',font=("arial",14),background="#212529",foreground="white")
        self.__labelAdress['wraplength'] = self.__width # Just a word wrap, in case the width is too small for the text
        self.__labelAdress.grid(row=1,column=0)
        self.__entryData.delete(0,tk.END)


        # Container for the button who copy to clipboard
        self.__container4 = tk.Frame(self.__root,width=self.__width,highlightbackground="red",bg="#212529") 
        self.__container4.pack(padx=8,anchor="w")
        self.__copyBtn = tk.Button(self.__container4,text="Copiar para a área de Transferência",command=self.copyAdressBtn,font=('arial',14),bg="#212529",fg="white")
        self.__copyBtn.grid(row=4,column=1)



    def buttonSearch(self): # Create the button to query CEP
        self._searchBtn = tk.Button(self.__container2,text="Buscar",command=self.search,font=('arial',14),bg="#212529",fg="white")
        self._searchBtn.grid(row=0,column=2,padx=5)

    def entryData(self): # Create the input for data
        self.__entryData = tk.Entry(self.__container2,font=('arial',14),fg="white",width=25,bd=5)
        self.__entryData.grid(row=0,column=1,sticky="news")
        self.__entryData.configure({"background": '#212529'})

    def labelEntry(self): # The textbox of the screen
        self.__labelEntry = tk.Label(self.__container1,text="Por favor digite o CEP:",anchor="e",justify="left",font=('arial',14),foreground='white',background="#212529")
        self.__labelEntry.grid(row=0,column=0)

    def startScreen(self): 
        self.__root.title("CEPfinder") 
        self.__root.config(background="#212529") # Background color for the window
        self.__root.resizable(False,False) # Make the windows screen not resizable
        self.__root.geometry(f'{self.__width}x{self.__height}') # Dimensions of the window
        self.createContainers()
        self.labelEntry()
        self.entryData()
        self.buttonSearch()
        self.__root.mainloop() # Run the screen
