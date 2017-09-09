class Cliente(object):
    estado_cuenta = None
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def __len__(self):
        return self.edad

    def __str__(self):
        #return self.nombre+' '+self.apellido
        #return ' '.join(self.nombre,self.apellido)
        #dato = 'cliente: $s $s' % (self.nombre,self.apellido)
        return self.getNombres()

    def getNombres(self):
        return ' '.join(self.nombre,self.apellido)

    @property
    def Nombres(self):
        return ' '.join(self.nombre,self.apellido)

if __file__ == '__main':
    cliente = Cliente('Davis', 'Turin', edad=28)

    print(cliente.edad)
    print(cliente.nombre, len(cliente))
    cliente.edad = '30'
    print(cliente.nombre, len(cliente))

