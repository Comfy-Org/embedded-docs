# CosmosImageToVideoLatent

El nodo CosmosImageToVideoLatent crea representaciones latentes de video a partir de imágenes de entrada. Genera un latente de video en blanco y, opcionalmente, codifica imágenes de inicio y/o final en los primeros y/o últimos fotogramas de la secuencia de video. Cuando se proporcionan imágenes, también crea máscaras de ruido correspondientes para indicar qué partes del latente deben preservarse durante la generación.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `vae` | El modelo VAE utilizado para codificar imágenes en el espacio latente | VAE | Sí | - |
| `ancho` | El ancho del video de salida en píxeles (predeterminado: 1280) | INT | Sí | 16 a MAX_RESOLUTION |
| `altura` | La altura del video de salida en píxeles (predeterminado: 704) | INT | Sí | 16 a MAX_RESOLUTION |
| `longitud` | El número de fotogramas en la secuencia de video (predeterminado: 121) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_lote` | El número de lotes latentes a generar (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `imagen_inicio` | Imagen opcional para codificar al inicio de la secuencia de video | IMAGE | No | - |
| `imagen_final` | Imagen opcional para codificar al final de la secuencia de video | IMAGE | No | - |

**Nota:** Cuando no se proporcionan ni `start_image` ni `end_image`, el nodo devuelve un latente en blanco sin ninguna máscara de ruido. Cuando se proporciona alguna imagen, las secciones correspondientes del latente se codifican y enmascaran según corresponda.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `latent` | La representación latente de video generada con imágenes codificadas opcionales y máscaras de ruido correspondientes | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/es.md)

---
**Source fingerprint (SHA-256):** `31ce4dc577c672e0b3dc0bfb6644b2ef7ab737f6c4ee5e0677973b6a4efdd66d`
