# EmptyARVideoLatent

## Descripción general

El nodo EmptyARVideoLatent crea una representación latente vacía para la generación de video. Se utiliza para inicializar un proceso de generación de video proporcionando un tensor de ceros con las dimensiones, relación de aspecto y longitud especificadas.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `width` | El ancho de los fotogramas de video en píxeles (predeterminado: 832) | INT | Sí | 16 a 8192 (paso: 16) |
| `height` | La altura de los fotogramas de video en píxeles (predeterminado: 480) | INT | Sí | 16 a 8192 (paso: 16) |
| `length` | El número de fotogramas en el video (predeterminado: 81) | INT | Sí | 1 a 1024 (paso: 4) |
| `batch_size` | El número de videos a generar en un solo lote (predeterminado: 1) | INT | Sí | 1 a 64 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `LATENT` | Un tensor latente lleno de ceros, que representa un espacio latente de video vacío con las dimensiones, longitud y tamaño de lote especificados. La forma del tensor es [batch_size, 16, lat_t, height/8, width/8], donde lat_t se calcula a partir de la longitud. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/es.md)

---
**Source fingerprint (SHA-256):** `5ae25e2ccb24e627eae583d14c5bcba8b576a227b7a489f3cd4bc56738928513`
