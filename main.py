usuarioAccedio = False
# Bienvenida!
mensaje_bienvenida = 'Bienvenide al sistema!\nAccede con tus credenciales'
print (mensaje_bienvenida)
# Resibo constantemente sus intentos
while not usuarioAccedio:
    # Primero ingresa Credenciales
    usuario = input('Usuario: ')
    contras = input('Contrase;a: ')
    # Reviso si el par coincide
    if usuario == 'kikitos' and contras == 'felino' :         usuarioAccedio = True  
        print("hola de nuevo!")
    else:
        if usuario == 'kikitos':
            print('Te equivocaste en la contrase;a')
    else:
        print (f'El usuario: "{usuario}" no esta registrado') 
print('Solamente llegaste aqui si ingresaste correctamente')