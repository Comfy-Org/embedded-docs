# SeedVR2TemporalMerge

Este nodo recombina fragmentos temporales latentes muestreados de SeedVR2 en un único latente de longitud completa. Utiliza una transición suave con ventana Hann sobre la región de superposición entre fragmentos para crear transiciones uniformes, o realiza una concatenación simple cuando no se especifica superposición.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `latents` | Los fragmentos temporales muestreados en orden secuencial. | LATENT | Sí | Lista de latentes |
| `temporal_overlap` | La salida `temporal_overlap` de Dividir Latente SeedVR2. 0 = concatenación simple. (valor predeterminado: 0) | INT | Sí | 0 a 16384 |

**Nota:** El valor de `temporal_overlap` debe ser mayor o igual a 0. El último fragmento de la secuencia puede tener menos fotogramas temporales que los demás fragmentos. Todos los fragmentos deben tener dimensiones coincidentes excepto en el eje temporal (T), y el primer fragmento debe ser pentadimensional (B, C, T, H, W).

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `latent` | El latente recompuesto de longitud completa. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalMerge/es.md)

---
**Source fingerprint (SHA-256):** `647653fc651462f62bcc9dca2919cfcaa4b476b4c679b0a1111698facab83f28`
