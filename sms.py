import os,sys,requests,json,time
def clear():
    os.system("clear")
def kata(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./140)
def load():
    for x in range(1,101):
        time.sleep(1./30)
        print(f"\r\033[1;97m[\033[1;96m!\033[1;97m]Loading...(\033[1;92m{x}\033[90m%\033[1;97m)", end="", flush=True)
def balik():
    f=input("\033[1;97m[\033[1;91m?\033[1;97m]Kembali? (y/t): ")
    if f == "y":
       os.system("python sms.py")
    else:
       sys.exit("\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91mExit\033[1;97m")
os.system("print sms gratis|lolcat -a")
os.system("printMR.414N|lolcat -a")
os.system("print  LOVElolcat -a")
os.system("print QUEEN LIA|lolcat -a")
os.system("print Wa=082292838634|lolcat -a")
if __name__=="__main__":
     clear()
     baner()
     try:
          no=input("\033[1;97m[\033[1;92m+\033[1;97m]Phone Number: \033[1;96m")
          msg=input("\033[1;97m[\033[1;92m+\033[1;97m]Message: \033[1;92m")
          dat={
          "number": no,
          "pesan": msg
          }
          load()
          br = requests.post("https://nuubi.herokuapp.com/api/smsgratis", data=dat).text
          if "SMS Gratis Telah Dikirim" in br:
              print(f"\n\033[1;97m[\033[1;92m✓\033[1;97m]Sms To \033[1;96m{no} \033[1;92mSuccess")
          elif "Terjadi kesalahan!" in br:
              kata("\n\033[1;97m[\033[1;91mx\033[1;97m]Terjadi Kesalahan\033[1;91m!!!\033[00m")
          else:
              print(f"\n\033[1;97m[\033[1;91mx\033[1;97m]Sms To \033[1;96m{no} \033[1;91mFailed\033[00m")
     except TypeError:
            print("\033[1;97m\033[1;91m•\033[1;97m]Number Not Valid\033[1;91m!\033[00m")
     except (KeyboardInterrupt,EOFError):
            sys.exit()
     except requests.exceptions.ConnectionError:
            print("\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91mConnection Error\033[00m") 
     balik()
