# Vista Previa de Muestreo TripoSplat

Este nodo parchea un modelo TripoSplat para que, al usarse con el nodo KSampler estándar, se muestre una vista previa en vivo del splat de gaussianos decodificado en cada paso de muestreo. Funciona envolviendo la llamada de retorno (callback) del muestreador para decodificar la salida del modelo en una imagen de vista previa después de cada paso.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `model` | El modelo TripoSplat a parchear para la vista previa en vivo | MODEL | Sí | |
| `vae` | Decodificador VAE de TripoSplat | VAE | Sí | |
| `octree_level` | Profundidad del octree para la decodificación de la vista previa (menor = más económico/rugoso). Valor por defecto: 5 | INT | No | 2 to 8 |
| `num_gaussians` | Número de gaussianos a generar para la vista previa (redondeado a un múltiplo de 32). Valor por defecto: 16384 | INT | No | 1024 to 262144 (step: 32) |
| `yaw` | Ángulo de guiñada (yaw) de la cámara de vista previa en grados. Valor por defecto: 90.0 | FLOAT | No | -360.0 to 360.0 (step: 1.0) |
| `pitch` | Ángulo de cabeceo (pitch) de la cámara de vista previa en grados. Valor por defecto: 15.0 | FLOAT | No | -89.0 to 89.0 (step: 1.0) |
| `point_size` | Radio máximo del splat en píxeles. Cada gaussiano se dimensiona según su escala y se limita aquí; menor = más fino/puntiagudo, mayor = más grueso. Valor por defecto: 3 | INT | No | 1 to 16 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `MODEL` | El modelo TripoSplat parcheado con la funcionalidad de vista previa en vivo integrada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatSamplingPreview/es.md)

---
**Source fingerprint (SHA-256):** `78678b65df325da964cfd3e8cd0dc07fa25b92d26bb2057117db413a205e9535`
