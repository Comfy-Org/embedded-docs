# EmptyARVideoLatent

El nodo `EmptyARVideoLatent` crea una representación latente vacía y en blanco para la generación de videos. Se utiliza para inicializar un proceso de generación de video proporcionando un tensor de ceros con las dimensiones, la relación de aspecto y la longitud especificadas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `width` | El ancho de los fotogramas del video en píxeles (predeterminado: 832) | INT | Sí | 16 to 8192 (step: 16) |
| `height` | La altura de los fotogramas del video en píxeles (predeterminado: 480) | INT | Sí | 16 to 8192 (step: 16) |
| `length` | El número de fotogramas del video (predeterminado: 81) | INT | Sí | 1 to 1024 (step: 4) |
| `batch_size` | La cantidad de videos a generar en un solo lote (predeterminado: 1) | INT | Sí | 1 to 64 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `LATENT` | Un tensor latente relleno de ceros, que representa un espacio latente de video vacío con las dimensiones, la longitud y el tamaño de lote especificados. La forma del tensor es [batch_size, 16, lat_t, height/8, width/8], donde lat_t se calcula a partir de la longitud. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/es.md)

---
**Source fingerprint (SHA-256):** `02ed3c96d94f2a3df9fb5315a5312e5280b9bee280369eb1218ba10bc122e609`
