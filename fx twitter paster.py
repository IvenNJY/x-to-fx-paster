import pyperclip
import winreg
import os

# fuction to allow for enable on startup #

# Get the path of the current script
script_path = os.path.realpath(__file__)

# Add the script to the run key in the registry
key = winreg.HKEY_CURRENT_USER
key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"

# Open the key to edit
open = winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS)

# Set value
winreg.SetValueEx(open, "any_name", 0, winreg.REG_SZ, script_path)

# Close the key
winreg.CloseKey(open)


# Main #

# check link whether it is 

def replace_twitter_link(text):

  if "x.com" in text:

    new_text = text.replace("/x.com", "/fxtwitter.com")
    return new_text

  else:
      
    return text

# Replace if the link is correct

while True:

  clipboarded_content = pyperclip.paste()
  modified_content = replace_twitter_link(clipboarded_content)
  
  if modified_content != clipboarded_content:
    pyperclip.copy(modified_content)
    
