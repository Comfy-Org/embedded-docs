# ComfyCloudFlux2TextToImageNode

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `prompt` | El prompt de texto que describe la imagen a generar. Se eliminan los espacios en blanco al inicio y al final antes del envío. | STRING | Sí | 1 a 4096 caracteres |
| `seed` | Semilla aleatoria que controla el resultado generado para permitir la reproducibilidad (predeterminado: 42). | INT | Sí | 0 a 18446744073709551615 |
| `aspect_ratio` | Relación de aspecto de la imagen de salida (predeterminado: "1:1"). | COMBO | Sí | "1:1"<br>"3:4"<br>"2:3"<br>"3:2"<br>"4:3"<br>"16:9"<br>"9:16"<br>"21:9" |
| `megapixels` | Presupuesto total de píxeles. 1.0 equivale aproximadamente a 1024x1024 en una relación cuadrada (predeterminado: 1.0). | FLOAT | Sí | 0.1 a 16.0 (paso 0.1) |
| `turbo` | Ejecuta el Turbo LoRA con un programa de muestreo corto, sacrificando un poco de fidelidad por una ejecución mucho más rápida. Cuando está desactivado, ejecuta el pase dev completo sin LoRA (predeterminado: True). | BOOLEAN | Sí | True / False |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `IMAGE` | La imagen generada a partir del prompt de texto, devuelta como un tensor de imagen de ComfyUI que puede pasarse a otros nodos. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudFlux2TextToImageNode/es.md)

---
**Source fingerprint (SHA-256):** `1b51a8ab89ae7c355dec4256a1a25a09a15e192c72fc8d1862c652dbdf337fcb`
