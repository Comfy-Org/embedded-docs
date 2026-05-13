> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawVideoEnhance/es.md)

El nodo HitPaw Video Enhance utiliza una API externa para mejorar la calidad de los videos. Escala videos de baja resolución a una resolución más alta, elimina artefactos visuales y reduce el ruido. El costo del procesamiento se calcula por segundo del video de entrada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | DYNAMIC COMBO | Sí | Múltiples opciones disponibles | El modelo de IA a utilizar para la mejora del video. Al seleccionar un modelo, se muestra un parámetro `resolution` anidado. Los modelos disponibles y sus resoluciones compatibles varían. |
| `model.resolution` | COMBO | Sí | `"original"`<br>`"720p"`<br>`"1080p"`<br>`"2k/qhd"`<br>`"4k/uhd"`<br>`"8k"` | La resolución objetivo para el video mejorado. Algunas opciones pueden no estar disponibles según el `model` seleccionado. |
| `video` | VIDEO | Sí | N/A | El archivo de video de entrada que se va a mejorar. |

**Restricciones:**

* El `video` de entrada debe tener una duración entre 0.5 segundos y 60 minutos (3600 segundos).
* La `resolution` seleccionada debe ser mayor que las dimensiones del video de entrada. Si el video es cuadrado, la resolución seleccionada debe ser mayor que su ancho/alto. Para videos no cuadrados, la resolución seleccionada debe ser mayor que la dimensión más corta del video. Si la resolución objetivo es menor, se generará un error. Seleccione `"original"` para mantener la resolución del video de entrada.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `video` | VIDEO | El archivo de video mejorado. |

---
**Source fingerprint (SHA-256):** `0f329cbf61784474ee5b97a92d28a3e2383dc40e208f8a8317f3c4f60b43e5b2`
