from pyswip import Prolog
import customtkinter as ctk
import re
import itertools

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.geometry("750x520")

prolog = Prolog()
prolog.consult("reguli.pl")

vocale = "aăâeiîou"
consoane = "bcdfghjklmnpqrsștțvwxyz"

fisier = "Dictionar.txt"


def regula3(cuvant):
    cuvant_despartit = cuvant[0]
    exceptii = ["lpt", "mpt", "nct", "ndv", "ncs", "rct", "rtf", "stm"]
    i = 1
    while i < len(cuvant) - 1:
        if (i + 2 < len(cuvant)) and (cuvant[i] + cuvant[i + 1] + cuvant[i + 2] in exceptii) and cuvant[i - 1] in vocale and cuvant[i + 3] in vocale:
            cuvant_despartit += cuvant[i] + cuvant[i + 1] + '-' + cuvant[i + 2]
            i += 3
        elif (i + 2 < len(cuvant)) and cuvant[i] in consoane and cuvant[i + 1] in consoane and cuvant[
            i + 2] in consoane and cuvant[i - 1] in vocale and cuvant[i + 3] in vocale and (cuvant[i+1] not in 'cg' and cuvant[i+2] != 'h'):
            cuvant_despartit += cuvant[i] + '-' + cuvant[i + 1] + cuvant[i + 2]
            i += 3
        elif (i + 3 < len(cuvant)) and cuvant[i] in consoane and cuvant[i + 1] in consoane and cuvant[
            i + 2] in consoane and cuvant[i + 3] in consoane and cuvant[i - 1] in vocale and cuvant[i + 4] in vocale:
            cuvant_despartit += cuvant[i] + '-' + cuvant[i + 1] + cuvant[i + 2] + cuvant[i + 3]
            i += 4
        else:
            cuvant_despartit += cuvant[i]
            i += 1
    cuvant_despartit += cuvant[-1]  # Adăugăm ultima literă a cuvântului în rezultat

    return cuvant_despartit


def is_semivocala(cuvant, pozitie):
    if cuvant[pozitie] == 'e' and (cuvant[pozitie-1] in 'ao' or cuvant[pozitie+1] in 'ao'):
        return True
    elif cuvant[pozitie] == 'i' and (cuvant[pozitie-1] in 'aăâeîou' or cuvant[pozitie+1] in 'aăâeîou'):
        return True
    elif cuvant[pozitie] == 'o' and (cuvant[pozitie+1] == "a"):
        return True
    elif cuvant[pozitie] == 'u' and (cuvant[pozitie-1] in 'aăâeîou' or cuvant[pozitie+1] in 'aăâeîu'):
        return True
    return False


def regula4(cuvant):
    exceptie = ["fii-că", "fii-ca"]
    if cuvant == exceptie[0] or cuvant == exceptie[1]:
        return cuvant
    else:
        cuvant_despartit = ''
        i = 0
        while i < len(cuvant):
            if i + 2 < len(cuvant) and cuvant[i] in vocale and cuvant[i + 2] == cuvant[i + 1] == cuvant[i]:
                cuvant_despartit += cuvant[i] + '-' + cuvant[i + 1] + cuvant[i + 2]
                i += 3
            elif i + 1 < len(cuvant) and cuvant[i] in vocale and cuvant[i + 1] == cuvant[i] and i+1 != len(cuvant)-1:
                cuvant_despartit += cuvant[i] + '-' + cuvant[i + 1]
                i += 2
            elif i+1 <len(cuvant) and cuvant[i] in vocale and cuvant[i + 1] in vocale and not is_semivocala(cuvant,i) and not is_semivocala(cuvant,i+1):
                cuvant_despartit += cuvant[i] + '-' + cuvant[i + 1]
                i+=2
            elif i+2 <len(cuvant) and cuvant[i] in vocale and cuvant[i + 1] in vocale and cuvant[i + 2] in vocale and \
                    not is_semivocala(cuvant, i) and is_semivocala(cuvant, i+1) and not is_semivocala(cuvant, i+2):
                cuvant_despartit += cuvant[i] + '-' + cuvant[i + 1] + cuvant[i + 2]
                i+=3
            elif i+4 <len(cuvant) and cuvant[i] in vocale and cuvant[i + 1] in vocale and cuvant[i + 2] in vocale and cuvant[i + 3] in vocale and \
                    not is_semivocala(cuvant, i) and is_semivocala(cuvant, i+1) and is_semivocala(cuvant, i+2) and not is_semivocala(cuvant, i+3):
                cuvant_despartit += cuvant[i] + '-' + cuvant[i + 1] + cuvant[i + 2] + cuvant[i + 3]
                i+=4
            elif i+4 <len(cuvant) and cuvant[i] in vocale and cuvant[i + 1] in vocale and cuvant[i + 2] in vocale and cuvant[i + 3] in vocale:
                cuvant_despartit += cuvant[i] + '-' + cuvant[i + 1] + cuvant[i + 2] + cuvant[i + 3]
                i+=4
            elif i+2 <len(cuvant) and cuvant[i] in vocale and cuvant[i + 1] in vocale and cuvant[i + 2] in consoane and \
                    not is_semivocala(cuvant, i) and is_semivocala(cuvant, i+1) :
                cuvant_despartit += cuvant[i] + cuvant[i + 1] + '-' + cuvant[i + 2]
                i+=3
            else:
                cuvant_despartit += cuvant[i]
                i += 1
        return cuvant_despartit


