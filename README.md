# Ejercicio 1 Practica 2 Procesos y servicios

> Desarrolla una aplicación utilizando python que genere una copia del proceso en ejecución y que tenga el siguiente comportamiento: (5 Puntos)

1. El proceso padre debe preguntar al usuario cuántos procesos hijos debe ejecutar, en función del valor introducido por el usuario, el proceso padre se replicará tantas veces como sea necesario.

2. El proceso hijo debe mostrar su PID, esperar 5 segundos mostrar un mensaje indicando que se va a terminar y acabar su ejecución.

### He utilizado fork para crear procesos hijos y sleep para esperar 5 segundos.
