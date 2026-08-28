# SamplerLCMUpscale

El nodo SamplerLCMUpscale proporciona un método de muestreo especializado que combina el muestreo del Modelo de Consistencia Latente (LCM) con capacidades de ampliación de imagen. Amplía la imagen progresivamente durante el proceso de muestreo utilizando varios métodos de interpolación, lo que permite generar salidas de mayor resolución en una sola pasada de muestreo. La salida es un objeto de muestreador configurado que se puede conectar a un nodo de muestreo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `relación_escala` | El factor de escala total que se aplicará durante la ampliación. Un valor de 1.0 mantiene la resolución original (valor predeterminado: 1.0) | FLOAT | Sí | 0.1 - 20.0 |
| `pasos_escala` | El número de pasos que se utilizarán para el proceso de ampliación. Use -1 para el cálculo automático basado en la programación de muestreo (valor predeterminado: -1) | INT | Sí | -1 - 1000 |
| `método_aumento_escala` | El método de interpolación utilizado para ampliar la imagen en cada paso de ampliación (valor predeterminado: "bislerp") | COMBO | Sí | "bislerp"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bicubic" |

`scale_ratio` y `scale_steps` son parámetros avanzados. La imagen se amplía gradualmente desde su tamaño original hasta el `scale_ratio` objetivo a lo largo de los pasos de ampliación. Cuando `scale_steps` es -1, el número de pasos de ampliación se calcula automáticamente como aproximadamente la mitad del número de pasos de muestreo, con un mínimo de 2; cuando se proporciona un valor positivo, el nodo lo ajusta internamente y lo limita según el número total de pasos de muestreo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `sampler` | Un objeto de muestreador configurado que realiza el muestreo LCM con ampliación progresiva, listo para utilizarse en el flujo de muestreo | SAMPLER |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCMUpscale/es.md)

---
**Source fingerprint (SHA-256):** `5d6f6472fbb4d2c66a8a8b9d6dc34dcc52ac8272589fd6c29e4084d6cab3141b`
