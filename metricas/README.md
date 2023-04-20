# Metricas

Este paquete contiene los nodos de los procesos que se han de realizar una vez finalizada la exploración. Entre ellos se encuentran los siguientes nodos:

- **`Terrorista`**. Se encarga de guardar el mapa una vez la exploracion ha finalizado y se recibe un mensaje por el `topic_publisher` o como se llame. Los mapas se guardan en la carpeta Maps.
- **`toHome`**. Se encargará de enviar al robot al `(0,0)` de su odometría una vez terminada la exploración.
- **`Metricas`**. Se encarga de computar la métricas del tio random de github.
- **`InserteMierdaAquí`**. Cualquier cosa que se te ocurra, si lo necesitas, hasta te abraza.