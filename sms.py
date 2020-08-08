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
       sys.exit("\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91mterimakasih telah menggunakan sc ini\033[1;97m")
os.system("clear")
os.system("print MR.414N|figlet -f banner|lolcat -a")
os.system("print LOVE️|figlet -f banner|lolcat -a -i")
os.system("print LIA|figlet -f banner|lolcat -a")

os.system("clear")
os.system("print ====================================|lolcat -a")
os.system("print author=MR.414N|lolcat -a")
os.system("print CINTA KU LIA😙😙😙❤️❤️❤️😙😙😙|lolcat -a")
os.system("print WA=082292838634|lolcat -a")
os.system("print TEAM=CYBER CRIMINAL PUBLIC|lolcat -a")
os.system("print ====================================|lolcat -a")
if __name__=="__main__":
     try:
          no=input("\033[1;98m[\033[1;92m+\033[1;98m] nomor: \033[1;95m")
          msg=input("\033[1;98m[\033[1;92m+\033[1;98m]pesan: \033[1;93m")
          dat={
          "number": no,
          "pesan": msg
          }
          load()
          br = requests.post("https://nuubi.herokuapp.com/api/smsgratis", data=dat).text
          if "SMS Gratis Telah Dikirim" in br:
              print(f"\n\033[1;94m[\033[1;92m✓\033[1;94m]Sms ke \033[1;96m{no} \033[1;92mberhasil")
          elif "Terjadi kesalahan!" in br:
              kata("\n\033[1;94m[\033[1;91mx\033[1;94m]gagal\033[1;91m!!!\033[00m")
          else:
              print(f"\n\033[1;94m[\033[1;91mx\033[1;94m]Sms ke \033[1;96m{no} \033[1;91mFailed\033[00m")
     except TypeError:
            print("\033[1;97m\033[1;91m•\033[1;97m]Nomor tidakValid\033[1;91m!\033[00m")
     except (KeyboardInterrupt,EOFError):
            sys.exit()
     except requests.exceptions.ConnectionError:
            print("\033[1;94m[\033[1;91m!\033[1;94m]\033[1;91mConnection Error\033[00m") 
     balik()
