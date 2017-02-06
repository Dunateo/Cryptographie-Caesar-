rot6=str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ','UVWXYZABCDEFGHIJKLMNOPQRST')
print(str.translate(input("message="),rot6))
#str.maketrans permet de modifier l'alphabet en alphabet+6, et str.translate permet de traduire le message avec l'alphabet definit plus haut
