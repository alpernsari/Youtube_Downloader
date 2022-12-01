from pytube import YouTube
import os

flag = "1"

while(flag == "1"):
    link = str(input("Please enter your link: "))
    yt = YouTube(link)

    answer = input("Video için V/v, Ses için S/s tuşlayınız: ")


    if(answer == 'v' or answer == 'V'):
        try:
            print("Enter the destination (leave blank for current directory)")
            destination = str(input(">> ")) or '.'

            print("download started")
            stream = yt.streams.get_highest_resolution()

            stream.download(output_path=destination)
            
            print(yt.title)
            print("download succesful!")
            
        except:
            print("an error occurred while downloading")
        
    elif(answer == 's' or answer == 'S'):
        try:
            print("Enter the destination (leave blank for current directory)")
            destination = str(input(">> ")) or '.'
  
            print("download started")
            stream = yt.streams.filter(only_audio=True).first()
            
            out_file = stream.download(output_path=destination)
            
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print("download Succesful!")
        except:
            print("İndirme sırasında hata meydana geldi")
    else:
        print("Hatalı tuşlama Yaptınız!")

    try:
        flag = input("Yeni indirme yapmak için 1, bitirmek için herhangi bir karakter tuşlayınız: ")
    except:
        print("hatalı giriş")






