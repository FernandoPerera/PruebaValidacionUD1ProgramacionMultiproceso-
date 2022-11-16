
## **~ Prueba de validación UD1 Programación multiproceso**

<br/>

#### **- | Introducción al proyecto |**

<br/>

- Tenemos que lograr generar 10 procesos, uno cada 10 segundos y mostrar un mensaje con el **PID** y la hora en la que inicia.

- Cada proceso hijo mostrará un mensaje al iniciar con su **PID**, y luego de esperar 3 segundos matar al proceso y mostrar otro mensaje
con el **PID**

#### **- | Gestión de ramas |**

<br/>

Creo la rama **development** donde iremos añadiendo las nuevas funcionalidades creadas en las rama **process**, y finalmente mergearlo todo al **main**.

<br/>

#### **- | Desarrollo de las ramas |**

<br/>

> main

- Mergearemos el código terminado desde **<code>development</code>** para pushearlo al origin.

<br/>

> development

- Mergeamos el código con la funcionalidad añadida desde **<code>process</code>** , y realizamos la documentación por medio
de un **<code>Readme.md</code>** 

> process

<br/>

- Realizamos la funcionalidad solicitada en el proyecto, por medio de dos funciones : 

<br/>

- - **<code>father()</code>** : En esta función iremos generando los 10 procesos solicitados, usando un bucle y un contador y mediante el uso de **<code>os.fork()</code>** para la creación de cada proceso. Si la salida de este el igual a 0 significará que nos encontramos en el proceso hijo por lo que llamaremos a la función **<code>children()</code>**, sino mostraremos el **PID** del hijo y la hora a la que inició dando uso de la clase **<code>datetime</code>**, obteniendo la fecha actual con el método **<code>.now()</code>** y luego aplicarle un **<code>format</code>** para conseguir la hora acual.

<br/>

- - **<code>children()</code>** : Lo que haremos en esta función será mostrar un mensaje con el **PID** del hijo y luego, mediante la función **<code>sleep()</code>** de la clase **<code>time</code>**, le diremos al programa que espere 3 segundos para matar al proceso usando **<code>os._exit(0)</code>** y mostrar un mensaje indicandolo con su **PID**

<br/>

#### **- | Conclusión del proyecto |**

<br/>

En mi opinión, en este proyecto hemos aprendido como crear procesos en pyhton y a matarlos en el tiempo solicitado, además del uso de diversos modulos como **<code>os</code>**, **<code>time</code>**, **<code>datetime</code>**.
