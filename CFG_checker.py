import parsser
content=parsser.load_file("CFG")

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

#VERIFICARE CORECTITUDINE VARIABILE REGULI
reguli=parsser.get_section_content(content,"Rules")
sigma=parsser.get_section_content(content, "Sigma")
vars=parsser.get_section_content(content, "Vars")

corespondenta=1
for cuvant in reguli:
    for litera in range(len(cuvant)):
        if cuvant[litera]!="," and cuvant[litera]!=" ":
            if cuvant[litera] not in sigma and cuvant[litera] not in vars:
                corespondenta=0

if(corespondenta==0):
    print("ATENTIE! Caracterele din sectiunea Rules nu corespund cu cele din sectiunile Sigma si Vars!")
else:
    print("Sectiunea Rules este bine definita. Caracterele din sectiunea Rules corespund cu cele din sectiunile Sigma si Vars!")

#VERIFICARE CORECTITUDINE LUNGIME VARIABILE REGULI
reguli=parsser.get_section_content(content,"Rules")
reguli.remove(reguli[len(reguli)-1])

corect=1
for regula in reguli:
    if len(regula.split(" , "))!=2:
        corect=0
    elif len(regula.split(" , ")[0])==1 and len(regula.split(" , ")[1])<=1:
        corect=0
    elif len(regula.split(" , ")[0])>1:
        corect=0

if corect==1:
    print("Sectiunea Rules este bine definita din punct de vedere al partilor reprezentative regulii.")
elif corect==0:
    print("Sectiunea Rules nu este bine definita din punct de vedere al partilor reprezentative regulii.")