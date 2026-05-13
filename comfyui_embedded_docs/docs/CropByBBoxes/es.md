> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropByBBoxes/es.md)

El nodo CropByBBoxes extrae y redimensiona regiones rectangulares específicas de un lote de imágenes de entrada. Utiliza las coordenadas de cuadros delimitadores proporcionadas para definir el área a recortar de cada imagen. Las regiones recortadas se redimensionan luego a una dimensión de salida especificada, con opciones para estirar el recorte o rellenarlo para preservar su relación de aspecto original.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `imagen` | IMAGE | Sí | - | El lote de imágenes de entrada a recortar. |
| `cajas delimitadoras` | BOUNDINGBOX | Sí | - | La lista de cuadros delimitadores que definen las regiones a recortar. Esta entrada es forzada, lo que significa que debe estar conectada. |
| `ancho de salida` | INT | No | 64 - 4096 | El ancho al que se redimensiona cada recorte (predeterminado: 512). |
| `alto de salida` | INT | No | 64 - 4096 | La altura a la que se redimensiona cada recorte (predeterminado: 512). |
| `relleno` | INT | No | 0 - 1024 | Relleno adicional en píxeles añadido a cada lado del cuadro delimitador antes de recortar (predeterminado: 0). |
| `mantener_proporción` | COMBO | No | `"stretch"`<br>`"pad"` | Si estirar el recorte para que se ajuste al tamaño de salida, o rellenarlo con píxeles negros para preservar su relación de aspecto (predeterminado: "stretch"). |

**Nota:** El nodo procesa un fotograma de imagen a la vez. Si se proporcionan múltiples cuadros delimitadores para un solo fotograma, calcula una única región de recorte que es la unión (el rectángulo más pequeño que contiene todos los cuadros) de todos los cuadros proporcionados. Si una región de recorte calculada no es válida (por ejemplo, ancho o altura cero), el nodo creará un recorte alternativo desde el centro-superior de la imagen.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `imagen` | IMAGE | Todas las regiones recortadas y redimensionadas, apiladas en un solo lote de imágenes. |

---
**Source fingerprint (SHA-256):** `9c0b3078405567911731c42e1873c57c77363e21ef6805769730667c811b0a0b`
