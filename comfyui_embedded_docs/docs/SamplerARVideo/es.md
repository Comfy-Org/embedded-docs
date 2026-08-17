# Sampler AR Video

El nodo Sampler AR Video proporciona un método de muestreo especializado para modelos de video autorregresivos, como aquellos que utilizan técnicas de Forzamiento Causal o Auto-Forzamiento. Gestiona todos los parámetros relacionados con el bucle autorregresivo (AR) directamente dentro del flujo de trabajo, lo que facilita la configuración de cómo el modelo genera fotogramas de video paso a paso.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `num_frame_per_block` | Fotogramas por bloque autorregresivo. Un valor de 1 significa que el modelo genera un fotograma a la vez (fotograma por fotograma), mientras que un valor de 3 significa que genera tres fotogramas juntos (por fragmentos). Esta configuración debe coincidir con el modo de entrenamiento del checkpoint. Valor predeterminado: 1. | INT | Sí | 1 a 64 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `SAMPLER` | Un objeto sampler configurado que utiliza la función de muestreo "ar_video" con los parámetros autorregresivos especificados. | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerARVideo/es.md)

---
**Source fingerprint (SHA-256):** `9ec72f52f5b77746f1587e64966bfa6cfd80ce8bb40a4fcb267f5197d09189fc`
