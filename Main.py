#importing tkinter module
from tkinter import *
# importing filedialog module 
from tkinter import filedialog 
#import scrolled text
from tkinter import scrolledtext
import zipfile,fnmatch,os
import traceback

#global variable to hold the path
global folder_selected
folder_selected=''

#Function to extract zip files
def extractZIP(rootPath):
    '''Function to traverse directory and extract zip files
    Parameters: rootPath (String)
    Returns:
    void
    '''
    text_area.configure(state='normal')
    text_area.insert("end",folder_selected)
    try:
        pattern = '*.zip'
        for root, dirs, files in os.walk(rootPath):
            for filename in fnmatch.filter(files, pattern):
                output=os.path.join(root, filename)+'  Extracted...'
                zipfile.ZipFile(os.path.join(root, filename)).extractall(os.path.join(root, os.path.splitext(filename)[0]))
                zipped_file = os.path.join(root, filename)
                os.remove(zipped_file)
                text_area.configure(state='normal')
                text_area.insert("end",output+'\n\n')
                text_area.configure(state='disabled')
                
    except Exception as e:
        text_area.configure(state='normal')
        text_area.insert("end","\n------------------------------------------------------------------------------------------------\n")
        text_area.insert("end","                               Console Log (Error Report)\n")
        text_area.insert("end","------------------------------------------------------------------------------------------------\n")
        text_area.insert("end",str(traceback.format_exc())+"\n",'error')
        text_area.tag_config('error', foreground='red')
        text_area.configure(state='disabled')
    finally: 
        text_area.yview(END)

#Function to display information about the application
def messageDisplay():
    '''Function to selct folder from file explorer
        Parameters: empty
        Returns:
        void
        '''
    text_area.configure(state='normal')
    text_area.insert("end","\n------------------------------------------------------------------------------------------------\n")
    text_area.insert("end","                               About The Application \n")
    text_area.insert("end","------------------------------------------------------------------------------------------------\n")
    text_area.insert("end","ZipExtractor is a free license software originally developed for personal use. \nThis software can extract zip files by traversing each directory.\n Developer : Dagimawi Eneyew \n Verison: 1.0.0 \n")
    text_area.configure(state='disabled')
    text_area.yview(END)




#function to explore and select folder
def selectFolder(): 
    '''Function to selct folder from file explorer
    Parameters: empty
    Returns:
    void
    '''
    global folder_selected
    folder_selected = filedialog.askdirectory()  
    # Change label contents 
    folder_selected=folder_selected.replace('/',"\\")
    #folder_selected=folder_selected.replace('\\',"\\\\")
    label_file_explorer.configure(text="Folder Selected: "+folder_selected)  

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

#Text are to display the logs
text_area = scrolledtext.ScrolledText(window, width = 80,  height = 20) 

#progress Log title 
progress_Log = Label(window,  text = "Progress Log...", width = 60, height = 4,  fg = "black",font = ("Times New Roman", 
                                              15)) 

#creating the root window
window = Tk() 

# Window title 
window.title('Zip File Extractor') 
   
# Set window size 
window.geometry("700x500") 
   
#Set window background color 
window.config(background = "white") 

#Adjust the location of GUI elements
path_Label.grid(column = 1, row = 1) 
explore_Button.grid(column = 1, row = 2) 
progress_Log.grid(column=1,row=3)
text_area.grid(column=1,row=4)
button_exit.grid(column = 1,row = 8) 

#Make the window unresizable
window.resizable(width=0,height=0)

#Window main loop 
window.mainloop() 
