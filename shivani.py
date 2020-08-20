import pyttsx3
import os
pyttsx3.speak("Welcome to Virtual Assistant")
print("                                    @@@###########################@@@")
print("                                    @  Welcome To Virtual Assistant @")
print("                                    @@@###########################@@@")
print("                           ___________________________________________________")

pyttsx3.speak(" I worked only for these things like -\n Goggle chrome")
print("1. Goggle Chrome")
pyttsx3.speak(" \nNotepad")
print("2. Editor")
pyttsx3.speak(" \nCamera")
print("3. Camera")
pyttsx3.speak(" \nSystem Information")
print("4. System Information")
pyttsx3.speak(" \nCommand Prompt")
print("5. Command Prompt")
pyttsx3.speak(" \nTeamviewer")
print("6. Teamviewer")
pyttsx3.speak(" \nXampp server")
print("7. Xampp server")
pyttsx3.speak(" \nmicrosoftedge")
print("8. MicrosoftEdge")
pyttsx3.speak(" \nvlc media player")
print("9. Vlc Media Player")
pyttsx3.speak(" \ngitbash")
print("10. Git Bash")
pyttsx3.speak(" \nandroidstudio")
print("11. AndroidStudio")
pyttsx3.speak(" \nwmplayer")
print("12. Wmplayer")
pyttsx3.speak(" \npaint")
print("13. Paint")

while True:
       pyttsx3.speak("What can i do for you:")
       
       print("what can i do for you:")
       p=input()
       if ((("start" in p or "run" in p) or ("execute" in p or "please" in p) or ("can" in p or "open" in p)) and (("chrome" in p or "Chrome" in p) or "browser"in p)):
          pyttsx3.speak("yes....i will")
          os.system("chrome")
          
       elif ((("run" in p or "start" in p) or ("execute" in p or "please" in p) or ("can" in p or "open" in p)) and (("notepad" in p or "Notepad"in p) or "editor" in p)):
          pyttsx3.speak("you can start writting")
          os.system("notepad")

       elif ((("start" in p or "open" in p) or ("can" in p or "run" in p)) and ("camera" in p or "Camera" in p)):
          pyttsx3.speak("Enjoy Capturing")
          os.system("start microsoft.windows.camera:")

       elif ((("give" in p or "Give" in p) or ("Show" in p or "show" in p)) and ("system information" in p or "sysinfo" in p)):
          pyttsx3.speak("this is all about your system")
          os.system("msinfo32")
 
       elif ((("start" in p or "run" in p) or ("execute" in p or "please" in p) or ("can" in p or "open" in p)) and (("Command Prompt" in p or "cmd" in p) or "command prompt" in p)):
          os.system("start cmd")
       
       elif ((("start" in p or "run" in p) or ("execute" in p or "please" in p) or ("can" in p or "open" in p)) and ("Teamviewer" in p or "teamviewer" in p)):
          os.system("TeamViewer")

       elif ((("start" in p or "run" in p) or ("execute" in p or "please" in p) or ("can" in p or "open" in p)) and ("xampp" in p or "Xampp" in p)):
          os.system("ampp-control")     #xampp name is renamed by ampp because '\x' creates an unicode error thats why it changed

       elif ((("start" in p or "run" in p) or ("execute" in p or "please" in p) or ("can" in p or "open" in p)) and (("MicrosoftEdge" in p or "microsoftedge" in p) or ("edge" in p or "msedge" in p))):
          os.system("start microsoftedge")

       elif ((("start" in p or "run" in p) or ("execute" in p or "please" in p) or ("can" in p or "open" in p)) and ("vlc" in p or "Vlc" in p)):
           os.system("vlc")

       elif ((("start" in p or "run" in p) or ("execute" in p or "please" in p) or ("can" in p or "open" in p)) and ("gitbash" in p or "Gitbash" in p)):
           os.system("git-bash")

       elif ((("start" in p or "run" in p) or ("execute" in p or "please" in p) or ("can" in p or "open" in p)) and (("android" in p or "Android" in p) or ("androidstudio" in p or "Androidstudio" in p))):
           os.system("studio64")

       elif ((("start" in p or "run" in p) or ("execute" in p or "please" in p) or ("can" in p or "open" in p)) and (("wmplayer" in p or "Wmplayer" in p) or "WMplayer" in p)):
           os.system("wmplayer")

       elif ((("start" in p or "run" in p) or ("execute" in p or "please" in p) or ("can" in p or "open" in p)) and ("paint" in p or "Paint" in p)):
           os.system("mspaint")

       elif (("exit" in p or "quit" in p) or ("stop" in p or "nothing" in p)):
          pyttsx3.speak("Thanks for using me....\nhope you like it \nhave a nice day")
          print("Have a nice day")
          break
       else:
          print("Its invalid....Please write in some Valid way.....")