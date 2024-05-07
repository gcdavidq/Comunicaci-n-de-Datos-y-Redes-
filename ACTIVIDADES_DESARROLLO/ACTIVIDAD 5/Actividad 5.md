![](Aspose.Words.8eaec84a-b48a-4f93-bd2d-0bb8fde15c7e.001.png)

**Departamento Académico de Ingeniería C8280 -Comunicación de Datos y Redes** 

**Actividad 5: Identificación de direcciones MACy direcciones IP**

**Objetivos**

**Parte 1: Recopilar información de PDU para la comunicación de red local Parte 2: Recopilar información de PDU para la comunicación de red remota**

**Aspectos básicos**

Esta actividad está optimizada para la visualización de PDU[^1]. Los dispositivos ya están configurados. Reunirá información de PDU en el modo de simulación y responderá una serie de preguntas sobre los datos que obtenga.

**Instrucciones**

**Recopila información del PDU para la comunicación de red local**

1. **Recopila información de la PDU a medida que un paquete viaja de 172.16.31.5 a 172.16.31.2.**
1. Haz clic en **172.16.31.5** y abra el **Command Prompt**.
1. Introduce el comando **ping 172.16.31.2**.
1. Cambia al modo de simulación y repita el comando **ping 172.16.31.2** . Aparece una PDU junto a **172.16.31.5**.
1. Haz clic en la PDU y observa la siguiente información de las pestañas **Modelo OSI l** y **Capa de PDU saliente:**
- Destination MAC Address:**000C:85CC:1DA7**
- Source MAC Address: **00D0:D311:C788**
- Source IP Address:**172.16.31.5**
- Destination IP Address: **172.16.31.2**
- At Device: **172.16.31.5**
5. Haz clic en **Capture / Forward (la flecha derecha seguida de una barra vertical)** para mover la PDU al siguiente dispositivo. Reúna la misma información del paso 1d. Repite este proceso hasta que la PDU llegue al destino. Registra la información que reunió de la PDU en una hoja de cálculo con un formato como el de la tabla que se muestra a continuación:

**Formato de hoja de cálculo de ejemplo**



|**En dispositivo**|**MAC de destino**|**MAC de origen**|**IPv4 de origen**|**IPv4 de destino**|
| - | - | - | - | - |
|172\.16.31.5|000C:85CC:1DA7|00D0:D311:C788|172\.16.31.5|172\.16.31.2|
|**En dispositivo**|**MAC de destino**|**MAC de origen**|**IPv4 de origen**|**IPv4 de destino**|
|Switch1|000C:85CC:1DA7|00D0:D311:C788|No corresponde|No corresponde|
|Concentrador|No corresponde|No corresponde|No corresponde|No corresponde|
|172\.16.31.2|00D0:D311:C788|000C:85CC:1DA7|172\.16.31.2|172\.16.31.5|

**2 . Reunir información adicional de la PDU de otros ping.**

Repite el proceso del paso 1 y reúna información para las siguientes pruebas:

- Ping de 172.16.31.2 a 172.16.31.3
- Ping de 172.16.31.4 a 172.16.31.5

Vuelva al modo Realtime.

2. **Recopila información del PDU para la comunicación de red remota**

Para comunicarse con redes remotas, es necesario un dispositivo de puerta de enlace. Estudia el proceso que tiene lugar para comunicarse con los dispositivos de la red remota. Presta mucha atención a las direcciones MAC utilizadas.

**Recopila información de la PDU a medida que un paquete viaja de 172.16.31.5 a 10.10.10.2.**

1. Haz click en **172.16.31.5** y abra el **Command Prompt**.
1. Introduce el comando **ping 10.10.10.2**.
1. Cambia al modo de simulación y repita el comando **ping 10.10.10.2** . Aparece una PDU junto a **172.16.31.5**.
1. Haz clic en la PDU y observe la siguiente información en la ficha **Outbound PDU Layer (Capa de PDU saliente)**:

   Destination MAC Address: 00D0:BA8E:741A Source MAC Address: 00D0:D311:C788 Source IP Address: 172.16.31.5

   Destination IP Address: 10.10.10.2

   At Device: 172.16.31.5

   ¿Qué dispositivo tiene el MAC de destino que se muestra?
   La MAC que se muestra es del router. 

5. Haz clic en **Capture / Forward (la flecha derecha seguida de una barra vertical)** para mover la PDU al siguiente dispositivo. Reúne la misma información del paso 1d. Repite este proceso hasta que la PDU llegue al destino. Registra la información de la PDU que recopiló del ping 172.16.31.5 a 10.10.10.2 en una hoja de cálculo utilizando un formato como la tabla de muestra que se muestra a continuación:



