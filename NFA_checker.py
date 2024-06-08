import parsser
content=parsser.load_file("nfa")

#VERIFICARE EXISTENTA FISIER
if content=={}:
    print("Fisierul nu a putut fi incarcat deoarece acesta nu exista.")
else:
    print("Fisierul a fost incarcat.")
    print(content)

#VERIFICARE EXISTENTA SECTIUNE LISTA
section_list=parsser.get_section_list(content)
if section_list==[]:
    print("Sectiunile nu au fost afisate deoarece fisierul incarcat nu are sectiuni.")
else:
    print("Sectiunile au fost afisate.")
    print(section_list)

#VERIFICARE EXISTENTA VALORI IN SECTIUNE
section_content=parsser.get_section_content(content,"Sigma")
if section_content==[]:
    print("Continutul sectiunii alese nu a fost afisat deoarece sectiunea selectata nu are continut sau sectiunea nu exista.")
else:
    print("Continutul sectiunii alese a fost afisat.")
    print(section_content)

#VERIFICARE CORECTITUDINE ALFABET
sigma=parsser.get_section_content(content,"Sigma")
def eliminate_duplicates(list):
    new_list=[]
    for element in list:
        if element not in new_list:
            new_list.append(element)
    return new_list
section_content=eliminate_duplicates(sigma)
if len(sigma)!=len(section_content):
    print("ATENTIE! Simbolurile alfabetului se repeta!")

#VERIFICARE CORECTITUDINE MULTIME STARI
#verific ca in multimea starilor sa existe obligatoriu cel putin o stare initiala si una finala
states=parsser.get_section_content(content,"States")
exista_start=0
exista_final=0
for element in states:
    if " , S" in element:
        exista_start=1
    if " , F" in element:
        exista_final=1
if exista_start==0:
    print("ATENTIE! NFA-ul incarcat nu are stare initiala!")
elif exista_start==0:
    print("ATENTIE! NFA-ul incarcat nu are stare finala!")
elif exista_start==0 and exista_final==0:
    print("ATENTIE! NFA-ul incarcat nu are stare nici stare initiala si nici stare finala!")
