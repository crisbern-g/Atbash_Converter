from tkinter import *
from tkinter.scrolledtext import *
from atbash import *
from writefile import *
from tkinter import messagebox

if __name__ == '__main__':

    atbash = Atbash()
    root = Tk()
    root.resizable(0, 0)
    root.title('Atbash')


    def convert(*event):
        convertedText.config(state=NORMAL)
        textMessage = Atbash().atbashencrypt(originalEntry.get(0.0, 'end-1c'))
        convertedText.delete(0.0, 'end')
        convertedText.insert(0.0, textMessage)
        convertedText.config(state=DISABLED)


    def savetext(*event):
        messagebox.showinfo('Success', 'Encrypted text is saved in ' + getfilepath() + '.txt')
        write_encryption(convertedText.get(0.0, 'end'))


    def atbashInfo(event):
        with open('text files\\about atbash', 'r') as about:
            atbashInfo = about.read()
        messagebox.showinfo('About Atbash', atbashInfo)


    def switchtext(*event):
        convertedText.config(state=NORMAL)
        text = convertedText.get(0.0, 'end-1c')
        originalEntry.delete(0.0, 'end')
        originalEntry.insert(0.0, text)
        convertedText.delete(0.0, 'end')
        convert()
        convertedText.config(state=DISABLED)


    mainLabel = Label(root, text="Atbash", fg='blue', cursor='hand2')
    mainLabel.config(font=('impact', 20))
    mainLabel.bind('<Button-1>', atbashInfo)
    mainLabel.grid(row=0, columnspan=2)

    originalLabel = Label(root, text='Original', fg='green')
    originalLabel.config(font=('impact', 20))
    originalLabel.grid(row=2, column=0)

    encryptedLabel = Label(root, text='Encrypted', fg='red', border=3)
    encryptedLabel.config(font=('impact', 20))
    encryptedLabel.grid(row=2, column=1)

    originalEntry = ScrolledText(root, wrap=WORD, border=3)
    originalEntry.config(height=10, width=35)
    originalEntry.grid(row=1, column=0)
    originalEntry.bind('<Key>', convert)
    originalEntry.bind('<KeyRelease>', convert)

    convertedText = ScrolledText(root, wrap=WORD, fg='SpringGreen2', bg='gray20', border=3)
    convertedText.config(state=DISABLED)
    convertedText.config(height=10, width=35)
    convertedText.grid(row=1, column=1)

    saveButton = Button(root, text='SAVE', bg='yellow', fg='black', command=savetext, cursor='hand2')
    saveButton.config(font=('cooper', 15))
    saveButton.config(height=1, width=10)
    saveButton.grid(row=3, column=0, sticky=E)

    switchButton = Button(root, text='SWITCH', bg='blue', fg='black', command=switchtext, cursor='hand2')
    switchButton.config(font=('cooper', 15))
    switchButton.config(height=1, width=10)
    switchButton.grid(row=3, column=1, sticky=W)

    root.mainloop()
