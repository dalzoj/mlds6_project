# Project Charter

## Antecedentes Empresariales

* **Ámbito Empresarial**: Salud
* **Cliente**: Hospital Colombiano
* **Objetivo**: Diagnosticar muestras de sangre

## Alcance
Dada una muestra de datos de donantes de sangre, brindar modelos de Inteligencia Artificial (Machine Learning), los cuales nos permitan diagnosticar muestras de pacientes con la enfermedad Hepatitis C.

## PErsonal
* Machine Learning Engineer
* Data Scientist
* Data Engineer
	
## Métricas
* Clasificación de muestras de sangre
* Reducir al menor un 50% el diagnóstico en pruebas personas con Hepatitis C
* El modelo será evaluado con la medida más pequeña de Generalización. También se tendrá en cuentra la Efectividad y el Error de dicho modelo.

## Fases
Se implementará la metodología Team Data Science Process (TDSP)
1. Conocimiento del negocio
2. Adquisición y comprensión de los datos
3. Modelado
4. Implementación
5. Aceptación del cliente
6. Despliegue

## Arquitectura
* **Datos**: Los datos están almacenando en un archivo .csv que se extrae de muestras de la base de datos del hospital
* **Herramientas**:
  * Python
  * Pandas
  * Numpy
  * Matplotlib
  * Sklearn
* How will the score or operationalized web service(s) (RRS and/or BES) be consumed in the business workflow of the customer? If applicable, write down pseudo code for the APIs of the web service calls.
  * How will the customer use the model results to make decisions
  * Data movement pipeline in production
  * Make a 1 slide diagram showing the end to end data flow and decision architecture
    * If there is a substantial change in the customer's business workflow, make a before/after diagram showing the data flow.

## Comunicación
* La comunicación se hará en reuniones cada 2 días con evidencia en los avances del proceso según el rol que corresponda con los integrantes.
* Existe un lider (Data Scientist) que tendrá comunicación directa con el encargado del Hospital en caso de Requerimientos, Avances y Entregas.