# EscalarROPE

El nodo ScaleROPE modifica la incrustación posicional rotatoria (ROPE) de un modelo aplicando factores separados de escala y desplazamiento a sus componentes X, Y y T (tiempo). Este es un nodo avanzado y experimental que se utiliza para ajustar el comportamiento de la codificación posicional del modelo.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo cuyos parámetros ROPE serán modificados. | MODEL | Sí | - |
| `scale_x` | El factor de escala que se aplicará al componente X del ROPE (por defecto: 1.0). | FLOAT | Sí | 0.0 - 100.0 (step 0.1) |
| `shift_x` | El valor de desplazamiento que se aplicará al componente X del ROPE (por defecto: 0.0). | FLOAT | Sí | -256.0 - 256.0 (step 0.1) |
| `scale_y` | El factor de escala que se aplicará al componente Y del ROPE (por defecto: 1.0). | FLOAT | Sí | 0.0 - 100.0 (step 0.1) |
| `shift_y` | El valor de desplazamiento que se aplicará al componente Y del ROPE (por defecto: 0.0). | FLOAT | Sí | -256.0 - 256.0 (step 0.1) |
| `scale_t` | El factor de escala que se aplicará al componente T (tiempo) del ROPE (por defecto: 1.0). | FLOAT | Sí | 0.0 - 100.0 (step 0.1) |
| `shift_t` | El valor de desplazamiento que se aplicará al componente T (tiempo) del ROPE (por defecto: 0.0). | FLOAT | Sí | -256.0 - 256.0 (step 0.1) |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `model` | El modelo con los nuevos parámetros de escala y desplazamiento ROPE aplicados. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ScaleROPE/es.md)

---
**Source fingerprint (SHA-256):** `5d5ab0182b78c8c12ceaf44685a91e666ce15fa099fd194e3605bbdb9cc3c961`
