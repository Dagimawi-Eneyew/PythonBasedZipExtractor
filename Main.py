#importing tkinter module
from tkinter import *
# importing filedialog module
from tkinter import filedialog
#import scrolled text
from tkinter import scrolledtext
import zipfile
import fnmatch
import os
import traceback

#global variable to hold the path
global folder_selected
folder_selected = ''

#Function to extract zip files


def extractZIP(rootPath):
    '''Function to traverse directory and extract zip files
    Parameters: rootPath (String)
    Returns:
    void
    '''
    text_area.configure(state='normal')
    text_area.insert("end", folder_selected)
    try:
        pattern = '*.zip'
        for root, dirs, files in os.walk(rootPath):
            for filename in fnmatch.filter(files, pattern):
                output = os.path.join(root, filename)+'  Extracted...'
                zipfile.ZipFile(os.path.join(root, filename)).extractall(
                    os.path.join(root, os.path.splitext(filename)[0]))
                zipped_file = os.path.join(root, filename)
                os.remove(zipped_file)
                text_area.configure(state='normal')
                text_area.insert("end", output+'\n\n')
                text_area.configure(state='disabled')

    except Exception as e:
        text_area.configure(state='normal')
        text_area.insert(
            "end", "\n------------------------------------------------------------------------------------------------\n")
        text_area.insert(
            "end", "                               Console Log (Error Report)\n")
        text_area.insert(
            "end", "------------------------------------------------------------------------------------------------\n")
        text_area.insert("end", str(traceback.format_exc())+"\n", 'error')
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
    text_area.insert(
        "end", "\n------------------------------------------------------------------------------------------------\n")
    text_area.insert(
        "end", "                               About The Application \n")
    text_area.insert(
        "end", "------------------------------------------------------------------------------------------------\n")
    text_area.insert("end", "ZipExtractor is a free license software originally developed for personal use. \nThis software can extract zip files by traversing each directory.\n Developer : Dagimawi Eneyew \n Verison: 1.0.0 \n")
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
    folder_selected = folder_selected.replace('/', "\\")
    #folder_selected=folder_selected.replace('\\',"\\\\")
    label_file_explorer.configure(text="Folder Selected: "+folder_selected)

#Function to close the application window


def close_window():
    '''Function to close the application window
    Parameters: empty
    Returns:
    void
    '''
    window.destroy()


# Create GUI elements
# Create the root window
window = Tk()

# Set window title
window.title('ZIp File Extractor')

# Set window size
window.geometry("840x500")


text_area = scrolledtext.ScrolledText(window,
                                      width=100,
                                      height=20)

text_area.grid(column=0, pady=10, padx=10)


# Making the text read only
#text_area.configure(state ='disabled')

#Set window background color
window.config(background="indigo")

# Create a File Explorer label
label_file_explorer = Label(window,
                            text="Folder not selected",
                            width=80, height=2,
                            fg="white", background="indigo", font=("Times New Roman",
                                                                   12), anchor='w')
#label to display progress log
progress_Log = Label(window,
                     text="Progress Log...",
                     width=80, height=1,
                     fg="white", font=("Times New Roman",
                                       14), background="indigo", anchor='w')
#A button to open explorer
button_explore = Button(window, width=15,
                        text="Browse Files",
                        command=selectFolder)
#A button to display about info
button_about = Button(window, width=15,
                      text="About", command=messageDisplay)
#A button to initiate extract operation
button_extract = Button(window, width=15, text="Extract Files",
                        command=lambda: extractZIP(folder_selected))

#A button to close the application
button_exit = Button(window,  width=12,
                     text="Exit",
                     command=close_window)


#Window main loop
window.mainloop()
