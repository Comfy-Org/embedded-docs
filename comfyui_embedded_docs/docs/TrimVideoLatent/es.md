# TrimVideoLatent

El nodo TrimVideoLatent elimina fotogramas del inicio de una representación latente de video. Toma una muestra de video latente y recorta un número específico de fotogramas desde el principio, devolviendo la parte restante del video. Esto permite acortar secuencias de video eliminando los fotogramas iniciales.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `samples` | La representación latente de video de entrada que contiene los fotogramas de video a recortar | LATENT | Sí | - |
| `trim_amount` | El número de fotogramas a eliminar desde el inicio del video (predeterminado: 0) | INT | Sí | 0 a 99999 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | La representación latente de video recortada con el número especificado de fotogramas eliminados desde el inicio | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimVideoLatent/es.md)

---
**Source fingerprint (SHA-256):** `33b7a899f2002e9a7008f2ca93de853c08dd0629a4c6867fb42aae4ec2eb864b`
