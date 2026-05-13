> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleCreativeNode/es.md)

# Ampliación Creativa de Estabilidad (Stability Upscale Creative)

Amplía imágenes con alteraciones mínimas a resolución 4K. Este nodo utiliza la tecnología de ampliación creativa de Stability AI para mejorar la resolución de la imagen mientras preserva el contenido original y añade detalles creativos sutiles.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se ampliará |
| `prompt` | STRING | Sí | - | Lo que deseas ver en la imagen de salida. Un prompt fuerte y descriptivo que defina claramente elementos, colores y sujetos generará mejores resultados. (predeterminado: cadena vacía) |
| `creativity` | FLOAT | Sí | 0.1-0.5 | Controla la probabilidad de crear detalles adicionales no fuertemente condicionados por la imagen inicial. (predeterminado: 0.3) |
| `style_preset` | STRING | Sí | `"3d-model"`<br>`"analog-film"`<br>`"anime"`<br>`"cinematic"`<br>`"comic-book"`<br>`"digital-art"`<br>`"enhance"`<br>`"fantasy-art"`<br>`"isometric"`<br>`"line-art"`<br>`"low-poly"`<br>`"modeling-compound"`<br>`"neon-punk"`<br>`"origami"`<br>`"photographic"`<br>`"pixel-art"`<br>`"tile-texture"` | Estilo deseado opcional de la imagen generada. (predeterminado: "None") |
| `seed` | INT | Sí | 0-4294967294 | La semilla aleatoria utilizada para crear el ruido. (predeterminado: 0) |
| `negative_prompt` | STRING | No | - | Palabras clave de lo que NO deseas ver en la imagen de salida. Esta es una función avanzada. (predeterminado: cadena vacía) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `image` | IMAGE | La imagen ampliada a resolución 4K |

---
**Source fingerprint (SHA-256):** `46f7bdd3cb4254b6305407f43e4a9a69a54fd3a0ac285d784c899dbf52edd552`
