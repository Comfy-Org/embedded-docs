# SamplerLCMUpscale

El nodo SamplerLCMUpscale proporciona un método de muestreo especializado que combina el muestreo del Modelo de Consistencia Latente (LCM) con capacidades de ampliación de imagen. Permite ampliar imágenes durante el proceso de muestreo utilizando varios métodos de interpolación, lo que resulta útil para generar salidas de mayor resolución manteniendo la calidad de la imagen. La ampliación se aplica gradualmente a lo largo de los pasos de muestreo hasta alcanzar el `scale_ratio` objetivo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `scale_ratio` | El factor de escala que se aplica durante la ampliación (por defecto: 1.0) | FLOAT | No | 0.1 - 20.0 |
| `scale_steps` | El número de pasos a utilizar para el proceso de ampliación. Usa -1 para el cálculo automático (por defecto: -1) | INT | No | -1 - 1000 |
| `upscale_method` | El método de interpolación utilizado para ampliar la imagen (por defecto: bislerp) | COMBO | Sí | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

Nota: cuando `scale_steps` se establece en un valor positivo, el número efectivo de pasos de ampliación está limitado por el número total de pasos de muestreo del sampler.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `sampler` | Devuelve un objeto sampler configurado que puede utilizarse en el pipeline de muestreo | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/es.md)

---
**Source fingerprint (SHA-256):** `5d6f6472fbb4d2c66a8a8b9d6dc34dcc52ac8272589fd6c29e4084d6cab3141b`
