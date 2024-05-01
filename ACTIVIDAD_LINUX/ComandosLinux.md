<img src="https://github.com/gcdavidq/Data-Communication-And-Networks_Group/blob/main/Images/logo_upch.png" style="width: 50%;" />

## **ACTIVIDAD_COMANDOS LINUX** 
----------------
Alumno: Quezada Marceliano Gian Carlos
----------------

Primera vista del terminal de Linux Ubuntu:

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.001.jpeg)

Para probar que es funcional podemos tratar de ejecutar cualquier comando de manera aleatoria, veremos que nos genera un error como a continuación:

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.002.jpeg)

Como primer comando, empleamos el comando PWD, el cual nos darà el directorio actual de trabajo en el que nos encontramos:

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.003.jpeg)

También tenemos otro comando importante, el cual es ls, este nos listarà los archivos que actualmente tenemos:

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.004.jpeg)Para cambiar el directorio de trabajo en el que estamos usamos “cd”, con este comando podemos acceder a una ruta específica del laboratorio. Para ejecutar dicho comando, tecleamos cd, seguido por el nombre de la ruta deseada.

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.005.jpeg)

Continuando,aprenderemos a movernos usando rutas relativas. Para ello, usaremos un par de notaciones especiales, el “.” y “..” ; la primera se refiere a la ruta del trabajo en si, mientras que la segunda se refiere a la ruta padre de la misma ruta de trabajo:

Para realizar esta demostración, empezaremos realizando el proceso pero colocando la ruta completa. Lo que se quiere lograr, es regresar al directorio padre de la ruta de trabajo.

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.006.jpeg)

Ahora, haremos lo mismo pero usando una ruta relativa.

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.007.jpeg)

Como se aprecia, de ambas formas conseguimos regresar al directorio padre, sin embargo, con la segunda se puede considerar más sencillo y práctico.

Ahora, aplicaremos el proceso de manera inversa, con la ruta padre llegaremos al directorio de trabajo, también de las 2 formas ya explicadas:

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.008.jpeg)

Ahora, haremos lo mismo pero empleando la ruta relativa:

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.009.jpeg)

**TRABAJANDO CON COMANDOS: TYPE**

-Para saber que tipo de comando es uno en particular, podemos emplear al shell “type”, el cual funciona de la siguiente manera:

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.010.jpeg)

**WHICH**

-Para saber que programa instalado se està ejecutando en el sistema podemos emplear “which”:

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.011.jpeg)

**Type**

-Ahora, a manera de ayuda, existe una forma de saber màs acerca de cualquiera de los

shell anteriormente visto, para ello, escribimos “type” seguido del shell que necesitamos averiguar:

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.012.jpeg)

**- - Help**

Otra forma de buscar la opción de ayuda es empleando “--help”, el cual nos darà una breve descripciòn del comando, junto con las opciones disponibles y sus descripciones en cada una de ellas:

**MAN**

Lo que nos proporciona este comando es una especie de manual, el cual contiene informacion detalla de como usar este comando y sus diferentes funciones. A diferencia de “--help”, con man tenemos informaciòn màs detallada:

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.013.jpeg)

**REDIRECCIÒN I/O SALIDAS STANDAR**

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.014.jpeg)

Lo que acà estamos haciendo es que liste los archivos y directorios del directorio actual y que guarde dicha lista en el archivo “text\_list..txt”

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.015.jpeg)

A diferencia del anterior, con este comando lo que buscamos es añadir la listà que se crearà la final de la informacion que tiene el archivo, y si es que no existe crearemos uno.

**Entrada Estandar:**

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.016.jpeg)

Lo que acabamos de hacer con este comando es primero, tomar la información del archivo “file\_list.txt” y, con ayuda de sort, ordenar la información dentro de aquella lista, por ultimo, se mostrarà el resultado en la salida estándar que vendria a ser la pantalla en este caso.

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.017.png)

Esta última línea de comando se divide en dos partes, primero, como en la anterior, ordenamos la lista existente en el archivo ya mencionado, pero ademàs se crea un nuevo archivo y se agrega dicha lista ordenada.![](Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.018.jpeg)

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.019.png)

En este caso, la primera parte del comando “ls -l”, nos listarà los archivos y directorios en el directorio actual con detalles extendidos, luego, se traslada esta lista hacia less, el cual nos permitirà desplazarnos entre los datos, de arriba hacia abajo.

**EXPANSIÓN**

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.020.jpeg)

Lo que acabamos de hacer es mostrar un mensaje en la salida mediante el comando echo, el cual sirve para imprimir mensajes en la salida estándar

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.021.jpeg)

En este otro ejemplo, tambien aplicamos echo junto con el comodin \*, el cual nos muestra una lista de todos los archivos y directorios.

**Pathname Expansión**

Veamos diferentes formas en las que se emplean los comodines:

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.022.jpeg)

Muestra los archivos o directorios cuyos nombres empiecen con D

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.023.jpeg)

Muestra los archivos y escritorios que terminen con s.

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.024.jpeg)

Muestra los archivos y directorios cuyos nombres empiecen con mayuscula.

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.025.jpeg)

Muestra la ruta de los directorios llamados share que se encuentren dentro de usr. **Tilde Expansion**

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.026.jpeg)

Imprime la ruta completa del directorio principal del actual usuario.

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.027.jpeg)

