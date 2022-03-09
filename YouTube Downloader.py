from pytube import YouTube
from pyfiglet import figlet_format
from termcolor import colored
from os import system

#get link

msg = colored(figlet_format("Youtube Video Downloader", font = 'banner3-D' , ),"green")
print(msg)
url =input(colored("Youtube Video Link::", "yellow"))
try:
    myvideo = YouTube(url)

except:
    print(colored("Somthing Worng","red"))
    system("cls")
    exit(1)

#video title

#download
print(colored("******download*******","green"))
print(colored("[1]Mp3"),"green")
print(colored("[2]Mp4"),"green")
print(colored("**Enter Number**","green"))

choose = int(input(colored("Mp3 or Mp4::","yellow")))
if choose == 1:
    print(colored("Downloading....","green"))
    try:
        myvideo = myvideo.streams.get_audio_only()
        file_path = input("Enter File Path::")
    except:
        print(colored("Something Wrong","red"))
        system("cls")
        exit(1)
    try:
        myvideo.download(file_path)
    except:
        print(colored("Something Wrong!!","red"))
    print(colored("Download Successfull","green"))
if choose == 2:
    print(colored("Downloading....","green"))
    try:
        myvideo = myvideo.streams.get_highest_resolution()
        file_path = input("Enter Your File Path:")
    except:
        print(colored("Something Wrong!!","red"))
        system("cls")
        exit(1)

    if file_path == "":
        file_path =()
    try:
        myvideo.download(file_path)
    except:
        print(colored("Something Wrong!!","red"))
        system("cls")
        exit(1)
    print(colored("Download Successfull","green"))
else:
    print(colored("Wrong Choose","red"))
