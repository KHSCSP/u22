import subprocess
from tkinter.filedialog import asksaveasfilename

# running commands
# subprocess.call("ping localhost")
# subprocess.call("ping www.pltw.org")
# subprocess.call("nslookup www.pltw.org")




# 'save as' dialog
def save_to_file():
    filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
    if filename is None:
        return
    file = open(filename, mode = 'w')
    text_to_save = "hello from me!"
    
    file.write(text_to_save)
    file.close()

# save_to_file()