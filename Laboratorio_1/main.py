# 1. Realizar las siguientes sustituciones: j × i, h × i,  ̃n× n, k × l, u × v, w × v, y × z
txt_exercise_1_read=open("input.txt", encoding='utf-8')

# with open('file.txt', 'r', encoding='utf-8') as file:
#     data = file.read()

test_inmmutable=txt_exercise_1_read.read()

txt_exercise_1_read.close()

test_mutable_copy=open("exercise_1.txt","w")



# print(test_inmmutable)


for i in range(len(test_inmmutable)):
    character_to_add=test_inmmutable[i]
    match character_to_add:
        case 'j':
            character_to_add='i'
        case 'h':
            character_to_add='i'
        
        case 'ñ':
            character_to_add='n'
        
        case 'k':
            character_to_add='l'

        case 'u':
            character_to_add='v'

        case 'w':
            character_to_add='v'
        
        case 'y':
            character_to_add='z'
    
    test_mutable_copy.write(character_to_add)
            
print(test_mutable_copy)

# 2. Elimine las tildes
test_inmmutable_2="áéíóus'''''''adasds"
test_mutable_2_copy=""
# print(test_inmmutable_2)


for i in range(len(test_inmmutable_2)):
    character_to_add=test_inmmutable_2[i]
    match character_to_add:
        case 'á':
            character_to_add='a'
        case 'é':
            character_to_add='e'
        
        case 'í':
            character_to_add='i'
        
        case 'ó':
            character_to_add='o'

        case 'ú':
            character_to_add='u'
        
        case "'":
            character_to_add=''
    
    test_mutable_2_copy+=character_to_add
            
test_inmmutable_2=test_mutable_2_copy
# print(test_inmmutable_2)
#3. Convierta todas las letras a may ́usculas
test_inmmutable_3="sadasdsascsacqwwesASDASD"
# print(test_inmmutable_3)

test_inmmutable_3=test_inmmutable_3.upper()
# print(test_inmmutable_3)

#4.  Elimine los espacios en blanco y los signos de puntuaci ́on.
# Guarde el resultado en el archivo ”HERALDOSNEGROS pre.txt”