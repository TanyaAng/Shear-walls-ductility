from tkinter import *
from math import ceil
from PIL import ImageTk, Image
import json


def clear_view():
    for slave in tk.grid_slaves():
        slave.destroy()


MAIN_COLOUR = '#fce5cd'
MAIN_FONT = 'ArialNarrow 10 bold'


class Ductility:
    def __init__(self):
        clear_view()

        Label(tk, text='Storey Height', bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=0, padx=5,
                                                                             pady=5)
        self.Hs = Entry(tk)
        self.Hs.grid(column=1, row=0, padx=5, pady=5)

        Label(tk, text='Initial Lenght of Lc [cm]', bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=1, padx=5,
                                                                                         pady=5)
        self.lc_cm = Entry(tk)
        self.lc_cm.grid(column=1, row=1, padx=5, pady=5)

        Label(tk, text='Wall Width [cm]', bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=2, padx=5, pady=5)
        self.bw_cm = Entry(tk)
        self.bw_cm.grid(column=1, row=2, padx=5, pady=5)

        Label(tk, text='Wall Lenght [cm]', bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=3, padx=5, pady=5)
        self.lw_cm = Entry(tk)
        self.lw_cm.grid(column=1, row=3, padx=5, pady=5)

        Label(tk, text='Ductility Class', bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=4, padx=5, pady=5)
        self.global_ductility = StringVar()
        radio_button1 = Radiobutton(tk, text='DCM', value='DCM', variable=self.global_ductility, bg='#fce5cd')
        radio_button1.grid(column=1, row=4, padx=5, pady=5)
        radio_button2 = Radiobutton(tk, text='DCH', value='DCH', variable=self.global_ductility, bg='#fce5cd')
        radio_button2.grid(column=2, row=4, padx=5, pady=5)

        Label(tk, text="Comparison Between T1 and Tc", bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=5, padx=5,
                                                                                            pady=5)
        self.is_bigger_T1 = BooleanVar()
        radio_button33 = Radiobutton(tk, text='T1>=Tc', value=True, variable=self.is_bigger_T1, bg='#fce5cd')
        radio_button33.grid(column=1, row=5, padx=5, pady=5)
        radio_button44 = Radiobutton(tk, text='T1<Tc', value=False, variable=self.is_bigger_T1, bg='#fce5cd')
        radio_button44.grid(column=2, row=5, padx=5, pady=5)

        Label(tk, text='Behavior Factor q0', bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=6, padx=5, pady=5)
        self.q0 = Entry(tk)
        self.q0.grid(column=1, row=6, padx=5, pady=5)

        Label(tk, text='Concrete Class', bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=7, padx=5, pady=5)
        self.fck = IntVar()
        radio_button3 = Radiobutton(tk, text='C25/30', value=25, variable=self.fck, bg='#fce5cd')
        radio_button3.grid(column=1, row=7, padx=5, pady=5)
        radio_button4 = Radiobutton(tk, text='C30/37', value=30, variable=self.fck, bg='#fce5cd')
        radio_button4.grid(column=2, row=7, padx=5, pady=5)
        radio_button5 = Radiobutton(tk, text='C35/45', value=35, variable=self.fck, bg='#fce5cd')
        radio_button5.grid(column=3, row=7, padx=5, pady=5)

        Label(tk, text='Concrete Cover [cm]', bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=8, padx=5, pady=5)
        self.concrete_cover = DoubleVar()
        radio_button6 = Radiobutton(tk, text='2.5 cm', value=2.5, variable=self.concrete_cover, bg='#fce5cd')
        radio_button6.grid(column=1, row=8, padx=5, pady=5)
        radio_button7 = Radiobutton(tk, text='3.0 cm', value=3.0, variable=self.concrete_cover, bg='#fce5cd')
        radio_button7.grid(column=2, row=8, padx=5, pady=5)
        radio_button8 = Radiobutton(tk, text='3.5 cm', value=3.5, variable=self.concrete_cover, bg='#fce5cd')
        radio_button8.grid(column=3, row=8, padx=5, pady=5)
        radio_button9 = Radiobutton(tk, text='4.0 cm', value=4.0, variable=self.concrete_cover, bg='#fce5cd')
        radio_button9.grid(column=4, row=8, padx=5, pady=5)

        Label(tk, text='Ned [kN]', bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=9, padx=5, pady=5)
        self.Ned = Entry(tk)
        self.Ned.grid(column=1, row=9, padx=5, pady=5)

        Label(tk, text='As1 [mm]', bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=10, padx=5, pady=5)
        self.As1_diameter = Entry(tk)
        self.As1_diameter.grid(column=1, row=10, padx=5, pady=5)

        Label(tk, text='Asw1 [mm]', bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=11, padx=5, pady=5)
        self.Asw1_diameter = Entry(tk)
        self.Asw1_diameter.grid(column=1, row=11, padx=5, pady=5)

        # Label(tk, text='Lenght of Stirrup [cm]: ', bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=12, padx=5, pady=5)
        # lenght_stirrup = choose_stirrup()
        # Label(tk, text={lenght_stirrup}).grid(column=1, row=12, padx=5, pady=5)
        # # lenght_stirrup.grid(column=1, row=12, padx=5, pady=5)

        Label(tk, text='Asv,1 [mm] ', bg=MAIN_COLOUR, font=MAIN_FONT).grid(column=0, row=13, padx=5, pady=5)
        self.Asv1 = Entry(tk)
        self.Asv1.grid(column=1, row=13, padx=5, pady=5)

        self.Sv = IntVar()
        radio_button10 = Radiobutton(tk, text='/10', value=10, variable=self.Sv, bg=MAIN_COLOUR)
        radio_button10.grid(column=2, row=13, padx=5, pady=5)
        radio_button11 = Radiobutton(tk, text='/15', value=15, variable=self.Sv, bg=MAIN_COLOUR)
        radio_button11.grid(column=3, row=13, padx=5, pady=5)
        radio_button12 = Radiobutton(tk, text='/20', value=20, variable=self.Sv, bg=MAIN_COLOUR)
        radio_button12.grid(column=4, row=13, padx=5, pady=5)

        # lenght_stirrup = choose_stirrup()

        Button(tk, text='Calculate Lc [cm]', bg='green', fg='white', font=MAIN_FONT,
               command=lambda: calculate_required_lc(float(self.Hs.get()), float(self.lc_cm.get()),
                                                     float(self.bw_cm.get()),
                                                     float(self.lw_cm.get()), self.global_ductility.get(),
                                                     int(self.q0.get()),
                                                     float(self.Ned.get()), float(self.fck.get()),
                                                     float(self.concrete_cover.get()),
                                                     int(self.Asw1_diameter.get()), int(self.As1_diameter.get()),
                                                     int(self.Asv1.get()),
                                                     int(self.Sv.get()), self.is_bigger_T1.get())).grid(column=0,
                                                                                                        row=15, padx=5,
                                                                                                        pady=5)

        Button(tk, text="Stirrup distibution", command=choose_stirrup).grid(column=0, row=14, padx=5,
                                                                            pady=5)


