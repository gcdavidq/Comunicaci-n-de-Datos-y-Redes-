<p align="center">
  <img src="../../Images/logo_upch.png">
</p>

**Departamento Académico de Ingeniería C8280 - Comunicación de Datos y Redes**  
---

## **Actividad 8: Comunicaciones de TCP y UDP**

**Objetivos**

- **Parte 1: Generar tráfico de red en el modo de simulación** 

- **Parte 2: Examinar la funcionalidad de los protocolos TCP y UDP**

**Aspectos básicos**

Esta actividad de simulación está destinada a proporcionar una base para comprender TCP y UDP en detalle. El modo de simulación Packet Tracer le proporciona la capacidad de ver el estado de diferentes PDU a medida que viajan a través de la red.

El modo de simulación de Packet Tracer te permite ver cada uno de los protocolos y las PDU asociadas. Los pasos descritos a continuación lo guían a través del proceso de solicitud de servicios
de red utilizando diversas aplicaciones que están disponibles en una PC cliente. Explorarás la funcionalidad de los protocolos TCP y UDP, la multiplexación y la función de los números de puerto para determinar qué aplicación local solicitó los datos o los envía.

**Instrucciones**

### **1. Genera tráfico de red en modo de simulación y vea multiplexación**

#### **Genera tráfico para completar las tablas del protocolo de resolución de direcciones (ARP)**
Realiza la siguiente tarea para reducir la cantidad de tráfico de red que se ve en la simulación.
a. Haz clic en MultiServer y luego haz click en Desktop tab > Command Prompt.
b. Ingresa el comando ping -n 1 192.168.1.255 . Está haciendo ping a la dirección broadcast de
la LAN del cliente. La opción de comando enviará sólo una solicitud de ping en lugar de las
cuatro habituales. Esto tomará unos segundos ya que cada dispositivo en la red responde a
la solicitud de ping de MultiServer.
c. Cierra la ventana MultiServer.

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


