<p align="center">
  <img src="../../Images/logo_upch.png">
</p>

**Departamento Académico de Ingeniería C8280 - Comunicación de Datos y Redes**  
---
**Actividad 1: Creación de una red simple** 

Para completar este laboratorio vamos a utilizar Cisco Packet Tracer **Topología** 

<p align="center">
  <img src="image1.png">
</p>

**Tabla de direccionamiento** 



|**Dispositivo** |**Interface** |**Dirección IP** |**Máscara de subred** |
| - | - | - | - |
|PC-A |NIC |192\.168.1.10 |255\.255.255.0 |
|PC-B |NIC |192\.168.1.11 |255\.255.255.0 |

**Objetivos** 

**Parte 1: Configuración de la topología de la red**  

- Identificar los dispositivos de red y construir una red simple con Packet Tracer. 
- Realizar el cableado de una topología de red. 

**Parte 2: Configuración de hosts en las PC** 

- Introducir la información de dirección IP estática en la interfaz LAN de los hosts. 
- Verificar que las PC puedan comunicarse por medio de la utilidad **ping**. 

**Información básica/situación** 

Las redes están formadas por tres componentes principales: hosts, switches y routers. En este laboratorio, armará una red simple con dos hosts y un switch. En esta práctica de laboratorio, aplicará la asignación de direcciones IP a las PC para habilitar la comunicación entre estos dos dispositivos. Use la utilidad **ping** para verificar la conectividad. 

**Nota**: Los switches que se usan son Cisco Catalyst 2960 con Cisco IOS Release 15.0(2) (imagen lanbasek9).  

Se pueden utilizar otros switches y otras versiones de Cisco IOS. 

**Recursos necesarios** 

- 1 switch (Cisco 2960 con Cisco IOS versión 15.0(2), imagen lanbasek9 o similar) 
- 2 PC (Windows 10) 
- cables Ethernet como se muestra en la topología. 

Paso 1: Construye la red simple configurando cada uno de los dispositivos dados. 

1. En la interfaz de Packet Tracer selecciona los dispositivos dados: Switch 2960.  
2. Click en el dispositivo y en la pestaña Config, Display Name, Hostname Cambia el nombre a S1. 
3. Realiza el mismo procedimiento para los otros dispositivos. Llamalos PC-A, PC-B respectivamente.
4. Selecciona el ícono Rayo de conexiones y escoge Copper Straight-Through.  
5. Conecte un extremo de un cable Ethernet al puerto de NIC en PC-A. Conecte el otro extremo del cable a F0/6 en S1. Después de conectar la PC al switch, la luz de F0/6 debería tornarse ámbar y luego verde, lo que indica que la PC-A se conectó correctamente. 
6. Conecte un extremo de un cable Ethernet al puerto de NIC en PC-B. Conecte el otro extremo del cable a F0/1 en S1. Después de conectar la PC al switch, la luz de F0/1 debería tornarse ámbar y luego verde, lo que indica que la PC-B se conectó correctamente. 

Paso 2: Verifique la configuración y la conectividad de la PC. 

Use la línea de comandos para verificar la configuración de la PC y la conectividad. 

1. Desde PC-A, haga clic y Desktop seleccione **Command Prompt**. 
2. En la ventana de comandos de packet tracer, puedes introducir comandos directamente en la PC y ver los resultados de esos comandos. Verifique la configuración de la PC mediante el comando **ipconfig /all**. Este comando muestra información sobre el nombre del host de la PC y la dirección IPv4. 
3. Escriba **ping 192.168.1.11** y presione Intro. 

   ¿Fueron correctos los resultados del ping? 
   
   *No, aparece 100% loss, lo que implica que se perdieron todos los archivos que enviaron.*

4. **Repite los pasos anteriores para PC-B** 

   **¿Fueron correctos los resultados del ping?** 
   
   *Tampoco, ocurrió lo mismo que con la PC-A.*

   **Nota**: Si no obtuvo una respuesta de PC-B, intente hacer ping a PC-B nuevamente. Si sigue sin obtener respuesta de PC-B, intente enviar un comando ping a PC-A desde PC-B.