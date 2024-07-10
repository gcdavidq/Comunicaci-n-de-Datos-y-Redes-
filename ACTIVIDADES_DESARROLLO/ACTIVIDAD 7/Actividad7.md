![ref1]**Departamento Académico de Ingeniería**

**C8280 -Comunicación de Datos y Redes**

**Actividad 7 : Investigación de los modelos TCP/IP y OSI**

.
# ` `**Objetivos**
**Parte 1: Examinar el tráfico web HTTP**

**Parte 2: Mostrar elementos de la suite de protocolos TCP/IP Utiliza el archivo .pka que acompaña la actividad.**
# ` `**Aspectos básicos**
Esta actividad de simulación tiene como objetivo proporcionar una base para comprender la suite de protocolos TCP/IP y la relación con el modelo OSI. El modo de simulación le permite ver el contenido de los datos que se envían a través de la red en cada capa.

A medida que los datos se desplazan por la red, se dividen en partes más pequeñas y se identifican de modo que las piezas se puedan volver a unir cuando lleguen al destino. A cada pieza se le asigna un nombre específico (unidad de datos del protocolo [PDU]) y se la asocia a una capa específica de los modelos TCP/IP y OSI. El modo de simulación de Packet Tracer te permite ver cada una de las capas y la PDU asociada. Los siguientes pasos te guían a través del proceso de solicitud de una página web desde un servidor web mediante la aplicación de navegador web disponible en una PC cliente.

` `**Instrucciones**


# **1 . Examinar el tráfico web HTTP**
En la parte 1 de esta actividad, utilizará el modo de simulación de Packet Tracer (PT) para generar tráfico web y examinar HTTP.

**Cambia del modo de tiempo real al modo de simulación.**

En la esquina inferior derecha de la interfaz de Packet Tracer, hay fichas que permiten alternar entre el modo **Tiempo real** y **Simulación**. El Packet Tracer siempre comienza en modo en **tiempo real**, donde los protocolos de red operan con temporizaciones realistas. Sin embargo, una función eficaz de Packet Tracer permite al usuario “detener el tiempo” conmutando al modo de simulación. En el modo de simulación, los paquetes se muestran como sobres animados, el tiempo es desencadenado por eventos y el usuario puede revisar los eventos de red.

1. Haz clic en el ícono del modo de **Simulación** para cambiar del modo de **Tiempo real** al modo de **Simulación**.
1. Selecciona **HTTP** en **Filtros de lista de eventos**.
   1) Es posible que HTTP ya sea el único evento visible. Si es necesario, haz clic en el botón **Editar filtros** en la parte inferior del panel de simulación para mostrar los eventos visibles disponibles. Alterna la casilla de verificación **Mostrar todo/ninguno** y observa cómo las casillas de verificación se desactivan y se activan, o viceversa, según el estado actual.
   1) Haz clic en la casilla de verificación **Mostrar todo/ninguno** hasta que se desactiven todas las casillas y luego selecciona **HTTP**. Haz clic en la X situada en la esquina superior derecha de la ventana para cerrar la ventana **Editar filtros** . Los eventos visibles ahora deben mostrar sólo HTTP.

**Genera tráfico web (HTTP).**

Actualmente, el panel de simulación está vacío. En la parte superior de Lista de eventos dentro del panel de simulación, se indican cinco columnas. A medida que se genera y se revisa el tráfico, aparecen los eventos en la lista.

**Nota:** el servidor web y el cliente web se muestran en el panel de la izquierda. Se puede ajustar el tamaño de los paneles manteniendo el mouse junto a la barra de desplazamiento y arrastrando a la izquierda o a la derecha cuando aparece la flecha de dos puntas.

1. Haz clic en **Cliente web** en el panel del extremo izquierdo.
1. Haz clic en la ficha **Escritorio** y luego en el ícono **Navegador web** para abrirlo.
1. En el campo de dirección URL, introduce **www.osi.local** y haga clic en **Ir**.

   Debido a que el tiempo en el modo de simulación se desencadena por eventos, debes usar el botón **Capturar/avanzar** para mostrar los eventos de red. El botón de captura hacia adelante se encuentra en el lado izquierdo de la banda azul que está debajo de la ventana de topología. De los tres botones, es el de la derecha.

1. Haz clic en **Capturar/Avanzar** cuatro veces. Deberías haber cuatro eventos en la Lista de eventos.

   Pregunta:

   Observa la página del navegador web del cliente web. ¿Cambió algo?

   Si, aparece el siguiente mensaje, “You have successfully accessed the home page for Web Server.”
   
