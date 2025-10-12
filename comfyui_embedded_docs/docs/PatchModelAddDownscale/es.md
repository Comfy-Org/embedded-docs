> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/es.md)

El nodo PatchModelAddDownscale implementa la funcionalidad Kohya Deep Shrink aplicando operaciones de reducción y aumento de escala a bloques específicos en un modelo. Reduce la resolución de las características intermedias durante el procesamiento y luego las restaura a su tamaño original, lo que puede mejorar el rendimiento manteniendo la calidad. El nodo permite un control preciso sobre cuándo y cómo ocurren estas operaciones de escalado durante la ejecución del modelo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo al que se aplicará el parche de reducción de escala |
| `numero_de_bloque` | INT | No | 1-32 | El número de bloque específico donde se aplicará la reducción de escala (predeterminado: 3) |
| `factor_de_reducción` | FLOAT | No | 0.1-9.0 | El factor por el cual reducir la escala de las características (predeterminado: 2.0) |
| `porcentaje_inicial` | FLOAT | No | 0.0-1.0 | El punto de inicio en el proceso de eliminación de ruido donde comienza la reducción de escala (predeterminado: 0.0) |
| `porcentaje_final` | FLOAT | No | 0.0-1.0 | El punto final en el proceso de eliminación de ruido donde se detiene la reducción de escala (predeterminado: 0.35) |
| `reducción_después_de_omitir` | BOOLEAN | No | - | Si aplicar la reducción de escala después de las conexiones de salto (predeterminado: True) |
| `método_de_reducción` | COMBO | No | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | El método de interpolación utilizado para las operaciones de reducción de escala |
| `método_de_ampliación` | COMBO | No | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | El método de interpolación utilizado para las operaciones de aumento de escala |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `modelo` | MODEL | El modelo modificado con el parche de reducción de escala aplicado |
