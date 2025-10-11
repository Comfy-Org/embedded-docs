> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimVideoLatent/es.md)

El nodo TrimVideoLatent elimina fotogramas del inicio de una representación latente de video. Toma una muestra de video latente y recorta un número específico de fotogramas desde el comienzo, devolviendo la porción restante del video. Esto permite acortar secuencias de video eliminando los fotogramas iniciales.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Sí | - | La representación latente de video de entrada que contiene los fotogramas a recortar |
| `trim_amount` | INT | No | 0 a 99999 | El número de fotogramas a eliminar desde el inicio del video (valor predeterminado: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | LATENT | La representación latente de video recortada con el número especificado de fotogramas eliminados desde el inicio |