Imprime la ruta del directorio principal del usuario “foo”, si no existe, solo imprimirà el supuesto nombre del usuario.

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.028.jpeg)

Imprime en pantalla una operaciòn aritmètica, el $ nos ayudarà a realizar las evaluaciones aritméticas en la linea de comandos.

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.029.jpeg)

Imprime un mensaje y el resultado de la operaciòn. **Brace Expansion**

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.030.jpeg)

Se muestra una lista de cadenas en las que se tiene que combinar los valores de la cadena con Front y Back

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.031.jpeg)

Genera una lista de cadenas en las que se combina Number con cada uno de los números en el rango de 1 a 5.

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.032.jpeg)

Genera una lista de caracteres que van de Z a A

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.033.jpeg)

Genera listas con las posibles combinaciones dentro de cada subconjunto y al final imprime toda slas combinaciones,

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.034.jpeg)

En este grupo de comandos primero: Creamos el directorio Photos, luego cambiamos el directorio de trabajo al directorio recién creado. En la tercera linea de comandos, se crean varios directorios, en el primer conjunto se simulan los años, y en el segundo los meses, por último, se lista todos los directorios creados.

**Parameter Expansion**

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.035.jpeg)

Imprime el nombre actual del usuario.

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.036.png)

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.037.jpeg)Lo primero que se hace es imprimir todas las variables de entorno existentes en el sistema, para después presentarlas de manera paginada, permitiendo desplazarse de arriba hacia abajo.

**Command Substitution**

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.038.png)

Imprime una lista de todos los archivos y directorios en el escritorio actual.

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.039.png)

Muestra información detallada del comando cd, incluyendo permisos.

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.040.jpeg)Primero, lista todos los archivos en el directorio /usr/bin, pero luego, especifica en esa parte para que la salida solo sea de archivos zip. Luego, con file, nos dirà que tipo de archivo es el ejecutable zip.

![](Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.041.png)

Primero se encuentra la ruta ejecutable del comando cp, para que despues se muerte su infocmaciòn detallada.

**Quoting**

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.042.png)

Acà podemos apreciar un tipo de fallo, si se puede decir así. Lo que pasa es que, como sabemos, el signo $ se emplea para variables o realizar sustitución de comandos. En este caso, se està emplean para buscar el valor de la variable 100, y al no encontrarlo imprime un valor nulo.

**Double Quotes**

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.043.png)

ESte es otro caso bastante común, pues mientras que nosotros queremos que “two words.txt ” que se trate como un solo argumento, el sistema lo trata como dos argumentos diferentes, de ahì el error.

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.044.png)

En este otro caso, en el que se usa comillas dobles para asegurar que el comando interprete correctamente el nombre del archivo. SIn embargo, al no existir un archivo con ese nombre, nos arroja dicho error.

**Single Quotes**

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.045.png)

**La entrada de los 3 comandos parece similar, pero no es así, generando que sus resultados tampoco. Todo varía en cómo se emplean las comillas. En el primer caso no hay comillas, por lo que la linea como se espera. Para el segundo caso, hay comillas dobles, ello genera que lo que esté entre llaves no se ejecute, sin embargo, el $USER si se ejecuta, ya que no está en las comillas. Por último, el ejemplo con camillas simples, en este caso, todo el comando se interpreta como una cadena string.**

**Escaping Characters**

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.046.png)

Al colocarse la barra invertida, se evita que $S se ejecute, pues se lee como una cadena o caracter.

**File Permissions**

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.047.png)

Se muestra información extensa del comando bash, el cual se encuentra dentro del directorio bin.

CHMOD

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.048.png)

LO que se pretende hacer es cambiar los permisos del archivo some\_file, sin embargo, nos aparece que el archivo no existe. Aun asì, podemos interpretar que el “600” representa al modo octal que se està empleando, en este caso significa que solo el propietario puede leer y editar el archivo.

**Becoming the Superuser for a Short While**

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.049.png)

Estamos intentando ingresar al superusuario, el cual puede servir para realizar importantes tareas de administración del sistema. Sin embargo, nos pide una contraseña.

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.050.png)

Esta es otra forma de acceder a los privilegios del superusuario, en este caso nos pide la contraseña para poder acceder al usuario root.

**JOB CONTROL**

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.051.png)

Muestra un grafico de la carga del sistema en el entorno de escritorio X Window System.

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.052.png)

Hace lo mismo que el anterior pero en segundo plano. **Listing Running Processes**

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.053.png)

Primero, jobs sirve para mostrar que procesos hay en segundo plano, en nuestro caso, ninguno. Por otro lado, ps muestra todos los procesos de ejecución del sistema.

**Killing a Process**

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.054.jpeg)

**A Little More About kill**

![](https://github.com/gcdavidq/Gian_Quezada_CDyR/blob/main/ACTIVIDAD_LINUX/Images/Aspose.Words.262015e2-4d3a-4a8f-91ba-6402131e8980.055.png)

Lo primero que hacemos es usar ps para identificar el PID del proceso que queremos terminar. Lo ideal es emplear sigterm y sigkill para intentar terminar el proceso con el PDO 27127, sin embargo, a mi me apareció un error al momento de ejecutar las líneas de comando. Ello no descarta que de manera ideal no deben existir errores asì.
