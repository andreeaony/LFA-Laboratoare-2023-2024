import parsser
content=parsser.load_file("nfa")
string=input("Introduceti stringul de verificat:")

#extragere stare initiala si stare finala
initialState=[]
finalState=[]
alfabetGresit=0
for key in content:
    for element in content[key]:
        if ", S" in element and key=="States":
            initialState.append(element.split(",")[0].strip())
        if ", F" in element and key=="States":
            finalState.append(element.split(",")[0].strip())

string+=string[-1]
initial=[]
alfabetGresit=0
for index in range(len(string)):  # pentru fiecare litera
    if string[index] in content['Sigma']:  # daca apartine alfabetului
        initial=[]
        for transition in content['Transitions']:  # parcurg toate tranzitiile
             if transition.split(" , ")[0] in initialState:  # gasesc tranzitia care incepe cu starea initiala
                if transition.split(" , ")[1] == string[index] or transition.split(" , ")[1] == " ":  # si care merge pe litera citita de mine sau pe epsilon
                        initial.extend(transition.split(' , ')[2:])  # adaug noile stari inițiale
        initialState=initial[:] # si apoi actualizeaz lista de stări inițiale pentru urmatoarea parcurgere
    else:
        alfabetGresit=1
acceptat=0
for element in finalState:
    if element in initialState:
        acceptat=1

if alfabetGresit==1 or acceptat==0:
    print("String refuzat")
else:
    print("String accceptat")


