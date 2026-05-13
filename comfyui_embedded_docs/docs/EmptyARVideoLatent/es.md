> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/es.md)

## Descripción general

El nodo EmptyARVideoLatent crea una representación latente vacía para la generación de video. Se utiliza para inicializar un proceso de generación de video proporcionando un tensor de ceros con las dimensiones, relación de aspecto y longitud especificadas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `width` | INT | Sí | 16 a 8192 (paso: 16) | El ancho de los fotogramas de video en píxeles (predeterminado: 832) |
| `height` | INT | Sí | 16 a 8192 (paso: 16) | La altura de los fotogramas de video en píxeles (predeterminado: 480) |
| `length` | INT | Sí | 1 a 1024 (paso: 4) | El número de fotogramas en el video (predeterminado: 81) |
| `batch_size` | INT | Sí | 1 a 64 | El número de videos a generar en un solo lote (predeterminado: 1) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `LATENT` | LATENT | Un tensor latente lleno de ceros, que representa un espacio latente de video vacío con las dimensiones, longitud y tamaño de lote especificados. La forma del tensor es [batch_size, 16, lat_t, height/8, width/8], donde lat_t se calcula a partir de la longitud. |

---
**Source fingerprint (SHA-256):** `5ae25e2ccb24e627eae583d14c5bcba8b576a227b7a489f3cd4bc56738928513`
