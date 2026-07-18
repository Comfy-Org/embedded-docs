# Superponer texto

Este nodo dibuja texto sobre una imagen o un lote de imágenes. Es compatible con texto personalizado, tamaño de fuente, color, posición, alineación y un contorno opcional, componiendo el texto sobre la imagen original.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `imágenes` | La imagen o lote de imágenes de entrada sobre las que se dibujará el texto. | IMAGE | Sí | |
| `texto` | La cadena de texto a superponer. Admite caracteres de nueva línea (`\n`) y tabulación (`\t`). Valor predeterminado: "" | STRING | Sí | |
| `tamaño de fuente` | Tamaño de la fuente como porcentaje de la altura de la imagen. Valor predeterminado: 5.0 | FLOAT | Sí | 0.5 a 50.0 |
| `color` | Color del texto. Valor predeterminado: "#ffffff" (blanco) | STRING | Sí | |
| `posición` | Posición vertical del texto sobre la imagen. Valor predeterminado: "top" | COMBO | Sí | "top"<br>"bottom" |
| `alineación` | Alineación horizontal del texto. Valor predeterminado: "left" | COMBO | Sí | "left"<br>"center"<br>"right" |
| `contorno` | Dibujar un contorno negro alrededor del texto. Valor predeterminado: Verdadero | BOOLEAN | Sí | |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `imágenes` | La imagen o lote de imágenes con la superposición de texto compuesta sobre ellas. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextOverlay/es.md)

---
**Source fingerprint (SHA-256):** `baffaa4ec9d3565e3533673658399271234def8c49e2e4a5f16767ec3f98cb22`
