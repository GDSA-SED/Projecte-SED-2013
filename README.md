-----------------------------------------------------------------------------------------------------------------
**English**

_Project description_:

This code presents an event image classifier realized as a project for the Catalonian University UPC, for the subject of audiovisual signals management and distribution, course 2013-2014.

For this case, we proposed a classifier programmed in Python based on meta-data, concretely the hash tags, using a supervised learning system for an already existent set of classes. MySQL is used to manage the data with a database.
The evaluation system used for this project returns the F-score with the Precision and Recall, Divergence from a Random Baseline and the Normalized Mutual Information (NMI). The code shows the information in a visual way through graphs when it’s executed.

_How to use the program_:

The main file is responsible of making both learning and classification of data calling the other functions. The program returns a .txt file with the ID of all images and the name of the event in which they’ve been classified in their right. It’ll also ask for the directory where the images are once executed.
The evaluation file will ask for the document to evaluate, generated by the main and in .txt format. Then, the evaluation parameters will be returned.

**Important**, in order to make the program work properly, it is needed to create a folder called ‘results’ in the working directory. Also, it's needed to have the [evaluation script] (http://atenea.upc.edu/moodle/mod/resource/view.php?id=420453) of MediaEval in the same folder that the evaluation program.

_Design_:

The descriptor uses tf-idf to weigh the tags, increasing or decreasing their value. During learning, the program gets every image and adds its tags to the corresponding class, making a count of how many times a tag is repeated in a class, which will allow the program to calculate the tf-idf for each tag.
Then, the classifier compares the tags of the image to classified with the coincident ones of the class that is being compared with. The weighs are then added and the class with a higher number of coincidences is assigned as such. If there are no matches, the image is declared as a non-event image.

_Libraries_:

- matplotlib.pyplot : http://matplotlib.org/api/pyplot_summary.html

- numpy : http://docs.scipy.org/doc/numpy/reference/

- math : http://docs.python.org/2/library/math.html

- decimal : http://docs.python.org/2/library/decimal.html

- mysqldb : http://mysql-python.sourceforge.net/MySQLdb.html



-----------------------------------------------------------------------------------------------------------------

**Español**

_Descripción del proyecto_:

Este código presenta un clasificador de imágenes de eventos realizado para un proyecto de la Universidad Catalana UPC, para la asignatura de gestión y distribución de señales audiovisuales curso 2013-2014.

Para este caso, propusimos un clasificador programado en python basado en metadatos, concretamente los hashtags, usando un sistema de aprendizaje supervisado para unas categorías ya existentes. Se utiliza MySQL como base de datos para la gestión de estos.
El sistema de evaluación empleado para este proyecto retorna el F-score con la presicion y el recall, la divergencia de una línea de base aleatoria e información mutua normalizada (NMI). El código muestra información de forma visual mediante gráficas una vez ejecutado.

_Como utilizar el programa_:

El archivo main se encarga de hacer tanto el aprendizaje como la clasificacion de datos llamando a la resta de funciones. Devuelve un archivo .txt con todas las imágenes y a su derecha el nombre de la categoria en que se ha clasificado. El mismo archivo preguntara los directorios de las imágenes una vez ejecutado.
El archivo de evaluacion pide el documento a evaluar, generado por el main y de tipo txt. Tras esto se generaran las medidas de evaluación.

**Importante**, para que el programa funcione debe existir una carpeta llamada ‘results’ en el directorio de trabajo. Además, se necesita tener el [script de evaluación] (http://atenea.upc.edu/moodle/mod/resource/view.php?id=420453) de MediaEval en la misma carpeta que el programa de evaluación.

_Diseño_:

El descriptor utiliza tf-idf para ponderar los tags dándoles mas o menos importancia. Durante el aprendizaje, el programa coge cada imagen y añade sus tags a la clase correspondiente, haciendo un recuento de cuantas veces se repite un tag por clase que luego permitira hacer el tf-idf de cada tag.
Luego el clasificador compara los tags de la imagen a clasificar con los tags coincidentes de la clase que se esta comparando. Las ponderaciones se suman y la clase que tenga un mayor numero de coincidencia se asigna como tal. En caso de que no haya coincidencias, la imagen se declara como no evento.

_Librerías_:


- matplotlib.pyplot : http://matplotlib.org/api/pyplot_summary.html

- numpy : http://docs.scipy.org/doc/numpy/reference/

- math : http://docs.python.org/2/library/math.html

- decimal : http://docs.python.org/2/library/decimal.html

- mysqldb : http://mysql-python.sourceforge.net/MySQLdb.html

------------------------------------------------------------------------------------------------------------------
**Català**

_Descripció del projecte_:

Aquest codi presenta un classificador d'imatges d'esdeveniments realitzat per a un projecte de la Universitat Catalana UPC, per a l'assignatura de gestió i distribució de senyals audiovisuals curs 2013-2014.

Per a aquest cas, vam proposar un classificador programat en Python basat en metadades, concretament els hashtags, usant un sistema d'aprenentatge supervisat per a unes categories ja existents. S'utilitza MySQL com a base de dades per a la gestió d'aquests.
El sistema d'avaluació emprat per a aquest projecte retorna el F-Score amb la Precisió i el Recall, la divergència d'una línia de base aleatòria i informació mútua normalitzada (NMI). El codi mostra informació de forma visual mitjançant gràfiques una vegada executat.

_Com utilitzar el programa_:

L'arxiu main s'encarrega de fer tant l'aprenentatge com la clasificacion de dades cridant a la resta de funcions. Retorna un arxiu .txt amb totes les imatges i a la seva dreta el nom de la categoria en què s'ha classificat. El mateix arxiu preguntés els directoris de les imatges una vegada executat.
L'arxiu de avaluació demana el document a avaluar, generat pel main i de tipus .txt . Després d'això es generessin les mesures d'avaluació.

**Important**, perquè el programa funcioni ha d'existir una carpeta anomenada ‘results’ en el directori de treball. A mes, es necesari incloure el [script d'avaluació] (http://atenea.upc.edu/moodle/mod/resource/view.php?id=420453) de MediaEval a la amteixa carpeta que el programa d'avaluació.

_Disseny_:

El descriptor utilitza tf-idf per ponderar els tags donant-los mes o menys importància. Durant l'aprenentatge, el programa agafa cada imatge i afegeix les seves tags a la classe corresponent, fent un recompte de quantes vegades es repeteix un tag per classe que després permet fer el tf-idf de cada tag.
Després el classificador compara els tags de la imatge a classificar amb els tags coincidents de la classe que s'està comparant. Les ponderacions se sumen i la classe que tingui un major numero de coincidència s'assigna com a tal. En cas que no hi hagi coincidències, la imatge es declara com no esdeveniment.

_Llibreries:_


- matplotlib.pyplot : http://matplotlib.org/api/pyplot_summary.html

- numpy : http://docs.scipy.org/doc/numpy/reference/

- math : http://docs.python.org/2/library/math.html

- decimal : http://docs.python.org/2/library/decimal.html

- mysqldb : http://mysql-python.sourceforge.net/MySQLdb.html
