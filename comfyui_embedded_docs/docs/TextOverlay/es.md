# Superponer texto

Este nodo dibuja texto sobre una imagen o un lote de imágenes. Crea una superposición de texto con tamaño de fuente, color, posición, alineación y un contorno opcional personalizables, y luego compone el texto sobre las imágenes originales.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `imágenes` | La imagen o lote de imágenes de entrada sobre las que dibujar el texto | IMAGE | Sí | |
| `texto` | El texto a superponer en la imagen (predeterminado: "") | STRING | Sí | |
| `tamaño de fuente` | Tamaño de fuente como porcentaje de la altura de la imagen (predeterminado: 5.0) | FLOAT | Sí | 0.5 a 50.0 |
| `color` | Color del texto (predeterminado: "#ffffff") | STRING | Sí | |
| `posición` | Posición vertical del texto en la imagen (predeterminado: "top") | COMBO | Sí | `"top"`<br>`"bottom"` |
| `alineación` | Alineación horizontal del texto (predeterminado: "left") | COMBO | Sí | `"left"`<br>`"center"`<br>`"right"` |
| `contorno` | Dibujar un contorno negro alrededor del texto (predeterminado: True) | BOOLEAN | Sí | |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `imágenes` | Las imágenes de entrada con la superposición de texto compuesta encima | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextOverlay/es.md)

---
**Source fingerprint (SHA-256):** `baffaa4ec9d3565e3533673658399271234def8c49e2e4a5f16767ec3f98cb22`
