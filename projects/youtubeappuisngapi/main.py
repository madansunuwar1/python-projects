import tkinter
import customtkinter
from pytube import YouTube

def startdownload():
    try:
        ytlink=link.get()
        ytObject=YouTube(ytlink, on_progress_callback=on_progress)
        video=ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="white")
        finishlabel.configure(text="")
        video.download()
        finishlabel.configure(text="downloaded!")
    except:
        finishlabel.configure(text="download Error!", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per=str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()
    progressBar.set(float(percentage_of_completion)/100)

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#app
app=customtkinter.CTk()
app.geometry("720x480")
app.title("youtube downloader")

#ui elements
title=customtkinter.CTkLabel(app, text="insert a link")
title.pack(padx=10,pady=10)

#link input
url_var=tkinter.StringVar()
link=customtkinter.CTkEntry(app, width=300,height=40,textvariable=url_var)
link.pack()

finishlabel=customtkinter.CTkLabel(app, text="")
finishlabel.pack()

pPercentage=customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar=customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10,pady=10)

Download=customtkinter.CTkButton(app, text="Download",command=startdownload)
Download.pack(padx=10, pady=10)
#run app
app.mainloop()
