-----------------------------------------------------------------------------------------------------------------
**English**

_Project description_:

This code presents an event image classifier realized as a project for the Catalonian University UPC, for the subject of audiovisual signals management and distribution, course 2013-2014.

For this case, we proposed a classifier programmed in Python based on meta-data, concretely the hash tags, using a supervised learning system for an already existent set of classes. MySQL is used to manage the data with a database.
The evaluation system used for this project returns the F-score with the Precision and Recall, and the Accuracy. The code shows the information in a visual way through graphs when it’s executed.

_How to use the program_:

The main file is responsible of making both learning and classification of data calling the other functions. The program returns a .txt file with the ID of all images and the name of the event in which they’ve been classified in their right. It’ll also ask for the directory where the images are once executed.

As said before, this program uses a database, in this case named gdsa. The user and password is root, as it is set by the program. Also, the following table should exist: sed2013_task2_dataset_train with the fields 'document_id' as primary key, 'url_pic',  'url_page',   'username',  'date_taken',   'title',   'latitude',   'longitude'; sed2013_task2_dataset_train_gs with the fields 'document_id' as primary key, 'event_type' and sed2013_task2_dataset_train_tags with the fields 'document_id' as primary key, and 'tag'.
  

**Important**, in order to make the program work properly, it is needed to create a folder called ‘results’ in the working directory. That's because the evaluation script will return the parameters of all the classifications inside this folder.

_Design_:

The descriptor uses tf-idf to weigh the tags, increasing or decreasing their value. During learning, the program gets every image and adds its tags to the corresponding class, making a count of how many times a tag is repeated in a class, which will allow the program to calculate the tf-idf for each tag.
Then, the classifier compares the tags of the image to classified with the coincident ones of the class that is being compared with. The weighs are then added and the class with a higher number of coincidences is assigned as such. If there are no matches, the image is declared as a non-event image.

_Libraries_:

- matplotlib.pyplot : http://matplotlib.org/api/pyplot_summary.html

- numpy : http://docs.scipy.org/doc/numpy/reference/

- math : http://docs.python.org/2/library/math.html

- decimal : http://docs.python.org/2/library/decimal.html

- mysqldb : http://mysql-python.sourceforge.net/MySQLdb.html

_Complementary_ _evaluation_:

The folder called complementary_evaluation contains a program that can be used to obtain the Divergence from a Random Baseline and the Normalized Mutual Information (NMI) of the results.  To do so, it's needed to have the [evaluation script] (http://atenea.upc.edu/moodle/mod/resource/view.php?id=420453) of MediaEval in the same folder that the evaluation program.


-----------------------------------------------------------------------------------------------------------------

**Español**

_Descripción del proyecto_:

Este código presenta un clasificador de imágenes de eventos realizado para un proyecto de la Universidad Catalana UPC, para la asignatura de gestión y distribución de señales audiovisuales curso 2013-2014.

Para este caso, propusimos un clasificador programado en python basado en metadatos, concretamente los hashtags, usando un sistema de aprendizaje supervisado para unas categorías ya existentes. Se utiliza MySQL como base de datos para la gestión de estos.
El sistema de evaluación empleado para este proyecto retorna el F-score con la Precisión y el Recuerdo, y la Accuracy. El código muestra información de forma visual mediante gráficas una vez ejecutado.

_Como utilizar el programa_:

El archivo main se encarga de hacer tanto el aprendizaje como la clasificacion de datos llamando a la resta de funciones. Devuelve un archivo .txt con todas las imágenes y a su derecha el nombre de la categoria en que se ha clasificado. El mismo archivo preguntara los directorios de las imágenes una vez ejecutado.

Como se ha mencionado anteriormente, este programa utiliza una base de datos que se debe llamar gdsa. El usuario y la contraseña son root,  ya que así está puesto en el programa. Además, deben existir las siguientes tablas: sed2013_task2_dataset_train con los campos 'document_id' como primary key, 'url_pic',  'url_page',   'username',  'date_taken',   'title',   'latitude',   'longitude'; sed2013_task2_dataset_train_gs con los campos 'document_id' como primary key, 'event_type' y sed2013_task2_dataset_train_tags con los campos 'document_id' como primary key, y 'tag'.

