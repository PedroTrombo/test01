#Creando un archivo
nombre_archivo="archivo.txt"

archivo=open(nombre_archivo,'w') #abre archivo en modo w. Escribe y machaca lo que contenga
archivo.write("Python es un lenguaje de programación orientado a objetos.\n")
archivo.write("Y Mario y yo nos estamos volviendo locos con ello.\n")
archivo.close()


archivo=open('archivo_02.txt','w')
archivo.write("Python es un lenguaje de programación orientado a objetos.\n")
archivo.close()