import os
def renombraExtensionesBack():
    """
    Renombra los docuementos con extesión ".bak" que se encuentren en el directorio de ejecución.
    Cambia su extension a ".dwg" extension de AutoCAD.
    El nombre resultante es: _nombreArchivo.dwg. El guion bajo al principio es para que no existan conflicto con el archivo cad existen.

    Args:
        no recibe argumentos por parametro

    Returns:
        mensaje por pantalla que finalizo
    """
    extension=".bak"
    extensionNew=".dwg"
    ruta=os.getcwd()
    lista=os.listdir()
    print("*** RENOMBRAR BAK DE CAD ***")
    for i in lista:
        if i[-4:]==extension:
            new="_"+i[:-4]+extensionNew
            os.rename(i,new)
                  
if __name__=="__main__":
    renombraExtensionesBack()
os.system("Pause")