## **Explora el contenido del paquete HTTP**
1. Haz clic en el primer cuadro coloreado debajo de la columna **Lista de eventos** > **Información**. Quizá sea necesario expandir el **panel de simulación** o usar la barra de desplazamiento que se encuentra directamente debajo de la **lista de eventos**.

   Se muestra la ventana **Información de PDU en dispositivo: cliente web**. En esta ventana, solo hay dos fichas, (**Modelo OSI** y **Detalles de PDU saliente**), debido a que este es el inicio de la transmisión. A medida que se analizan más eventos, se muestran tres fichas, ya que se agrega la ficha **Detalles de PDU entrante**. Cuando un evento es el último evento de la transmisión de tráfico, solo se muestran las fichas **Modelo OSI** y **Detalles de PDU entrante**.

1. Asegúrate de que esté seleccionada la ficha **Modelo OSI**.

   En la columna **Capas de salida** , haga clic en **Capa 7** .

   Preguntas:

   ¿Qué información se indica en los pasos numerados directamente debajo de los cuadros **Capas de entrada** y **Capas de salida**?

   Se muestra este mensaje The HTTP client sends a HTTP request to the server, que indica que un cliente http envio una solicitud al servidor

   ¿Cuál es el valor del **puerto Dst** para la **capa 4** en la columna **Capas de salida**?

   El puerto de destino 80

   ¿Cuál es el **destino? ¿** Valor IP para la **Capa 3** en la columna **Capas de salida** ?

   El ip de destino es 192.168.1.254

   ¿Qué información se muestra en la Capa 2 en la columna **Capas de salida**?

   Se muestra las direcciones mac, y la orientación de donde a dónde va la información

![](Aspose.Words.52aa9739-5bff-4a18-813a-4692f430536e.002.png)El encabezado Ethernet II de capa 2 y las direcciones MAC entrantes y salientes**.**

`	`c.	Haz clic en la ficha de **Detalles de la PDU saliente**.

La información que se indica debajo de **Detalles de PDU** refleja las capas dentro del modelo TCP/IP.

Nota**: La información que se indica en la sección** Ethernet II **proporciona información aún más detallada que la que se indica en capa 2 en la ficha Modelo OSI.** Los **detalles de la PDU** saliente proporcionan información más descriptiva y detallada. Los **valores de** MAC DE DEST. **y de** MAC DE ORIGEN **en la sección** Ethernet II **de** Detalles de PDU **aparecen en la ficha** Modelo OSI**, en capa 2, pero no se los identifica como tales.**

Preguntas:

¿Cuál es la información frecuente que se indica en la sección **IP** de **detalles de PDU** comparada con la información que se indica en la ficha **Modelo OSI**? ¿Con qué capa se relaciona?

En la seccon IP se pueden ver las direcciones de salida y de destino, esto pertenece a la capa 3

¿Cuál es la información frecuente que se indica en la sección **TCP** de **Detalles de PDU** comparada con la información que se indica en la ficha **Modelo OSI**?

En la sección TCP, se encuentran los puertos de entrada y destino, pertenecen a la cpaa 4

¿Cuál es el **host** que se indica en la sección **HTTP** de **Detalles de PDU**? ¿Con qué capa se relacionaría esta información en la ficha **Modelo OSI**?

