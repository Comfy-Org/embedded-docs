> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ThresholdMask/es.md)

El nodo ThresholdMask convierte una máscara en una máscara binaria aplicando un valor de umbral. Compara cada píxel en la máscara de entrada con el valor de umbral especificado y crea una nueva máscara donde los píxeles por encima del umbral se convierten en 1 (blanco) y los píxeles por debajo o iguales al umbral se convierten en 0 (negro).

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `máscara` | MASK | Sí | - | La máscara de entrada a procesar |
| `valor` | FLOAT | Sí | 0.0 - 1.0 | El valor de umbral para la binarización (valor por defecto: 0.5) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `máscara` | MASK | La máscara binaria resultante después del umbralizado |
