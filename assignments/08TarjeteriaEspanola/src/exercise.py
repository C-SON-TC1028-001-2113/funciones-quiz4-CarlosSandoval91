def num_pliegues(x,y):
    x= x*12
    y= y*35
    if x<y:
        return(x)
    elif y<x:
        return(y)
def main():
    #escribe tu código abajo de esta línea
    x=int(input('Dame la cantidad de pliegos de papel albanene: '))
    y=int(input('Dame la cantidad de plumones: '))
    
    z = num_pliegues(x,y)
    print('El número máximo de tarjetas que se pueden hacer es: '+str(z))

if __name__=='__main__':
    main()
    #pytest assignments/08TarjeteriaEspanola