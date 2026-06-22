# ByteDance Seedream 4.5 & 5.0

Este nodo genera o edita imágenes utilizando los modelos Seedream de ByteDance (versiones 4.0, 4.5 y 5.0 Lite). Puede crear nuevas imágenes a partir de un texto descriptivo o editar imágenes existentes proporcionando imágenes de referencia, con soporte para resoluciones de hasta 4K.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Texto descriptivo para crear o editar una imagen. | STRING | Sí | N/A |
| `modelo` | Versión del modelo Seedream a utilizar para la generación. Cada modelo tiene diferentes capacidades y precios. | COMBO | Sí | `"seedream 5.0 lite"`<br>`"seedream-4-5-251128"`<br>`"seedream-4-0-250828"` |
| `semilla` | Semilla para la generación (predeterminado: 0). | INT | No | 0 a 2147483647 |
| `marca de agua` | Si se debe añadir una marca de agua "Generado por IA" a la imagen (predeterminado: Falso). | BOOLEAN | No | Verdadero / Falso |

### Parámetros Específicos del Modelo

Al seleccionar un modelo, estarán disponibles parámetros adicionales:

- **Predefinido de Tamaño**: Un menú desplegable para seleccionar una resolución de imagen predefinida (ej., "2048x2048", "1024x1024"). Los predefinidos disponibles dependen del modelo seleccionado.
- **Ancho**: El ancho de la imagen generada en píxeles (predeterminado: 2048).
- **Alto**: El alto de la imagen generada en píxeles (predeterminado: 2048).
- **Máximo de Imágenes**: El número máximo de imágenes a generar (predeterminado: 1). Cuando se establece en 1, la generación secuencial de imágenes está desactivada.
- **Imágenes de Referencia**: Hasta 10 (para Seedream 4.0 y 4.5) o 14 (para Seedream 5.0 Lite) imágenes de referencia para edición. Las imágenes deben tener una relación de aspecto entre 1:3 y 3:1.
- **Fallar en Parcial**: Si está habilitado, el nodo generará un error si no todas las imágenes solicitadas se generan correctamente (predeterminado: Falso).

### Restricciones de Resolución

- **Seedream 5.0 Lite y 4.5**: La resolución mínima es de 3.68 megapíxeles (ej., 1920x1920).
- **Seedream 4.0**: La resolución mínima es de 0.92 megapíxeles (ej., 960x960).
- **Todos los modelos**: La resolución máxima es de 16.78 megapíxeles (ej., 4096x4096).

### Restricciones de Cantidad de Imágenes

- El número total de imágenes de referencia más las imágenes generadas no puede exceder 15.
- Para Seedream 5.0 Lite, se admiten un máximo de 14 imágenes de referencia.
- Para Seedream 4.0 y 4.5, se admiten un máximo de 10 imágenes de referencia.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `image` | La imagen generada o editada como un tensor. Si se solicitaron múltiples imágenes, se concatenan en un solo lote. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/es.md)

---
**Source fingerprint (SHA-256):** `1ceccfdb773807a993c32af22703da155367b67865338c78f153a8ccb02dcc8f`
