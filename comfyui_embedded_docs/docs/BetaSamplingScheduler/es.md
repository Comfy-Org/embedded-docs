> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/es.md)

El nodo BetaSamplingScheduler genera una secuencia de niveles de ruido (sigmas) para el proceso de muestreo utilizando un algoritmo de programación beta. Toma un modelo y parámetros de configuración para crear un programa de ruido personalizado que controla el proceso de eliminación de ruido durante la generación de imágenes. Este programador permite ajustar finamente la trayectoria de reducción de ruido a través de los parámetros alfa y beta.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `modelo` | MODEL | Requerido | - | - | El modelo utilizado para el muestreo, que proporciona el objeto de muestreo del modelo |
| `pasos` | INT | Requerido | 20 | 1-10000 | El número de pasos de muestreo para los cuales generar sigmas |
| `alfa` | FLOAT | Requerido | 0.6 | 0.0-50.0 | Parámetro alfa para el programador beta, que controla la curva de programación |
| `beta` | FLOAT | Requerido | 0.6 | 0.0-50.0 | Parámetro beta para el programador beta, que controla la curva de programación |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `SIGMAS` | SIGMAS | Una secuencia de niveles de ruido (sigmas) utilizados para el proceso de muestreo |