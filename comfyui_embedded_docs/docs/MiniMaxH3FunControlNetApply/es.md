# MiniMaxH3FunControlNetApply

Este nodo aplica un ControlNet MiniMax H3 Fun a un modelo de texto a video como un parche de modelo. Puede usar un video de control opcional y una máscara opcional para guiar la generación, y devuelve una copia parcheada del modelo para su posterior muestreo. Cuando `strength` se establece en 0, o cuando no se proporciona ni un video de control ni una máscara, el modelo de entrada se devuelve sin cambios.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `model` | El modelo de difusión al que se aplica el parche MiniMax H3 Fun ControlNet. | MODEL | Sí | N/A |
| `model_patch` | El parche MiniMax H3 Fun ControlNet cuyas señales de control se inyectan en el modelo; debe ser compatible con el `model` proporcionado. | MODEL_PATCH | Sí | N/A |
| `vae` | VAE utilizado para codificar los fotogramas del video de control y del video fuente en el espacio latente esperado por el modelo. | VAE | Sí | N/A |
| `strength` | Fuerza general del efecto ControlNet. Cuando se establece en 0, el nodo no hace nada y devuelve el modelo de entrada sin cambios. (por defecto: 1.0) | FLOAT | Sí | min 0.0, max 10.0, step 0.01 |
| `start_percent` | Inicio del rango de muestreo, expresado como un porcentaje del programa de muestreo, durante el cual el ControlNet está activo. Internamente se convierte al valor sigma equivalente. (por defecto: 0.0) | FLOAT | Sí | min 0.0, max 1.0, step 0.001 |
| `end_percent` | Fin del rango de muestreo, expresado como un porcentaje del programa de muestreo, durante el cual el ControlNet está activo. Internamente se convierte al valor sigma equivalente. (por defecto: 1.0) | FLOAT | Sí | min 0.0, max 1.0, step 0.001 |
| `control_video` | Fotogramas de video opcionales utilizados como indicación visual del ControlNet. Los fotogramas se redimensionan para coincidir con el video generado y se codifican con el `vae`. | IMAGE | No | N/A |
| `mask` | 1 marca las regiones a regenerar. Los valores de la máscara superiores a 0.5 se tratan como regiones marcadas. | MASK | No | N/A |
| `source_video` | Video detrás de la máscara; solo se lee cuando se proporciona una máscara. | IMAGE | No | N/A |

Nota: Para que el parche tenga efecto, `strength` debe ser mayor que 0 y debe suministrarse al menos uno de `control_video` o `mask`. `source_video` se ignora a menos que se proporcione `mask`; si se proporciona `mask` sin `source_video`, el contenido detrás de las regiones enmascaradas se trata como negro.

## Salidas

| Nombre de salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `model` | Un clon parcheado del modelo de entrada con el MiniMax H3 Fun ControlNet aplicado. Si `strength` es 0, o no se suministra ningún video de control o máscara, el modelo original se devuelve sin cambios. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3FunControlNetApply/es.md)

---
**Source fingerprint (SHA-256):** `e907fb8e5ae60663d1d10b315985695ee5d49397fef6bd76b0e723637457a74a`