def get_value_lenght_stirrup():
    stirrup = []
    stirrup.append(button_value.get())
    with open('database.txt', 'w') as file:
        json.dump(stirrup, file)


def choose_stirrup():
    clear_view()
    global head_40_60_img
    global button_value
    button_value = IntVar()
    # img = Image.open('D:\SOFTUNI\Local Ductility Of Shear Walls\head40x60.png')
    # img_2 = img.resize(100, 100)
    head_40_60_img = ImageTk.PhotoImage(Image.open('D:\SOFTUNI\Local Ductility Of Shear Walls\head40x60.png'))
    # new_img=PhotoImage(file=r"D:\SOFTUNI\Local Ductility Of Shear Walls\head40x60.gif")
    Radiobutton(tk, image=head_40_60_img, value=445, variable=button_value, command=get_value_lenght_stirrup).grid(
        column=0, row=0)
    Radiobutton(tk, text='500', value=500, variable=button_value, command=get_value_lenght_stirrup).grid(column=1,
                                                                                                         row=0)
    Radiobutton(tk, text='600', value=600, variable=button_value, command=get_value_lenght_stirrup).grid(column=2,
                                                                                                         row=0)
    Radiobutton(tk, text='700', value=700, variable=button_value, command=get_value_lenght_stirrup).grid(column=3,
                                                                                                         row=0)
    Button(tk, text="Go Back", command=lambda : Ductility.__init__(self=main_view)).grid(column=0, row=1, padx=5, pady=5)


