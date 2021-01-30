#importing tkinter module
from tkinter import *
# importing filedialog module 
from tkinter import filedialog 


#function to explore and select folder
def selectFolder(): 
    '''Function to selct folder from file explorer
    Parameters: empty
    Returns:
    void
    '''
    #open file explorer and grab the path
    folder_selected = filedialog.askdirectory() 
    #Assign the path to text label 
    path_Label.configure(text="Folder Selected: "+folder_selected) 

#Function to close the application window     
def close_window (): 
    '''Function to close the application window
    Parameters: empty
    Returns:
    void
    '''
    window.destroy()   


# Create GUI elements
#label to hold the path string
path_Label = Label(window, text = "Folder not selected !", width = 100, height = 4,  fg = "blue") 
   
#explore window button  
explore_Button = Button(window,  text = "Browse Files", command = browseFiles)  

#application exit button  
exit_Button = Button(window,  text = "Exit", command = close_window)  