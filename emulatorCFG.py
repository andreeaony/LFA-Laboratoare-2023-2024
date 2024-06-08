import parsser
content=parsser.load_file("CFG")
string=input("Introduceti un string de verificat: ")

variabila_start=content['Vars'][0]

#functie care verifica daca un string este acceptat de gramatica
def acceptat(start, string):
    stiva=[(start, string)]

    while stiva: #cat timp stiva nu este goala
        variabila_curenta, string_ramas=stiva.pop() #scoatem cate o pereche din stiva si o atribuim lui valoare_curenta si string_ramas

        #ambele goale=> acceptat (stiva a ramas goala)
        if variabila_curenta=='' and string_ramas=='':
            return True

        #verificare corespondenta intre caracterele variabilei curente si stringul ramas
        if variabila_curenta!='' and variabila_curenta[0] in content['Sigma']: #daca primul caracter din variabila_curenta este simbol din alfabet 
            if string_ramas!='' and variabila_curenta[0]==string_ramas[0]: #verificam daca se potriveste cu primul caracter din stringul ramas
                stiva.append((variabila_curenta[1:], string_ramas[1:])) #daca se potrivesc, adaugam pe stiva restul ramas din fiecare, pentru a le verifica si pe acestea
        elif variabila_curenta and variabila_curenta[0] in content['Vars']: #daca primul caracter din variabila_curenta este simbol din variabile
            rest=variabila_curenta[1:]
            for rule in content['Rules']:
                ce, in_ce=rule.split(' , ')
                if ce==variabila_curenta[0]:
                    stiva.append((in_ce+rest, string_ramas)) #adaugam pe stiva transformarea efectuata
    return False

if acceptat(variabila_start, string):
    print("Stringul este acceptat de gramatică.")
else:
    print("Stringul nu este acceptat de gramatică.")
