
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def LOGIN():

    def code_requested():
        f = open(relative_to_assets("details.txt"), "w")
        username = entry_1.get()
        pwd = entry_2.get()

        if username=="" or pwd=="":
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurun")  

        else:
            f.write(username+"\n")
            f.write(pwd+"\n")
            f.close()
            

    def login_with_code():
        f = open(relative_to_assets("code.txt"), "w")
        code = entry_3.get()

        if code=="":
            messagebox.showerror("Hata", "Lütfen telefonunuza gelen 6 haneli kodu girin")
        else:
            a = open(relative_to_assets("auth.txt"), "w")
            a.write("TRUE")
            a.close()
            window.destroy()
            f.write(code+"\n")
            f.close()

    window = Tk()

    window.geometry("862x519")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 519,
        width = 862,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        190.0,
        0.0,
        526.0,
        519.0,
        fill="#F8F8F8",
        outline="")

    canvas.create_rectangle(
        526.0,
        0.0,
        862.0,
        519.0,
        fill="#F8F8F8",
        outline="")

    canvas.create_rectangle(
        0.0,
        0.0,
        190.0,
        519.0,
        fill="#2A0139",
        outline="")

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        415.0,
        149.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=9.0,
        y=136.0,
        width=89.0,
        height=22.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=9.0,
        y=181.0,
        width=121.0,
        height=22.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    button_3.place(
        x=9.0,
        y=226.0,
        width=122.0,
        height=22.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: code_requested(),
        relief="flat"
    )
    button_4.place(
        x=213.0,
        y=284.0,
        width=284.0,
        height=37.097015380859375
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: login_with_code(),
        relief="flat"
    )
    button_5.place(
        x=305.0,
        y=443.0,
        width=100.0,
        height=37.097015380859375
    )

    canvas.create_text(
        219.0,
        70.0,
        anchor="nw",
        text="Kullanıcı adı",
        fill="#515486",
        font=("RobotoRoman Regular", 14 * -1)
    )

    canvas.create_text(
        218.0,
        165.0,
        anchor="nw",
        text="Şifre",
        fill="#515486",
        font=("RobotoRoman Regular", 14 * -1)
    )

    canvas.create_text(
        218.0,
        338.0,
        anchor="nw",
        text="6 Haneli Kod",
        fill="#515486",
        font=("RobotoRoman Regular", 14 * -1)
    )

    canvas.create_text(
        607.0,
        15.0,
        anchor="nw",
        text="Whatsapp’a Bağlan",
        fill="#000000",
        font=("RobotoRoman Bold", 20 * -1)
    )

    canvas.create_text(
        248.0,
        15.0,
        anchor="nw",
        text="Online Şube’ye Giriş Yap",
        fill="#000000",
        font=("RobotoRoman Bold", 20 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        360.0,
        116.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=223.0,
        y=96.0,
        width=274.0,
        height=39.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        360.0,
        390.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=223.0,
        y=370.0,
        width=274.0,
        height=39.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        360.0,
        211.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_3.place(
        x=223.0,
        y=191.0,
        width=274.0,
        height=39.0
    )
    window.resizable(False, False)
    window.mainloop()



LOGIN()