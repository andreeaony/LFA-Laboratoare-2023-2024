#FUNCTII
def load_file(file_name):
    f=open(file_name, "r")
    d={}

    #lista cu toate liniile din fisier
    l=[]
    for line in f:
        l.append(line.strip())

    #formare dictionar
    elements=[]
    one=0
    for element in l:
        if '#' in element:
            pass
        elif ':' in element:
            if one>0: #daca am gasit inainte un nume
                d[nume]=elements
            one=1 #marchez ca am gasit un nume
            nume=element.strip(':')
            elements=[]
        elif element!='End':
            elements.append(element)
    d[nume]=elements
    return d

def get_section_list(content):
    section_list=[]
    for key in content:
        section_list.append(key)
    return section_list

def get_section_content(content, section_name):
    section_content=[]
    for key in content:
        if key==section_name:
            for element in content[key]:
                section_content.append(element)
    return section_content
"""
#RULARE FUNCTII
content=load_file("M2")
print(content)
section_list=get_section_list(content)
print(section_list)
section_content=get_section_content(content,"Sigma")
print(section_content)
"""
