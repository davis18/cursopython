from modelo.clientes import Cliente

cliente = Cliente('Davis','Turin', edad=28)

print (cliente.edad)
print (cliente.nombre,len(cliente))

cliente.edad='30'

print (cliente.nombre,len(cliente))
