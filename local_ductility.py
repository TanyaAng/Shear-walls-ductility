from tkinter import *
from math import ceil


def render_main_view():
    Label(tk, text='Storey height [cm]:').grid(column=0, row=0, padx=5, pady=5)
    Hs_cm = Entry(tk)
    Hs_cm.grid(column=1, row=0, padx=5, pady=5)

    Label(tk, text='Initial lenght of head [cm]:').grid(column=0, row=1, padx=5, pady=5)
    lc_cm = Entry(tk)
    lc_cm.grid(column=1, row=1, padx=5, pady=5)

    Label(tk, text='Wall width [cm]:').grid(column=0, row=2, padx=5, pady=5)
    bw_cm = Entry(tk)
    bw_cm.grid(column=1, row=2, padx=5, pady=5)

    Label(tk, text='Wall lenght [cm]:').grid(column=0, row=3, padx=5, pady=5)
    lw_cm = Entry(tk)
    lw_cm.grid(column=1, row=3, padx=5, pady=5)

    Label(tk, text='Ductility class:').grid(column=0, row=4, padx=5, pady=5)
    global_ductility = StringVar()
    radio_button1 = Radiobutton(tk, text='DCM', value='DCM', variable=global_ductility)
    radio_button1.grid(column=1, row=4, padx=5, pady=5)
    radio_button2 = Radiobutton(tk, text='DCH', value='DCH', variable=global_ductility)
    radio_button2.grid(column=2, row=4, padx=5, pady=5)

    Label(tk, text='Behavior factor: ').grid(column=0, row=5, padx=5, pady=5)
    q0 = Entry(tk)
    q0.grid(column=1, row=5, padx=5, pady=5)

    Label(tk, text='fck [MPa]').grid(column=0, row=6, padx=5, pady=5)
    fck = IntVar()
    radio_button3 = Radiobutton(tk, text='C25/30', value=25, variable=fck)
    radio_button3.grid(column=1, row=6, padx=5, pady=5)
    radio_button4 = Radiobutton(tk, text='C30/37', value=30, variable=fck)
    radio_button4.grid(column=2, row=6, padx=5, pady=5)
    radio_button5 = Radiobutton(tk, text='C35/45', value=35, variable=fck)
    radio_button5.grid(column=3, row=6, padx=5, pady=5)

    Label(tk, text='Concrete cover [cm]:').grid(column=0, row=7, padx=5, pady=5)
    concrete_cover = DoubleVar()
    radio_button6 = Radiobutton(tk, text='2.5 cm', value=2.5, variable=concrete_cover)
    radio_button6.grid(column=1, row=7, padx=5, pady=5)
    radio_button7 = Radiobutton(tk, text='3.0 cm', value=3.0, variable=concrete_cover)
    radio_button7.grid(column=2, row=7, padx=5, pady=5)
    radio_button8 = Radiobutton(tk, text='3.5 cm', value=3.5, variable=concrete_cover)
    radio_button8.grid(column=3, row=7, padx=5, pady=5)
    radio_button9 = Radiobutton(tk, text='4.0 cm', value=4.0, variable=concrete_cover)
    radio_button9.grid(column=4, row=7, padx=5, pady=5)

    Label(tk, text='Ned [kN]').grid(column=0, row=8, padx=5, pady=5)
    Ned = Entry(tk)
    Ned.grid(column=1, row=8, padx=5, pady=5)

    Label(tk, text='As1 [mm]').grid(column=0, row=9, padx=5, pady=5)
    As1_diameter = Entry(tk)
    As1_diameter.grid(column=1, row=9, padx=5, pady=5)

    Label(tk, text='Diameter of stirrup [mm]').grid(column=0, row=10, padx=5, pady=5)
    Asw1_diameter = Entry(tk)
    Asw1_diameter.grid(column=1, row=10, padx=5, pady=5)

    Label(tk, text='Lenght of stirrup [cm]: ').grid(column=0, row=11, padx=5, pady=5)
    lenght_stirrup = Entry(tk)
    lenght_stirrup.grid(column=1, row=11, padx=5, pady=5)

    Label(tk, text='Asv,1 [mm] ').grid(column=0, row=12, padx=5, pady=5)
    Asv1 = Entry(tk)
    Asv1.grid(column=1, row=12, padx=5, pady=5)
    Sv=IntVar()
    radio_button10 = Radiobutton(tk, text='/10', value=10, variable=Sv)
    radio_button10.grid(column=2, row=12, padx=5, pady=5)
    radio_button11 = Radiobutton(tk, text='/15', value=15, variable=Sv)
    radio_button11.grid(column=3, row=12, padx=5, pady=5)
    radio_button12 = Radiobutton(tk, text='/20', value=20, variable=Sv)
    radio_button12.grid(column=4, row=12, padx=5, pady=5)

    Button(tk, text='Calculate lc [cm]', bg='green', fg='white',
           command=lambda: calculate_required_lc(float(Hs_cm.get()), float(lc_cm.get()), float(bw_cm.get()),
                                                 float(lw_cm.get()), global_ductility.get(), int(q0.get()),
                                                 float(Ned.get()), float(fck.get()),
                                                 float(concrete_cover.get()),
                                                 int(Asw1_diameter.get()), int(As1_diameter.get()),
                                                 float(lenght_stirrup.get()), int(Asv1.get()),int(Sv.get()))).grid(
        column=0, row=13, padx=5, pady=5)


