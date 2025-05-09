mamifero = {'perra' , 'gorila' , 'mono' ,'macaco' }
aves = {'cuervo' , 'pato' , 'gallina', 'agila'}
reptil = {'serpiente' , 'lagartija', 'comodo' , 'iguana'}

animal = str(input('Introduzca un animal : ')).upper()
if animal in mamifero : 
    print(f'El animal es un mono ')
elif animal in aves : 
    print(f'El animal es un ave ')
elif animal in reptil : 
    print(f'El animal es un reptil ')
else : 
    print(f'Es otro tipo de animal')
