> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaImageToVideoNode2_2/es.md)

El nodo Pika Image to Video envía una imagen y un texto de prompt a la API de Pika versión 2.2 para generar un video. Convierte tu imagen de entrada a formato de video basándose en la descripción y configuraciones proporcionadas. El nodo maneja la comunicación con la API y devuelve el video generado como salida.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | IMAGE | Sí | - | La imagen a convertir en video |
| `texto del prompt` | STRING | Sí | - | La descripción textual que guía la generación del video |
| `prompt negativo` | STRING | Sí | - | Texto que describe qué evitar en el video |
| `semilla` | INT | Sí | - | Valor de semilla aleatoria para resultados reproducibles |
| `resolución` | STRING | Sí | - | Configuración de resolución del video de salida |
| `duración` | INT | Sí | - | Duración del video generado en segundos |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado |