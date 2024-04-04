import wandb
import pandas
import os
import tkinter as tk
from tkinter.filedialog import asksaveasfilename

api = wandb.Api()

# Check that the path entered is valid and wandb recognizes it.
def wb_check(thing):
    if "/" not in thing and not thing.startswith("/"):
        print("User input does not appear to be a path in the proper format. Please paste the full path minus quotes from W and B.")
        thing = input("Please enter the run path from W and B here: ")
        safe = 0
    else:
        try:
            api.run(thing)
            safe = 1
        except:
            print("The path provided does not appear to be a valid run path.\nPlease double check on W and B")
            safe = 0
    return safe, thing
 
# Get user input for wandb run name/path.       
safe1 = 0
nrun = input("Please enter the run path from W and B here: ")
while not safe1:
    safe1, nrun = wb_check(nrun)

# Get user input for output save path.
root = tk.Tk()
root.attributes('-alpha', 0.0)
root.attributes('-topmost', True)
save_name = asksaveasfilename(parent=root, initialdir=os.path.realpath(os.path.dirname(__file__)), title="Choose Output Save Path", filetypes=[('Excel Spreadsheet', '*.xlsx')], defaultextension=".xlsx")
root.destroy()
safe2 = 0
while not safe2:
    if save_name == '':
        print("No file specified. Aborting...")
        exit()
    else:
        safe2 = 1

# Do the thing.    
print("Saving to:")
print(save_name)
run = api.run(nrun)
history = run.history(pandas=True)
history.to_excel(save_name)
