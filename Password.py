import random

p = ["+","-","/","*","!","&","$","#","?","=","@","a","b","c","d","e","f","g","h","i","j","k","l","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]

a = int(input('Que tan larga quieres que sea tu contraseña? '))
j = ''
for i in range(a):
    b = random.choice(p)
    j += b

print('Tu contraseña es: ', j)
