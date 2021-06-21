from tkinter import *
import webbrowser

def test():
    webbrowser.open_new("https://github.com/Python564/Test")
#creer une preimiere fenetre
windows = Tk()

#personalisez la fentre
windows.title("Mon application")
windows.geometry("720x480")
windows.minsize(480, 360)
windows.iconbitmap("icon.ico")
windows.config(background='#41B77F')

#creer la frame
frame1 = Frame(windows, bg='#41B77F')

#ajouter un premier texte
firsttext = Label(frame1, text="Les Programes crées", font=("Courrier", 40), bg='#41B77F', fg='white')
firsttext.pack()

#ajouter un second texte
firstsubtitle = Label(frame1, text="Clique sur le bouton.", font=("Courrier", 25), bg='#41B77F', fg='white')
firstsubtitle.pack()

#ajouter un boutton
yt_boutton = Button(frame1, text="Clique !", font=("Courrier", 25), bg='white', fg='#41B77F', command=test)
yt_boutton.pack(pady=25, fill=X)

#afficher la frame
frame1.pack(expand=YES)

#afficher la fenetre
windows.mainloop()
