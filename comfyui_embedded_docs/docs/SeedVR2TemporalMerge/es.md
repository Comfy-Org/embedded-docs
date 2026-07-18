# SeedVR2TemporalMerge

Este nodo recombina fragmentos temporales de datos de video latente que fueron previamente divididos por el nodo Split SeedVR2 Latent. Utiliza una transición suave con ventana Hann sobre las regiones superpuestas para crear una fusión uniforme entre fragmentos, o realiza una concatenación simple cuando no se especifica superposición.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `latents` | Los fragmentos temporales muestreados en orden secuencial. | LATENT | Sí | Lista de latentes |
| `temporal_overlap` | La salida `temporal_overlap` de Split SeedVR2 Latent. 0 = concatenación simple. | INT | Sí | 0 a 16384 (predeterminado: 0) |

**Nota:** El parámetro `temporal_overlap` debe conectarse desde la salida `temporal_overlap` del nodo Split SeedVR2 Latent. Todos los latentes de entrada deben tener el mismo tamaño de lote, número de canales, altura y anchura. Solo el fragmento final puede tener una dimensión temporal más corta que los demás.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|-------------|-------------|-----------|
| `latent` | El latente recombinado de longitud completa. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalMerge/es.md)

---
**Source fingerprint (SHA-256):** `647653fc651462f62bcc9dca2919cfcaa4b476b4c679b0a1111698facab83f28`
