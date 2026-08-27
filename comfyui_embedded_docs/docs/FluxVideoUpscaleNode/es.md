# FluxVideoUpscaleNode

Flux Video Upscale amplía un clip de video de 1.5 a 3 veces mediante la superresolución de FLUX. En el modo creativo restaura e inventa detalles finos; en el modo preciso nitifica el origen sin modificarlo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `video` | Clip de origen de 1 a 20 segundos con una relación de aspecto entre 1:4 y 4:1. La salida se renderiza a 24 fps y tiene un límite de aproximadamente 14.4 megapíxeles por fotograma. | VIDEO | Sí | Duración de 1 a 20 segundos; relación de aspecto entre 1:4 y 4:1; mínimo de 64x64 píxeles |
| `upscale_factor` | Tamaño de salida en relación con el origen. Los orígenes muy grandes se amplían a una escala menor que el factor solicitado debido al límite por fotograma. (predeterminado: 2.0) | FLOAT | Sí | 1.5 a 3.0 (paso 0.1) |
| `mode` | El modo 'creative' restaura e inventa detalles finos, ideal para material generado, texturas y paisajes. El modo 'precise' nitifica el origen sin modificarlo, para rostros, productos y metraje real. (predeterminado: "creative") | COMBO | Sí | "creative"<br>"precise" |
| `prompt` | Descripción opcional del clip que orienta el detalle mejorado. Déjela vacía para una ampliación neutra. (predeterminado: vacío) | STRING | Sí | Texto multilínea |
| `auto_downscale` | Reduce automáticamente la escala de los orígenes cuya área supere los 3840x2160 píxeles para ajustarse al límite de entrada. Se conserva la relación de aspecto; los videos más pequeños no se modifican. (predeterminado: true) | BOOLEAN | Sí | true<br>false |
| `safety_tolerance` | Tolerancia de moderación; 0 es la más estricta. (predeterminado: 2, parámetro avanzado) | INT | Sí | 0 a 4 |
| `seed` | Semilla para determinar si el nodo debe volver a ejecutarse; FLUX elige su propia semilla, por lo que los resultados reales son no deterministas independientemente de este valor. (predeterminado: 42) | INT | Sí | 0 a 4294967295 |

Nota: El video de origen debe durar entre 1 y 20 segundos y tener un tamaño mínimo de 64x64 píxeles. Si `auto_downscale` está deshabilitado y el área del video supera los 3840x2160 píxeles, el nodo genera un error. El video de salida se renderiza a 24 fps y tiene un límite de aproximadamente 14.4 megapíxeles por fotograma, por lo que los orígenes muy grandes pueden ampliarse a una escala menor que el factor solicitado.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El clip de video ampliado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoUpscaleNode/es.md)

---
**Source fingerprint (SHA-256):** `22dcf7c176705ce21a9032b1c9f4fe82ee6aa153f5057b90dac653b37281a677`