**Importante**, para que el programa funcione debe existir una carpeta llamada ‘results’ en el directorio de trabajo. Esto se debe a que el script de evaluación retorna los parametros de todos los archivos que se encuentren en esta carpeta. 

_Diseño_:

El descriptor utiliza tf-idf para ponderar los tags dándoles mas o menos importancia. Durante el aprendizaje, el programa coge cada imagen y añade sus tags a la clase correspondiente, haciendo un recuento de cuantas veces se repite un tag por clase que luego permitira hacer el tf-idf de cada tag.
Luego el clasificador compara los tags de la imagen a clasificar con los tags coincidentes de la clase que se esta comparando. Las ponderaciones se suman y la clase que tenga un mayor numero de coincidencia se asigna como tal. En caso de que no haya coincidencias, la imagen se declara como no evento.

_Librerías_:


- matplotlib.pyplot : http://matplotlib.org/api/pyplot_summary.html

- numpy : http://docs.scipy.org/doc/numpy/reference/

- math : http://docs.python.org/2/library/math.html

- decimal : http://docs.python.org/2/library/decimal.html

- mysqldb : http://mysql-python.sourceforge.net/MySQLdb.html

_Evaluación_ _complementaria_:

La carpeta llamada complementary_evaluation contiene un programa que se puede utilizar para obtener la Divergencia de una línea de base aleatoria y la Información mútua normalizada (NMI) de los resultados.  Para hacerlo, se necesita tener el [script de evaluación] (http://atenea.upc.edu/moodle/mod/resource/view.php?id=420453) de MediaEval en la misma carpeta que el programa de evaluación.

------------------------------------------------------------------------------------------------------------------
**Català**

_Descripció del projecte_:

Aquest codi presenta un classificador d'imatges d'esdeveniments realitzat per a un projecte de la Universitat Catalana UPC, per a l'assignatura de gestió i distribució de senyals audiovisuals curs 2013-2014.

Per a aquest cas, vam proposar un classificador programat en Python basat en metadades, concretament els hashtags, usant un sistema d'aprenentatge supervisat per a unes categories ja existents. S'utilitza MySQL com a base de dades per a la gestió d'aquests.
El sistema d'avaluació emprat per a aquest projecte retorna el F-Score amb la Precisió i el Recall, i la Accuracy. El codi mostra informació de forma visual mitjançant gràfiques una vegada executat.

_Com utilitzar el programa_:

L'arxiu main s'encarrega de fer tant l'aprenentatge com la clasificacion de dades cridant a la resta de funcions. Retorna un arxiu .txt amb totes les imatges i a la seva dreta el nom de la categoria en què s'ha classificat. El mateix arxiu preguntés els directoris de les imatges una vegada executat.

Como s'ha esmentat anteriorment, aquest programa utilitza una base de dades que s'anomena gdsa. L'usuari i la contrasenya son root,  ja que així el programa accedeix. A mes, han d'existir les següents taules: sed2013_task2_dataset_train amb els camps 'document_id' com primary key, 'url_pic',  'url_page',   'username',  'date_taken',   'title',   'latitude',   'longitude'; sed2013_task2_dataset_train_gs amb els camps 'document_id' com primary key, 'event_type' i sed2013_task2_dataset_train_tags amb els camps 'document_id' com primary key, i 'tag'.

**Important**, perquè el programa funcioni ha d'existir una carpeta anomenada ‘results’ en el directori de treball. Això és degut a que el script d'avaluació retorna els paràmetres de tots els archius que es trobin en aquesta carpeta. 

_Disseny_:

El descriptor utilitza tf-idf per ponderar els tags donant-los mes o menys importància. Durant l'aprenentatge, el programa agafa cada imatge i afegeix les seves tags a la classe corresponent, fent un recompte de quantes vegades es repeteix un tag per classe que després permet fer el tf-idf de cada tag.
Després el classificador compara els tags de la imatge a classificar amb els tags coincidents de la classe que s'està comparant. Les ponderacions se sumen i la classe que tingui un major numero de coincidència s'assigna com a tal. En cas que no hi hagi coincidències, la imatge es declara com no esdeveniment.

_Llibreries:_


- matplotlib.pyplot : http://matplotlib.org/api/pyplot_summary.html

- numpy : http://docs.scipy.org/doc/numpy/reference/

- math : http://docs.python.org/2/library/math.html

- decimal : http://docs.python.org/2/library/decimal.html

- mysqldb : http://mysql-python.sourceforge.net/MySQLdb.html

_Avaluació_ _complementaria_:

La carpeta anomenada complementary_evaluation conté un programa que es pot utilizar per obtenir la Divergencia d'una línea de base aleatoria i la Informació mútua normalitzada (NMI) dels resultats.  Per poder fer-ho, es necesari incloure el [script d'avaluació] (http://atenea.upc.edu/moodle/mod/resource/view.php?id=420453) de MediaEval a la mateixa carpeta que el programa d'avaluació.

------------------------------------------------------------------------------------------------------------------

**日本語：**


**プロジェクトの説明：**

このコードは、カタロニア大学、UPCのプロジェクトのために作られたイベントの画像の分類器を提示、年間 2013-2014「audiovisual signals management and distribution」の主語とするため。

この場合のために、既存のカテゴリの教師付き学習システム使い方、メタデータに基づいて「Python」でプログラミングさクラシファイアを持ちかけた、具体的には、ハッシュタグ。「MySQL」は、これらを管理するためのデータベースとして使用されている。このプロジェクトのために使用される評価システムは、 プレーシジオンと F-スコアと リコールと アッキュラシイとして返されます。一度実行した、コードは、グラフィックスによって視覚的に情報が表示されます。

**プログラムを使用する方法：**

メインファイルは、両方の学習をする責任がある関数減算を呼び出してデータの分類など。.txtファイルをすべての付き右のでそれが分類されたカテゴリの名前返します。一度実行した、ディレクトリの同じファイルはの画像を依頼する。評価ファイルは評価するドキュメントを要求、メインと .txtファイルで生成された。この後で評価尺度が生成された。


上述したように、このプログラムは、データベースを使用しています、「gdsa」が呼び出ます必要があります。ユーザとパスワードはrootです、などので、プログラムにある。さらに、次の表は、存在している必要があります：sed2013_task2_dataset_trainフィールドを持ち'document_id' プライマリーキーとの, 'url_pic', 'url_page', 'username', 'date_taken', 'title', 'latitude', 'longitude'; sed2013_task2_dataset_train_gsフィールドを持ち'document_id'プライマリーキーとの, 'event_type'そしてsed2013_task2_dataset_train_tagsフィールドを持ち'document_id'プライマリーキーとの, そして 'tag'.


**重要**、プログラムが動作するための作業ディレクトリに「results」というフォルダが存在しなければならない。これは、スクリプト評価はパラメータこのフォルダすべてのファイルを内にあることに取って返す。

**デザイン:**

記述子は、タグは、多かれ少なかれ重要性を与えてTF-IDF重みを使用していました。間に学習中、プログラムでは、各画像を取得しておよびそれらの対応するクラスにタグを追加、クラスのタグを繰り返す回数をカウントをしますにより、その後、各タグのTF-IDFを作ることができます。その後、分類子が比較されているクラスに一致するタグを分類するためにイメージタグを比較します。重みは合計され、暗合数の多いクラスが割り当てられているなど。一致するものがない場合、画像はイベントとして宣言しません。

**図書館：**

- matplotlib.pyplot : http://matplotlib.org/api/pyplot_summary.html

- numpy : http://docs.scipy.org/doc/numpy/reference/

- math : http://docs.python.org/2/library/math.html

- decimal : http://docs.python.org/2/library/decimal.html

- mysqldb : http://mysql-python.sourceforge.net/MySQLdb.html

__追加の評価:__

complementary_evaluationというフォルダは、プログラムが含まれています。これは、発散ランダムにラインを得るために使用することができると結果の正規化相互情報（NMI）。これを行うには、評価のプログラムと同じフォルダにスクリプト評価MediaEvalを持っている必要があります。

