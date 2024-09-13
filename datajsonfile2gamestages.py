import os
from os import listdir
from os.path import isdir
import json

def write_dictionaries_to_file(tab):
    filename = 'output.txt'
    with open(filename, 'w') as file:
        for text in tab:
            file.write(f"{text}\n")

def test_json(file_path):
    test = ""
    for loopr in range(len(file_path)-1, len(file_path)-5, -1):
        test = test + file_path[loopr]
    if test != "nosj":
        return False
    if os.path.isfile(file_path):
        if os.path.getsize(file_path) == 0:
            return False
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            if "type" in data:
                if data["type"] == "minecraft:crafting_shaped":
                    return True
            return False
    else:
        print(f"File not found: {file_path}")
        return False
        
def fonction():
    tab = []
    rep = listdir()
    for i in range(len(rep)):
        rep1 = rep[i]
        if isdir(rep1):
            for j in range(len(listdir(rep1))):
                rep5 = rep1 + "/" + listdir(rep1)[j]
                if isdir(rep5):
                    for k in range(len(listdir(rep5))):
                        rep2 = rep1 + ":" + listdir(rep5)[k]
                        rep6 = rep5 + "/" + listdir(rep5)[k]
                        if not isdir(rep6):
                            if test_json(rep6):
                                tab.append(rep2)
                        if isdir(rep6):
                            for l in range(len(listdir(rep6))):
                                rep3 = rep2 + "/" + listdir(rep6)[l]
                                rep7 = rep6 + "/" + listdir(rep6)[l]
                                if os.path.isfile(rep7) :
                                    if test_json(rep7):
                                        tab.append(rep3)
                                if isdir(rep7):
                                    for m in range(len(listdir(rep7))):
                                        rep4 = rep3 + "/" + listdir(rep7)[m]
                                        rep8 = rep7 + "/" + listdir(rep7)[m]
                                        if os.path.isfile(rep8) :
                                            if test_json(rep8):
                                                tab.append(rep4)
                                        if isdir(rep8):
                                            for n in range(len(listdir(rep8))):
                                                rep9 = rep4 + "/" + listdir(rep8)[n]
                                                rep10 = rep8 + "/" + listdir(rep8)[n]
                                                if os.path.isfile(rep10) :
                                                    if test_json(rep10):
                                                        tab.append(rep9)
                                                else :
                                                    print(rep9 + "/")
    write_dictionaries_to_file(tab)