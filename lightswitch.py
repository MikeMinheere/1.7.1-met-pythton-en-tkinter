from tkinter import Tk, Button
window = Tk()

def licht_aan():
    window.configure(bg="yellow")
    button.configure(text='licht uit', command=licht_uit)
    print('het licht is aan')
def licht_uit():
    window.configure(bg="black")
    button.configure(text='licht aan', command=licht_aan)
    print('het licht is uit')
window.configure(bg="black")
button = Button(window, text='licht aan', command=licht_aan)
button.pack(pady = 80, padx = 80)
window.mainloop()