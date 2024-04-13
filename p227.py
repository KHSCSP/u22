# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

# before lambda
# def do_command():
#     subprocess.call("ping localhost")


# using lambda
def do_command(command):
    global command_textbox, url_entry
    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"

    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    # use url_val 
    p = subprocess.Popen(command + " " + url_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #v2
    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)


# Save function.
def mSave():
    filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
    if filename is None:
        return
    file = open(filename, mode = 'w')
    text_to_save = command_textbox.get("1.0", tk.END)
    
    file.write(text_to_save)
    file.close()




root = tk.Tk()



# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10)
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ")
url_label.pack(side=tk.LEFT)

url_entry= tk.Entry(frame_URL)
url_entry.pack(side=tk.LEFT)

frame = tk.Frame(root) # change frame color
frame.pack()



# before lambda
# set up button to run the do_command function
# ping_btn = tk.Button(frame, text="ping", command=do_command)
# ping_btn.pack()


# buttons using lambda
# Makes the command button pass it's name to a function using lambda
ping_btn = tk.Button(frame, text="Check to see if a URL is up and active", command=lambda:do_command("ping"))
ping_btn.pack()


# tracert
trace_btn = tk.Button(frame, text="Trace route to website", command=lambda:do_command("tracert"))
trace_btn.pack()

# nslookup
ns_btn = tk.Button(frame, text="nslookup", command=lambda:do_command("nslookup"))
ns_btn.pack()


# save to file
save_btn = tk.Button(frame, text="Save to file", command=mSave)
save_btn.pack()





# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack()


root.mainloop()
