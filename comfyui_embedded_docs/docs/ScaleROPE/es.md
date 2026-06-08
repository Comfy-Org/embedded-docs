El nodo ScaleROPE permite modificar la Codificación Posicional Rotatoria (ROPE) de un modelo aplicando factores de escala y desplazamiento independientes a sus componentes X, Y y T (tiempo). Este es un nodo experimental avanzado utilizado para ajustar el comportamiento de la codificación posicional del modelo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo cuyos parámetros ROPE serán modificados. | MODEL | Sí | - |
| `escala_x` | Factor de escala a aplicar al componente X del ROPE (predeterminado: 1.0). | FLOAT | No | 0.0 - 100.0 |
| `desplazamiento_x` | Valor de desplazamiento a aplicar al componente X del ROPE (predeterminado: 0.0). | FLOAT | No | -256.0 - 256.0 |
| `escala_y` | Factor de escala a aplicar al componente Y del ROPE (predeterminado: 1.0). | FLOAT | No | 0.0 - 100.0 |
| `desplazamiento_y` | Valor de desplazamiento a aplicar al componente Y del ROPE (predeterminado: 0.0). | FLOAT | No | -256.0 - 256.0 |
| `escala_t` | Factor de escala a aplicar al componente T (tiempo) del ROPE (predeterminado: 1.0). | FLOAT | No | 0.0 - 100.0 |
| `desplazamiento_t` | Valor de desplazamiento a aplicar al componente T (tiempo) del ROPE (predeterminado: 0.0). | FLOAT | No | -256.0 - 256.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `modelo` | El modelo con los nuevos parámetros de escala y desplazamiento ROPE aplicados. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ScaleROPE/es.md)

---
**Source fingerprint (SHA-256):** `c5ca193a46faa9477a2e6c99b905205685e8add8faa2f2d161c7c384b3dc2441`