def calculate_required_lc(Hs_cm, lc_cm, bw_cm, lw_cm, global_ductility, q0, Ned, fck, concrete_cover,
                          Asw1_diameter, As1_diameter, lenght_stirrup, Asv1_diameter, Sv):
    REBARS_DIAMETER = [8, 10, 12, 14, 16, 18, 20, 22, 25, 28, 32]
    REBARS_CM2 = [0.503, 0.785, 1.131, 1.539, 2.011, 2.545, 3.142, 3.801, 4.909, 6.158, 8.042]
    FYK = 500
    index_Asw = REBARS_DIAMETER.index(Asw1_diameter)
    Asw1 = REBARS_CM2[index_Asw]
    index_Asv = REBARS_DIAMETER.index(Asv1_diameter)
    Asv1 = REBARS_CM2[index_Asv]



    fcd = 0.85 * (fck / 10) / 1.50
    Fywd = (FYK / 10) / 1.15
    b0 = bw_cm - 2 * concrete_cover
    h0 = lc_cm - 2 * concrete_cover
    Sw = 10
    # while True:
    #     if lc_cm < max(0.15 * lw_cm, 1.50 * bw_cm):
    #         # print("Current lenght is < 0.15*lw! Choose another lenght of lc [cm]:", end='')
    #         lc_cm = float(input())
    #         continue
    #     if lc_cm <= max(0.2 * lw_cm, 2 * bw_cm):
    #         if bw_cm >= max(Hs_cm / 15, 20):
    #             # print("<<<Bw is appropriate!>>>")
    #             break
    #         else:
    #             # print("Change wall width bw [cm]: ", end='')
    #             bw_cm = float(input())
    #     else:
    #         if bw_cm >= max(Hs_cm / 10, 20):
    #             # print("<<<Bw is appropriate!>>>")
    #             break
    #         else:
    #             # print("Change wall width bw [cm]: ", end='')
    #             bw_cm = float(input())

    Vsw = Asw1 * lenght_stirrup
    Vc = b0 * h0 * Sw

    Wwd = (Vsw / Vc) * (Fywd / fcd)
    if Wwd >= 0.08:
        print(f"{Wwd:.2f} >= 0.08 --> OK")
    else:
        print(f"{Wwd:.2f} < 0.08 --> Choose another parameters!")

    sum_square_bi = calculate_sum_of_squares_bi(lc_cm, bw_cm, lw_cm, bw_cm, concrete_cover, Asw1_diameter, As1_diameter)
    alfa_n = (1 - sum_square_bi / (6 * b0 * h0))
    alfa_s = (1 - Sw / (2 * b0)) * (1 - Sw / (2 * h0))
    alfa = alfa_n * alfa_s
    e_cu2 = 0.0035
    e_cu2c = e_cu2 + 0.1 * alfa * Wwd

    vd = Ned / (lw_cm * bw_cm * fcd)
    # if vd > 0.4:
    #     print("<<<Choose another wall dimensions!>>>")
    # else:
    #     print(f"Vd: {vd:.2f}")

    pv=(2*Asv1)/(Sv*bw_cm)
    Wv = pv * Fywd / fcd
    xu = (vd + Wv) * lw_cm * bw_cm / b0
    lc_req = xu * (1 - (e_cu2 / e_cu2c))
    Label(tk, text=f'Required lc = {lc_req:.2f} cm', bg='#93c47d', fg='black').grid(column=1, row=14, padx=5, pady=5)

    if global_ductility == "DCM":
        Wwd = 0.08
    elif global_ductility == "DCH":
        Wwd = 0.12

    es_d = FYK / (1.15 * 200000)
    m_fi_max = (alfa * Wwd + 0.035) / (30 * (vd + Wv) * es_d * bw_cm / b0)

    Med_to_Mrd = (m_fi_max + 1) / (2 * q0)
    Label(tk, text=f'Required Med/Mrd: {Med_to_Mrd:.2f}',  bg='#93c47d', fg='black').grid(column=1, row=15, padx=5, pady=5)


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


tk = Tk()
tk.geometry('600x600')
tk.title('Local ductility of shear walls')
tk.configure(bg='#fce5cd')
render_main_view()
tk.mainloop()
