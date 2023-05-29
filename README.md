# Mi script de Utilidad - Renombrar de Archivos "bak" a "dwg"

El programa de dibujo asistido por computadora "Auto CAD", manufacturado por Autodesk genera, durante la creacion de un archivo, uno o varios archivos con extension <<.bak>>; estos son puntos de restauracion automaticos que el soft gerera cada cierto tiempo. Cuando un archivo de CAD <<.dwg>> resulta corrupto o lo hemos cerrado sin guardar sus cambios es que podemos recurrir a este archivo de respaldo.

El script renombra todos los archivos (dentro del folio de ejecución) que con la extesion ***.bak*** a ***.dwg*** agregando al principio del nombre un guion bajo ***_*** para no generar conflictos con el documentos original en el directorio.

Para la realizacion de este script he consultado las siguientes fuentes:
- https://markdown.es/
- https://docs.python.org/es/3.10/library/os.html
- http://www.tugurium.com/python/index.php?C=PYTHON.12_1_1
