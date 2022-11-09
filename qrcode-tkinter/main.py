import qrcode
from tkinter import *
from tkinter import messagebox

wn = Tk()
wn.title('Gerador de QR Code da Massa')
wn.geometry('700x700')
wn.config(bg='lightsteelblue')  # merely changes colors after init

# 3 steps:
# create a label to take the url as text
# locate and also name the QR code for saving
# creates a button that triggers the generateCode() to generate the QR Code

# window label:
heading_frame = Frame(wn, bg='ghostwhite', bd=5)
heading_frame.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.1)  # how much space relatively
heading_label = Label(heading_frame, text='Gerador de QR Code', bg='ghostwhite',
                      font=('Times', 20, 'bold'))
heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

# label for input --- needs to align center with the title
frame_input = Frame(wn, bg='ghostwhite', bd=5)
frame_input.place(relx=0.1, rely=0.15, relwidth=0.7, relheight=0.3)
label_input = Label(frame_input, text='Digite a URL:', fg='black',
                    font=('Times', 16, 'bold'))
label_input.place(relx=0.05, rely=0.2, relheight=0.08)

# just for the place holder
text = Entry(frame_input, font='Century 12')
text.place(relx=0.1, rely=0.35, relwidth=0.7, relheight=0.3)

# input for the location to save the QR
frame_loc = Frame(wn, bg='lightsteelblue')
frame_loc.place(relx=0.1, rely=0.35, relwidth=1, relheight=0.2)

label_loc = Label(frame_loc, text='Onde salvar: ', bg='ghostwhite', fg='black',
                  font=('Times', 16, 'bold'))
loc = Entry(frame_loc, font='Century 12')
loc.place(relx=0.1, rely=0.55, relwidth=0.7, relheight=0.3)

# the size variable for the generateCode() function
frame_size = Frame(wn, bg='lightsteelblue')
frame_size.place(relx=0.1, rely=0.75, relwidth=0.7, relheight=0.2)

label_size = Label(frame_size, text='Tamanho ente 1 e 40 para o QR Code: ',
                   bg='ghostwhite', fg='black', font=('Times', 16, 'bold'))
label_size.place(relx=0.05, rely=0.2, relheight=0.08)
# the name variable for the generateCode() function
# the button to generate

wn.mainloop()


def generateCode():
    qr = qrcode.QRCode(version=size.get(), box_size=10, border=5)
    # size will be passed from the tkinter window
    qr.add_data(text.get())
    qr.make(fit=True)
    img = qr.make_image()  # from PIL
    fileDir = loc.get() + '\\' + name.get()  # if the dir string is passed incorrectly ??
    img.save(f'{fileDir}.png')
    messagebox.showinfo('Código gerado com sucesso no local indicado')
