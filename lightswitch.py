from tkinter import Tk, Button
window = Tk()

a= False

def licht():
    global a
    if a == False:
        a = True
        window.configure(bg="yellow")
        button.configure(text='licht uit')
        print('het licht is aan')
    else:
        a = False
        window.configure(bg="black")
        button.configure(text='licht aan')
        print('het licht is uit')

window.configure(bg="black")
button = Button(window, text='licht aan', command=licht)
button.pack(pady = 80, padx = 80)
window.mainloop()