#koristit cemo funkcije iz time modulea
import time
import string
import random

#zapocni brojati vrijeme
pocetno_vrijeme = time.time()

#sve moguce rijeci
lista_rijeci = ['V R A T', 'O S A', 'S U N C E', 'P E D A L A', 'C V I J E T', 'P O T O C I', 'Z E K O', 'I G R A', 'S T A B L O', 'J A Z A V A C', 'T O R B A', 'B U M B A R', 'K A M E N', 'P L O D', 'O K O']

#rijeci koje odgovaraju odgovorima
lista_odgovora = []

#pretvori rijeci u mala slova, obrisi razmake i dodaj u lista_odgovora koja nam sluzi za pogadanje
for i in lista_rijeci:
    temp_string = i.replace(" ", "").lower()
    lista_odgovora.append(temp_string)

#postavimo trenutne i max bodove
trenutni_bodovi = 0
max_bodovi = len(lista_rijeci)

#podijeli listu rijeci u liste, kasnije nam to sluzi za redove
lista_1 = lista_rijeci[:3]
lista_2 = lista_rijeci[3:6]
lista_3 = lista_rijeci[6:9]
lista_4 = lista_rijeci[9:12]
lista_5 = lista_rijeci[12:15]

#provjeri duljinu svakog reda da bude u svakom redu jednako slova
total_lista_1 = 0
for word in lista_1:
    total_lista_1 += len(word)
total_lista_2 = 0
for word in lista_2:
    total_lista_2 += len(word)
total_lista_3 = 0
for word in lista_3:
    total_lista_3 += len(word)
total_lista_4 = 0
for word in lista_4:
    total_lista_4 += len(word)
total_lista_5 = 0
for word in lista_5:
    total_lista_5 += len(word)

#svi redovi moraju biti dugacki kao najdulji
longest_row = max(total_lista_1, total_lista_2, total_lista_3, total_lista_4, total_lista_5)

#dodaj random slova u redove ako nisu jednako dugi kao najdulji
for i in range((longest_row - total_lista_1)//2):
    lista_1.append(random.choice(string.ascii_uppercase))
for i in range((longest_row - total_lista_2)//2):
    lista_2.append(random.choice(string.ascii_uppercase))
for i in range((longest_row - total_lista_3)//2):
    lista_3.append(random.choice(string.ascii_uppercase))
for i in range((longest_row - total_lista_4)//2):
    lista_4.append(random.choice(string.ascii_uppercase))
for i in range((longest_row - total_lista_5)//2):
    lista_5.append(random.choice(string.ascii_uppercase))

#isprintaj svaku listu u svoj red i svako polje razdvoji razmakom
for i in (lista_1, lista_2, lista_3, lista_4, lista_5):
    print(*i, sep=' ')

#unosi rijeci sve dok ih sve ne pogodis
while trenutni_bodovi != max_bodovi:
    #unesi rijec
    unesena_rijec = input().lower()
    #ako je unesena rijec u mogucim rijecima
    if unesena_rijec in lista_odgovora:
        #povecaj bodove za 1
        trenutni_bodovi += 1
        #izbrisi rijec iz liste rijeci
        lista_odgovora.remove(unesena_rijec)
        print('Cestitamo, preostalo je jos {} rijeci.\n'.format(max_bodovi - trenutni_bodovi))
    else:
        print('Rijec ne postoji ili je vec unesena, molimo pokusajte ponovo.\n')

#zaustavi brojanje vremena, vrjednost proteklog vremena je jednako pocetno vrijeme - trenutno vrijeme
proteklo_vrijeme = time.time() - pocetno_vrijeme

print('Cestitamo, pogodili ste sve rijeci u {}s!\n'.format(int(proteklo_vrijeme)))