El host es [www.osi.local](http://www.osi.local), y pertenece a la capa 7

4. Haz clic en el primer cuadro coloreado debajo de la columna **Lista de eventos** >**Tipo**. Solo la capa 1 está activa (sin atenuar). El dispositivo mueve el frame desde el búfer y la coloca en la red.
4. Avanza al siguiente cuadro **Tipo** de HTTP dentro de la **lista de eventos** y haz clic en el cuadro coloreado. Esta ventana contiene las columnas **Capas de entrada** y **Capas de salida**. Observa la dirección de la flecha que está directamente debajo de la columna **Capas de entrada**; esta apunta hacia arriba, lo que indica la dirección en la que se transfiere la información. Desplázate por estas capas y toma nota de los elementos vistos anteriormente. En la parte superior de la columna, la flecha apunta hacia la derecha. Esto indica que el servidor ahora envía la información de regreso al cliente. Compara la información que se muestra en la columna **Capas de entrada** con la de la columna **Capas de salida**: ¿cuáles son las diferencias principales?
4. Haz clic en la ficha **Inbound PDU Details** (Detalles de PDU entrante). Revisa los detalles de la PDU.
4. Haz clic en el último cuadro coloreado de la columna **Información**.Explica los resultados.

   En el modelo OSI, solo se aprecia los resultados de inlayer, ya que solo esta recibiendo la informacion, no la envia, ya que ya termino el proceso, y por lo mismo solo aparece la pestaña inbound
# **2. Mostrar elementos de la suite de protocolos TCP/IP**
En la parte 2 de esta actividad, utilizará el modo de simulación de Packet Tracer para ver y examinar algunos de los otros protocolos que componen la suite TCP/IP.

**Ver eventos adicionales**

1. Cierra todas las ventanas de información de PDU abiertas.
1. En la sección **Filtros de lista de eventos** > **Eventos visibles**, haga clic en **Mostrar todo.**

   Pregunta:

   ¿Qué tipos de eventos adicionales se muestran?

   Se muestran DNS, TCP y ARP

   Estas entradas adicionales cumplen diversas funciones dentro de la suite TCP/IP. El Protocolo de resolución de direcciones (ARP) solicita direcciones MAC para los hosts de destino. El protocolo DNS es responsable de convertir un nombre (por ejemplo, **www.osi.local**) a una dirección IP. Los eventos de TCP adicionales son responsables de la conexión, del acuerdo de los parámetros de comunicación y de la desconexión de las sesiones de comunicación entre los dispositivos.

1. Haz clic en el primer evento de DNS en la columna **Información**. Examina las fichas **Modelo**

   **OSI** y **Detalles de PDU**, y observa el proceso de encapsulamiento. Al observar la ficha

   **Modelo OSI** con el cuadro **capa 7** resaltado, se incluye una descripción de lo que ocurre, inmediatamente debajo de las **Capas de entrada** y las **Capas de salida**: (“1. The DNS client sends a DNS query to the DNS server.” [“El cliente DNS envía una consulta DNS al servidor DNS”]). Esta información es muy útil para ayudarte a comprender qué ocurre durante el proceso de comunicación.

1. Haz clic en la ficha de **Detalles de la PDU saliente**.

   Pregunta:

   ¿Qué información se indica en **NOMBRE**: en la sección CONSULTA DNS?

   Indica el host www.osi.local

1. Haz clic en el último cuadro coloreado **Información** de DNS en la lista de eventos.

   Preguntas:

   ¿En qué dispositivo se capturó la PDU?

   En el web client

   ¿Cuál es el valor que se indica junto a **DIRECCIÓN**: en la sección RESPUESTA DE DNS de **Detalles de la PDU entrante**?

   192\.168.1.254

1. Busca el primer evento de **HTTP** en la lista y haga clic en el cuadro coloreado del evento de **TCP** que le sigue inmediatamente a este evento. Resalte **capa 4** en la ficha **Modelo OSI**.

   Pregunta:

   En la lista numerada que está directamente debajo de **Capas de entrada** y **Capas de salida**, ¿cuál es la información que se muestra en los elementos 4 y 5?. El protocolo TCP administra la conexión y la desconexión del canal de comunicaciones, además de tener otras responsabilidades. Este evento específico muestra que SE ESTABLECIÓ el canal de comunicaciones.

1. Haz clic en el último evento de TCP. Resalte capa 4 en la ficha **Modelo OSI**. Examine los pasos que se indican directamente a continuación de **Capas de entrada** y **Capas de salida**.

   Pregunta:

   ¿Cuál es el propósito de este evento, según la información proporcionada en el último elemento de la lista (debe ser el elemento 4)?

   Esto indica que la conexión se cerró, ya que ya se termino el proceso

   ***Escriba sus respuestas aquí.***
# ` `**Preguntas**


En esta simulación, se proporcionó un ejemplo de una sesión web entre un cliente y un servidor en una red de área local (LAN). El cliente realiza solicitudes de servicios específicos que se ejecutan en el servidor. Se debe configurar el servidor para que escuche puertos específicos y detecte una solicitud de cliente. (Sugerencia: observe la capa 4 en la ficha **Modelo OSI** para obtener información del puerto).

Sobre la base de la información que se analizó durante la captura de Packet Tracer, ¿qué número de puerto escucha el **servidor web** para detectar la solicitud web?

El puerto 80

¿Qué puerto escucha el **servidor web** para detectar una solicitud de DNS?

El puerto 53

***Escriba sus respuestas aquí.***

*Fin del documento*
Comunicación de Datos y Redes

[ref1]: Aspose.Words.52aa9739-5bff-4a18-813a-4692f430536e.001.png