|**En dispositivo**|**MAC de destino**|**MAC de origen**|**IPv4 de origen**|**IPv4 de destino**|
| - | - | - | - | - |
|172\.16.31.5|00D0:BA8E:741A|00D0:D311:C788|172\.16.31.5|10\.10.10.2|
|Switch1|00D0:BA8E:741A|00D0:D311:C788|No corresponde|No corresponde|
|Router|0060:2 F 84:4 AB6|00D0:588C:2401|172\.16.31.5|10\.10.10.2|
|Switch0|0060:2F84:4AB6|00D0:588C:2401|No corresponde|No corresponde|
|**En dispositivo**|**MAC de destino**|**MAC de origen**|**IPv4 de origen**|**IPv4 de destino**|
|Punto de acceso|No corresponde|No corresponde|No corresponde|No corresponde|
|10\.10.10.2|00D0:588C:2401|0060:2 F 84:4 AB6|10\.10.10.2|172\.16.31.5|

**Preguntas**

Responde las siguientes preguntas relacionadas con los datos capturados:

1. ¿Se utilizaron diferentes tipos de cables / medios para conectar dispositivos?
Si, se emplearon los dos diferentes medios existentes: cableado e inalámbrico. 
1. ¿Los cables cambiaron el manejo de la PDU de alguna manera?
No, debido que solo se encargan de transportar los paquetes.
1. ¿El **Hub** perdió parte de la información que recibió?
No, una vez que recibe los paquetes, el Hub envia los datos a todos los dispositivos a los que está conectado.
1. ¿Qué hace el **hub** con las direcciones MAC y las direcciones IP?
No hace nada, pues no tiene la capacidad para distinguir las diferentes direcciones IP y MAC que están conectados a él; el solo reenvia la informacion a todos los puertos.
1. ¿El **punto de acceso** inalámbrico hizo algo con la información que se le entregó?
1. ¿Se perdió alguna dirección MAC o IP durante la transferencia inalámbrica?
No, lo unico que ocurrió fue un cambio de direcciones IP en el router.
1. ¿Cuál fue la capa OSI más alta que utilizaron el **hub** y el **punto de acceso**?
Capa 1
1. ¿El **hub** o el **punto de acceso** reprodujeron en algún momento una PDU rechazada con una “X” de color rojo?
Si, ello debido a que enviaron los paquetes a destinos incorrectos.
1. Al examinar la ficha **PDU Details (Detalles de PDU)**, ¿qué dirección MAC aparecía primero, la de origen o la de destino?
La dirección MAC de destino. 
1. ¿Por qué las direcciones MAC aparecen en este orden?
Porque cuando se envia un paquete de datos, el dispositivo que envia los datos necesita saber cual será la dirección MAC de destino para que envie los datos correctamente. Luego se encuentra la dirección MAC de origen, que servirá para que el receptor emita una respuesta de manera mas rapida, siempre y cuando sea necesaria. 
1. ¿Había un patrón para el direccionamiento MAC en la simulación?
No
1. ¿Los switches reprodujeron en algún momento una PDU rechazada con una “X” de color rojo?
No, ya que estos si pueden identificar la direccion MAC de destino y así enviar los paquetes al dispositivo correcto.
1. Cada vez que se enviaba la PDU entre las redes 10 y 172, había un punto donde las direcciones MAC cambiaban repentinamente. ¿Dónde ocurrió eso?
En el router.
1. ¿Qué dispositivo usa direcciones MAC que comienzan con 00D0: BA?
El router.
1. ¿A qué dispositivos pertenecían las otras direcciones MAC?
Al emisor y al receptor.
16. ¿Las direcciones IPv4 de envío y recepción cambiaron los campos en alguna de las PDU?
Sí.
16. Cuando sigue la respuesta a un ping, a veces llamado *pong*, ¿ve el cambio de envío y recepción de direcciones IPv4?
Sí.
16. ¿Cuál es el patrón para el direccionamiento IPv4 utilizado en esta simulación?
Cada puerto del router requiere un conjunto de direcciones que no se superponga, ello significa que una red requiere un direccionamiento IPv4 diferente a la otra red.
16. ¿Por qué es necesario asignar diferentes redes IP a los diferentes puertos de un router?
Porque precisamente esa es su función: Conectar diferentes redes IP.
16. Si esta simulación se configura con IPv6 en lugar de IPv4, ¿cuál sería la diferencia?
En escala real, los datos se enviarían mucho más rapido debido a que el ancho de banda es mayor.
Comunicación de Datos y Redes

