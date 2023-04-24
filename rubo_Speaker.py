import win32com.client as wincl
flag=True
while flag:

    x = input("Enter what do you want me to say. ")
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(x)
    flag=input('''Do you want to continue
                Press true is yes
                and false if not  ''').lower()=='true'
