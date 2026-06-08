# Ampliación Creativa de Estabilidad (Stability Upscale Creative)

Amplía imágenes con alteraciones mínimas a resolución 4K. Este nodo utiliza la tecnología de ampliación creativa de Stability AI para mejorar la resolución de la imagen mientras preserva el contenido original y añade detalles creativos sutiles.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | La imagen de entrada que se ampliará | IMAGE | Sí | - |
| `prompt` | Lo que deseas ver en la imagen de salida. Un prompt fuerte y descriptivo que defina claramente elementos, colores y sujetos generará mejores resultados. (predeterminado: cadena vacía) | STRING | Sí | - |
| `creatividad` | Controla la probabilidad de crear detalles adicionales no fuertemente condicionados por la imagen inicial. (predeterminado: 0.3) | FLOAT | Sí | 0.1-0.5 |
| `estilo predefinido` | Estilo deseado opcional de la imagen generada. (predeterminado: "None") | STRING | Sí | `"3d-model"`<br>`"analog-film"`<br>`"anime"`<br>`"cinematic"`<br>`"comic-book"`<br>`"digital-art"`<br>`"enhance"`<br>`"fantasy-art"`<br>`"isometric"`<br>`"line-art"`<br>`"low-poly"`<br>`"modeling-compound"`<br>`"neon-punk"`<br>`"origami"`<br>`"photographic"`<br>`"pixel-art"`<br>`"tile-texture"` |
| `semilla` | La semilla aleatoria utilizada para crear el ruido. (predeterminado: 0) | INT | Sí | 0-4294967294 |
| `prompt negativo` | Palabras clave de lo que NO deseas ver en la imagen de salida. Esta es una función avanzada. (predeterminado: cadena vacía) | STRING | No | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `imagen` | La imagen ampliada a resolución 4K | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleCreativeNode/es.md)

---
**Source fingerprint (SHA-256):** `46f7bdd3cb4254b6305407f43e4a9a69a54fd3a0ac285d784c899dbf52edd552`
