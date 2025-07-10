Este nodo está específicamente diseñado para el modelo SDXL Refiner para convertir indicaciones textuales en información de acondicionamiento mediante la incorporación de puntuaciones estéticas e información dimensional para mejorar las condiciones de las tareas de generación, mejorando así el efecto de refinamiento final. Actúa como un director de arte profesional, no solo transmitiendo tu intención creativa sino también inyectando estándares estéticos precisos y requisitos de especificación en el trabajo.

## Acerca de SDXL Refiner

SDXL Refiner es un modelo de refinamiento especializado que se centra en mejorar los detalles y la calidad de la imagen basándose en el modelo base SDXL. Este proceso es como tener un retocador de arte:

1. Primero, recibe imágenes preliminares o descripciones textuales generadas por el modelo base
2. Luego, guía el proceso de refinamiento a través de puntuación estética precisa y parámetros dimensionales
3. Finalmente, se centra en procesar detalles de imagen de alta frecuencia para mejorar la calidad general

El Refiner se puede usar de dos maneras:

- Como un paso de refinamiento independiente para el post-procesamiento de imágenes generadas por el modelo base
- Como parte de un sistema de integración experto, tomando el control del procesamiento durante la fase de bajo ruido de la generación

## Entradas

| Nombre del Parámetro | Data Type | Tipo de Entrada | Valor Predeterminado | Rango de Valores | Descripción |
|----------------------|-----------|-----------------|---------------------|------------------|-------------|
| `clip` | CLIP | Requerido | - | - | Instancia del modelo CLIP utilizada para la tokenización y codificación de texto, el componente central para convertir texto en formato comprensible para el modelo |
| `ascore` | FLOAT | Opcional | 6.0 | 0.0-1000.0 | Controla la calidad visual y la estética de las imágenes generadas, similar a establecer estándares de calidad para obras de arte:<br/>- Puntuaciones altas(7.5-8.5): Busca efectos más refinados y ricos en detalles<br/>- Puntuaciones medias(6.0-7.0): Control de calidad equilibrado<br/>- Puntuaciones bajas(2.0-3.0): Adecuado para indicaciones negativas |
| `width` | INT | Requerido | 1024 | 64-16384 | Especifica el ancho de la imagen de salida (píxeles), debe ser múltiplo de 8. SDXL funciona mejor cuando el recuento total de píxeles está cerca de 1024×1024 (aproximadamente 1M píxeles) |
| `height` | INT | Requerido | 1024 | 64-16384 | Especifica la altura de la imagen de salida (píxeles), debe ser múltiplo de 8. SDXL funciona mejor cuando el recuento total de píxeles está cerca de 1024×1024 (aproximadamente 1M píxeles) |
| `text` | STRING | Requerido | - | - | Descripción de la indicación de texto, admite entrada multilínea y sintaxis de indicación dinámica. En Refiner, las indicaciones de texto deben centrarse más en describir la calidad visual deseada y las características de detalle |

## Salidas

| Nombre de Salida | Data Type | Descripción |
|------------------|-----------|-------------|
| `ACONDICIONAMIENTO` | CONDITIONING | Salida condicional refinada que contiene codificación integrada de semántica textual, estándares estéticos e información dimensional, específicamente para guiar al modelo SDXL Refiner en el refinamiento preciso de imágenes |

## Notas

1. Este nodo está específicamente optimizado para el modelo SDXL Refiner y difiere de los nodos CLIPTextEncode regulares
2. Se recomienda una puntuación estética de 7.5 como línea base, que es la configuración estándar utilizada en el entrenamiento de SDXL
3. Todos los parámetros dimensionales deben ser múltiplos de 8, y se recomienda un recuento total de píxeles cercano a 1024×1024 (aproximadamente 1M píxeles)
4. El modelo Refiner se centra en mejorar los detalles y la calidad de la imagen, por lo que las indicaciones de texto deben enfatizar los efectos visuales deseados en lugar del contenido de la escena
5. En el uso práctico, Refiner se utiliza típicamente en las últimas etapas de generación (aproximadamente el último 20% de los pasos), centrándose en la optimización de detalles