def calculate_required_lc(Hs_cm, lc_cm, bw_cm, lw_cm, global_ductility, q0, Ned, fck, concrete_cover,
                          Asw1_diameter, As1_diameter, Asv1_diameter, Sv, is_bigger_T1):
    try:
        with open('database.txt', 'r') as file:
            database = json.load(file)
            lenght_stirrup = database[0]
    except:
        Label(tk, text="Choose stirrup distribution").grid(column=1, row=14, padx=5, pady=5)

    REBARS = {8: 0.503, 10: 0.785, 12: 1.131, 14: 1.539, 16: 2.011, 18: 2.545, 20: 3.142, 22: 3.801, 25: 4.909,
              28: 6.158, 32: 8.042}
    FYK = 500
    Asw1 = REBARS[Asw1_diameter]
    Asv1 = REBARS[Asv1_diameter]

    fcd = 0.85 * (fck / 10) / 1.50
    Fywd = (FYK / 10) / 1.15
    b0 = bw_cm - 2 * concrete_cover
    h0 = lc_cm - 2 * concrete_cover
    Sw = 10
    if lc_cm < max(0.15 * lw_cm, 1.50 * bw_cm):
        Label(tk, text=f"NO", bg='#CC3333', fg='white').grid(column=2, row=1, padx=5,
                                                             pady=5)
    else:
        Label(tk, text="OK", bg='#93c47d', fg='black').grid(column=2, row=1, padx=5, pady=5)

    if lc_cm <= max(0.2 * lw_cm, 2 * bw_cm):
        if bw_cm >= max(Hs_cm / 15, 20):
            Label(tk, text="OK", bg='#93c47d', fg='black').grid(column=2, row=2, padx=5, pady=5)
        else:
            Label(tk, text=f"NO", bg='#CC3333', fg='white').grid(column=2, row=2, padx=5, pady=5)
    else:
        if bw_cm >= max(Hs_cm / 10, 20):
            Label(tk, text="OK", bg='#93c47d', fg='black').grid(column=2, row=2, padx=5, pady=5)
        else:
            Label(tk, text=f"NO", bg='#CC3333', fg='white').grid(column=2, row=2, padx=5, pady=5)

    Vsw = Asw1 * lenght_stirrup
    Vc = b0 * h0 * Sw

    Wwd = (Vsw / Vc) * (Fywd / fcd)
    if Wwd >= 0.08:
        Label(tk, text=f"{Wwd:.2f} >= 0.08 --> OK", bg='#93c47d', fg='black').grid(column=2, row=12, padx=5,
                                                                                   pady=5)
    else:
        Label(tk, text=f"{Wwd:.2f}  < 0.08 --> NO", bg='#CC3333', fg='white').grid(column=2, row=12, padx=5, pady=5)

    sum_square_bi = calculate_sum_of_squares_bi(lc_cm, bw_cm, lw_cm, bw_cm, concrete_cover, Asw1_diameter, As1_diameter)
    alfa_n = (1 - sum_square_bi / (6 * b0 * h0))
    alfa_s = (1 - Sw / (2 * b0)) * (1 - Sw / (2 * h0))
    alfa = alfa_n * alfa_s
    e_cu2 = 0.0035
    e_cu2c = e_cu2 + 0.1 * alfa * Wwd

    vd = Ned / (lw_cm * bw_cm * fcd)
    if vd > 0.4:
        Label(tk, text=f"NO", bg='#CC3333', fg='white').grid(column=2, row=9, padx=5, pady=5)
    else:
        Label(tk, text=f"OK", bg='#93c47d', fg='black').grid(column=2, row=9, padx=5, pady=5)

    pv = (2 * Asv1) / (Sv * bw_cm)
    Wv = pv * Fywd / fcd
    xu = (vd + Wv) * lw_cm * bw_cm / b0
    lc_req = xu * (1 - (e_cu2 / e_cu2c))
    Label(tk, text=f'Required Lc = {lc_req:.2f} cm', bg='#93c47d', fg='black').grid(column=1, row=14, padx=5, pady=5)

    if global_ductility == "DCM":
        Wwd = 0.08
    elif global_ductility == "DCH":
        Wwd = 0.12

    es_d = FYK / (1.15 * 200000)
    m_fi_max = (alfa * Wwd + 0.035) / (30 * (vd + Wv) * es_d * bw_cm / b0)

    if is_bigger_T1:
        Med_to_Mrd = (m_fi_max + 1) / (2 * q0)
    else:
        Med_to_Mrd = (m_fi_max + 1) / (2 * q0)
    Label(tk, text=f'Required Med/Mrd: {Med_to_Mrd:.2f}', bg='#93c47d', fg='black').grid(column=1, row=15, padx=5,
                                                                                         pady=5)


def calculate_sum_of_squares_bi(lc_cm, bw_cm, height, width, concrete_cover, Asw1_diameter, As1_diameter):
    number_rebars_long_side = 0
    number_rebars_short_side = 0
    sum_square_bi_long_side = 0
    sum_square_bi_short_side = 0
    if height == 10:
        number_rebars_long_side += 2
    elif height > 10:
        number_rebars_long_side += ceil((height - 5) / 15 + 1) * 2
    if width > 25:
        number_rebars_short_side += ceil((width - 5) / 15 - 1) * 2

    if number_rebars_long_side > 2:
        bi_spaces_long_side = int((number_rebars_long_side / 2 - 1) * 2)
        bi_long_side = (lc_cm - 2 * concrete_cover - 2 * Asw1_diameter / 10 - As1_diameter / 10) / (
                bi_spaces_long_side / 2)
        sum_square_bi_long_side = bi_spaces_long_side * bi_long_side ** 2

    if number_rebars_short_side > 0:
        bi_spaces_short_side = int(number_rebars_short_side / 2 + 1) * 2
        bi_short_side = (bw_cm - 2 * concrete_cover - 2 * Asw1_diameter / 10 - As1_diameter / 10) / (
                bi_spaces_short_side / 2)
        sum_square_bi_short_side = bi_spaces_short_side * bi_short_side ** 2
    else:
        bi_short_side = (bw_cm - 2 * concrete_cover - 2 * Asw1_diameter / 10 - As1_diameter / 10)
        sum_square_bi_short_side = 2 * bi_short_side ** 2

    return sum_square_bi_short_side + sum_square_bi_long_side


if __name__ == "__main__":
    tk = Tk()
    tk.geometry('650x550')
    tk.title('LOCAL DUCTILITY OF SHEAR WALLS')
    tk.configure(bg='#fce5cd')
    main_view = Ductility()
    main_view.__init__()
    tk.mainloop()
