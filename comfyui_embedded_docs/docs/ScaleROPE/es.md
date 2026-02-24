> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ScaleROPE/es.md)

El nodo ScaleROPE permite modificar el Embedding de Posición Rotacional (ROPE) de un modelo aplicando factores de escalado y desplazamiento separados a sus componentes X, Y y T (tiempo). Es un nodo avanzado y experimental utilizado para ajustar el comportamiento de la codificación posicional del modelo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo cuyos parámetros ROPE serán modificados. |
| `scale_x` | FLOAT | No | 0.0 - 100.0 | El factor de escalado a aplicar al componente X del ROPE (por defecto: 1.0). |
| `shift_x` | FLOAT | No | -256.0 - 256.0 | El valor de desplazamiento a aplicar al componente X del ROPE (por defecto: 0.0). |
| `scale_y` | FLOAT | No | 0.0 - 100.0 | El factor de escalado a aplicar al componente Y del ROPE (por defecto: 1.0). |
| `shift_y` | FLOAT | No | -256.0 - 256.0 | El valor de desplazamiento a aplicar al componente Y del ROPE (por defecto: 0.0). |
| `scale_t` | FLOAT | No | 0.0 - 100.0 | El factor de escalado a aplicar al componente T (tiempo) del ROPE (por defecto: 1.0). |
| `shift_t` | FLOAT | No | -256.0 - 256.0 | El valor de desplazamiento a aplicar al componente T (tiempo) del ROPE (por defecto: 0.0). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo con los nuevos parámetros de escalado y desplazamiento ROPE aplicados. |
