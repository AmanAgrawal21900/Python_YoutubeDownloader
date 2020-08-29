"""importing modules"""
from tkinter import *
from tkinter import simpledialog, messagebox
from pytube import YouTube

# Defining Functions
qual = {"1": '144p', "2": '240p', "3": '360p', "4": '480p', "5": '720p', "6": "1080p"}
select = 0
video_link = []
path = ''
quality = ''
fn = ''
link = ''
clean_stream = ''


def show_link():
    global link, fn, quality, clean_stream, path
    link = urlEntry.get()
    video_link.append(link)
    print(link)
    for items in video_link:
        yt = YouTube(items)
        fn = yt.title
        print("\nVideo Title -- ")
        print(fn)
        print("\nVideo Description -- \n")
        print(yt.description)
        print("\nDownload Streams Available -- \n")
        stream = yt.streams.filter(progressive=True, file_extension='mp4')
        for i in stream:
            print(i)
            print(str(i.filesize / (1000000)) + ' MB')


def selection():
    global select, quality, link, clean_stream
    select = v.get()

    for key in qual:
        if int(key) == select:
            quality = qual[str(key)]

    for items in video_link:
        yt = YouTube(items)
        stream = yt.streams
        print("\n\nSELECTED :")
        print(quality)
        clean_stream = stream.filter(progressive=True, file_extension='mp4', resolution=quality)
        print(clean_stream)


# link = urlEntry.get()
# video_link.append(link)
# print(link)


def downLoad():

    path = simpledialog.askstring("Downloader", "Enter a name for your file")
    if path != '':
        clean_stream.first().download('C:\\Users\\Aman Agrawal\\Desktop\\' + path + '.mp4')
    else:
        clean_stream.first().download('C:\\Users\\Aman Agrawal\\Desktop\\' + fn + '.mp4')
    messagebox.showinfo('Downloader', 'Download Successful')
    


# Making Front
"""Making window"""
win = Tk()
win.title('YouTube Video Downloader')
win.geometry('470x270+400+100')
win.config(bg='Red')
win.resizable(0, 0)
v = IntVar()

"""Making Label"""
labelFrame = Frame(master=win)
labelFrame.grid(rowspan=3, columnspan=5)
titleLabel = Label(master=labelFrame, text="YouTube\nDownloader", font=('Arial', 20, 'bold'), fg='white', bg='red')
titleLabel.grid(rowspan=3, columnspan=8, pady=10, padx=10)

"""Taking URL Entry"""
urlFrame = Frame(master=win, bg='red')
urlFrame.grid(row=5, column=4)
urlLabel = Label(master=urlFrame, text='Enter Link (URL) of Video : ', bg='red',
                 fg='white', font=('Arial', 10, 'bold'), anchor=W)
urlLabel.grid(row=3, columnspan=4, padx=10, pady=10)
urlEntry = Entry(master=urlFrame, width=55)
urlEntry.grid(row=4, columnspan=9, padx=15)

"""Bottons"""
radio = {" 144p ": "1", " 240p ": "2", " 360p ": "3", " 480p ": "4", " 720p ": "5", " 1080p ": "6"}
for key, item in radio.items():
    Radiobutton(master=urlFrame, text=key, font=('Arial', 10, 'bold'), value=item,
                variable=v, bg='red', command=selection).grid(row=8, column=radio[key], padx=5, pady=20)

downButton = Button(master=urlFrame, text='Download', fg='white', bg='red', width=10,
                    height=1, relief=RAISED, bd=3, command=downLoad)
downButton.grid(row=9, column=5)
showButton = Button(master=urlFrame, text='Show links', fg='white', bg='red', width=10,
                    height=1, relief=RAISED, bd=3, command=show_link)
showButton.grid(row=9, column=3)

# Making Mainloop()
win.mainloop()
