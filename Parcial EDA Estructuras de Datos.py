import csv

POKEMON = []

with open(r'C:\Users\jorge\OneDrive\Escritorio\python\pokemon.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            POKEMON.append(row[0])
            POKEMON.append(row[1])
            POKEMON.append(row[2])
            POKEMON.append(row[3])
            POKEMON.append(row[4])
            POKEMON.append(row[5])
            POKEMON.append(row[6])
            POKEMON.append(row[7])
            POKEMON.append(row[8])
            POKEMON.append(row[9])
            POKEMON.append(row[10])
            POKEMON.append(row[11])
            POKEMON.append(row[12])
            #print(f'\t{row[0]}  {row[1]}  {row[2]}  {row[3]}    {row[4]}    {row[5]}    {row[6]}    {row[7]}    {row[8]}    {row[9]}    {row[10]}   {row[11]}   {row[12]}.')
            line_count += 1
    print(f'Processed {line_count} lines.') 


print("Media de TODOS los pokemon(sin separar): ")
y=4
z=0
media=0
for x in range(len(POKEMON)):
    if x==y:
        y=y+13
        media=media+int(POKEMON[x])
        z=z+1

media = media/z

print("Media del total: "+str(media))

y1=5
z=0
media=0
for x in range(len(POKEMON)):
    if x==y1:
        y1=y1+13
        media=media+int(POKEMON[x])
        z=z+1


media = media/z


print("Media del HP: "+str(media))

y1=6
z=0
media=0
for x in range(len(POKEMON)):
    if x==y1:
        y1=y1+13
        media=media+int(POKEMON[x])
        z=z+1


media = media/z



print("Media del Ataque: "+str(media))


y1=7
z=0
media=0
for x in range(len(POKEMON)):
    if x==y1:
        y1=y1+13
        media=media+int(POKEMON[x])
        z=z+1


media = media/z

print("Media de la Defensa: "+str(media))

y1=8
z=0
media=0
for x in range(len(POKEMON)):
    if x==y1:
        y1=y1+13
        media=media+int(POKEMON[x])
        z=z+1


media = media/z

print("Media del Ataque Especial: "+str(media))


y1=9
z=0
media=0
for x in range(len(POKEMON)):
    if x==y1:
        y1=y1+13
        media=media+int(POKEMON[x])
        z=z+1


media = media/z


print("Media de la Defensa Especial: "+str(media))


y1=10
z=0
media=0
for x in range(len(POKEMON)):
    if x==y1:
        y1=y1+13
        media=media+int(POKEMON[x])
        z=z+1


media = media/z


print("Media de la Velocidad: "+str(media))


y1=12
z=0
media=0
for x in range(len(POKEMON)):
    if x==y1:
        y1=y1+13
        if POKEMON[x]=="True":
            media=media+1
        z=z+1

#print(media)
media = (media/z)*100 

print("Porcentaje de legendarios: "+str(media)+"%")

#print(POKEMON)

print("La primera mitad de los pokemon correspondera al primer entrenador, ahora es tu decsion a partir de que pokemon quieres que sea del segundo. ")

v11 = int(input("Introduzca numero de pokemon donde se dividirán los pokemon(el que pongas esta incluido con el primer entrenador)"))