def printare_vector(vector):
    cuv = ""
    for i in vector:
        cuv += i
    return cuv


def formare_cuvinte(cuvant):
    silabe = re.split("-", cuvant)
    permutari_silabe = list(itertools.permutations(silabe))
    lista_majuscule = []
    for permutare in permutari_silabe:
        cuvant = printare_vector(list(permutare))
        if cuvant not in lista_majuscule:
            lista_majuscule.append(cuvant.upper())
    return lista_majuscule


def cautare_cuvinte():
    cuvinte_gasite = []
    cuvinte_cautate = formare_cuvinte(entry_punct3.get())
    with open(fisier, 'r') as file:
        for line in file:
            cuvinte = line.strip().split()
            for cuvant in cuvinte:
                if cuvant in cuvinte_cautate and cuvant not in cuvinte_gasite:
                    cuvinte_gasite.append(cuvant)
    print("Cuvintele ce se pot forma din " + entry_punct3.get() + " sunt: ", cuvinte_gasite)


def despartire():
    c = list(prolog.query(f"despartire('{entry_cuv.get()}', Rezultat)"))
    regula12 = c[0]['Rezultat']
    cuv3 = regula3(regula12)
    cuv4 = regula4(cuv3)
    print("Cuvantul " + entry_cuv.get() + " despartit in silabe este: " + cuv4)
    return cuv4


def despartire2(cuvant):
    c = list(prolog.query(f"despartire('{cuvant}', Rezultat)"))
    regula12 = c[0]['Rezultat']
    cuv3 = regula3(regula12)
    cuv4 = regula4(cuv3)
    return cuv4


def secv_silabe_valide():
    despartit = entry_punct2.get()
    legat = entry_punct2.get().replace(" ", "")
    cuvnou = despartire2(legat)
    cuvnou = re.sub(r'-', ' ', cuvnou)
    if cuvnou == despartit:
        print(legat)
    else:
        print("Fail")


frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label_punct1 = ctk.CTkLabel(master=frame, text="Desparte cuvinte in silabe")
label_punct1.configure(font=("Arial", 20, "bold"))
label_punct1.pack(pady=12, padx=10)

entry_cuv = ctk.CTkEntry(master=frame, placeholder_text="Introduceti un cuvant")
entry_cuv.pack(pady=12, padx=10)

button_desp = ctk.CTkButton(master=frame, text="Desparte", command=despartire, fg_color='#FF0', text_color='#000')
button_desp.pack(pady=12, padx=10)


label_punct2 = ctk.CTkLabel(master=frame, text="Verifica daca despartirea este corecta")
label_punct2.configure(font=("Arial", 20, "bold"))
label_punct2.pack(pady=12, padx=10)

entry_punct2 = ctk.CTkEntry(master=frame, placeholder_text="Silabele cu spatiu")
entry_punct2.pack(pady=12, padx=10)

button_punct2 = ctk.CTkButton(master=frame, text="Verifica", command=secv_silabe_valide)
button_punct2.pack(pady=12, padx=10)


label_punct3 = ctk.CTkLabel(master=frame, text="Printeaza cuvintele valide formate din silabele:")
label_punct3.configure(font=("Arial", 20, "bold"))
label_punct3.pack(pady=12, padx=10)

entry_punct3 = ctk.CTkEntry(master=frame, placeholder_text="Silabele cu cratima")
entry_punct3.pack(pady=12, padx=10)

button_punct3 = ctk.CTkButton(master=frame, text="Printeaza", command=cautare_cuvinte)
button_punct3.pack(pady=12, padx=10)


root.mainloop()








