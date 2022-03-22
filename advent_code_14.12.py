# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 11:49:48 2021

@author: Niky
"""


def parse_input(fh):
    with open(f"{fh}.txt") as f:
        lines = []
        for x in f.readlines():
            if x =="\n":
                continue
            else:
                x = x.strip("\n")
                lines.append(x)
    template = lines.pop(0)
    template_molecules = []
    template_dict = {}
    for mol in template:
        if mol not in template_molecules:
            template_molecules.append(mol)
    dict_polymers = {}
    for e in lines:
        e=e.split("->")
        dict_polymers[e[0].strip(" ")] = e[1].strip(" ")
    for el in dict_polymers.keys():
        if dict_polymers[el] not in template_molecules:
            template_molecules.append(dict_polymers[el])
    for mol in template_molecules:
        for mol2 in template_molecules:
            template_dict[mol+mol2]= 0
    nmr_of_steps = len(template)-1
    for i in range(0, nmr_of_steps):
        key = template[i]+template[i+1]
        template_dict[key] +=1
    counts = count_elements(template)
    return dict_polymers, template_dict, counts

def parse_insertion(dict_polymers, template, counts):
    new_template = {}
    for e in template.keys():
        new_template[e]=0
    for i in template.keys():
        number_of_reps = template[i]
        if number_of_reps >0:
            new_key1 = i[0]+dict_polymers[i]
            new_key2 = dict_polymers[i]+i[1]
            counts.setdefault(dict_polymers[i],0 )
            counts[dict_polymers[i]]+=number_of_reps
            new_template[new_key1]+=number_of_reps
            new_template[new_key2]+=number_of_reps
    return new_template, counts

def count_elements(template):
    counts = {}
    for i in template:
        counts.setdefault(i,0 )
        counts[i] +=1
    return counts

dict_polymers, template_dict, counts = parse_input("test")
for i in range(0,40): ### For the first assignment, change range(0,40) to (0,10)
    template_dict, counts = parse_insertion(dict_polymers, template_dict, counts)
result = max(counts.values())-min(counts.values())
print(result)
