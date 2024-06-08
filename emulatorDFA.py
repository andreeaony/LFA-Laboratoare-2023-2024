import parsser
content=parsser.load_file("M2")
print(content)
string=input()

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


for index in range(len(string)): #pentru fiecare litera
    if string[index] in content['Sigma']: #daca apartine alfabetului
        for i in range(len(initialState)): #pornesc cu toate starile mele initiale
            initial=initialState[i]
            for transition in content["Transitions"]: #parcurg toate tranzitiile
                if transition.split(" , ")[0]==initial: #gasesc tranzitia care incepe cu starea mea
                    if transition.split(" , ")[1]==string[index]: #si care merge pe litera citita de mine
                        initialState[i]=transition.split(" , ")[2] #si actualizez initial state-ul curent
    else:
        print("Alfabetul nu contine elemente din string-ul introdus.")
        alfabetGresit=1

#la final, ar trebui ca in lista initialStates sa am starile finale in care am ajuns in urma operatiilor efectuate de delta
ok=1
for element in initialState:
    if element not in finalState:
        ok=0
        break

if ok==0 or alfabetGresit==1:
    print("String neacceptat.")
else:
    print("String acceptat.")
