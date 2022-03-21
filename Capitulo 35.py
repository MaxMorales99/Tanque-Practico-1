def fav(*args):
    	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

fav("verde","rojo")

def suma(*args):
    c= args[0] + args[1] + args[2] +args[3] + args[4]
    print("El rsultado de sumar 5+7+15+21+50 es igual a:", c)


suma(5,7,15,21,50)