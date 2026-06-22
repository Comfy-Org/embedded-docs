# TextEncodeBooguEdit

Este nodo prepara el condicionamiento para la edición de imágenes con Boogu. Procesa imágenes de referencia para generar salidas de condicionamiento tanto positivas como negativas. La imagen de referencia se utiliza dos veces: los tokens visuales de la imagen se añaden solo al condicionamiento positivo para amplificar la instrucción de edición, mientras que un latente de referencia del VAE se añade tanto al condicionamiento positivo como al negativo para que se anulen bajo CFG, preservando la identidad de la imagen original.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `clip` | El modelo CLIP utilizado para la codificación de texto | CLIP | Sí | |
| `prompt` | El prompt de texto que describe la edición deseada | STRING | Sí | |
| `negative_prompt` | El prompt de texto que describe lo que se debe evitar en la edición | STRING | No | |
| `vae` | El modelo VAE utilizado para codificar imágenes de referencia en el espacio latente | VAE | No | |
| `imágenes` | Imagen(es) de referencia a editar. Boogu se enfoca en una referencia por muestra; se permiten más. | IMAGE | No | Hasta 16 imágenes |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `negativo` | Condicionamiento que contiene tanto el prompt de texto con tokens visuales como los latentes de referencia | CONDITIONING |
| `negative` | Condicionamiento que contiene el prompt de texto negativo y los latentes de referencia | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeBooguEdit/es.md)

---
**Source fingerprint (SHA-256):** `170979acf5b2e9f25f96231a4b23a4376cfddcd4bda2fdd6e03528417e6931b0`
