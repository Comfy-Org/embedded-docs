El nodo TrimVideoLatent elimina fotogramas del inicio de una representación latente de video. Toma una muestra de video latente y recorta un número específico de fotogramas desde el principio, devolviendo la porción restante del video. Esto permite acortar secuencias de video eliminando los fotogramas iniciales.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `muestras` | La representación latente de video de entrada que contiene los fotogramas de video a recortar | LATENT | Sí | - |
| `cantidad_de_recorte` | El número de fotogramas a eliminar desde el inicio del video (predeterminado: 0) | INT | Sí | 0 a 99999 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | La representación latente de video recortada con el número especificado de fotogramas eliminados desde el inicio | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimVideoLatent/es.md)

---
**Source fingerprint (SHA-256):** `7fd482533d1f63219565a3a25776173c77c419fbf5086015d42136f5bfdfbed2`
