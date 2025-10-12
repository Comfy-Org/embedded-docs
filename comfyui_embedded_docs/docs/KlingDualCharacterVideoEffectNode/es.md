> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingDualCharacterVideoEffectNode/es.md)

El nodo Kling Dual Character Video Effect crea videos con efectos especiales basados en la escena seleccionada. Toma dos imágenes y posiciona la primera imagen en el lado izquierdo y la segunda imagen en el lado derecho del video compuesto. Se aplican diferentes efectos visuales dependiendo de la escena de efecto elegida.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen_izquierda` | IMAGE | Sí | - | Imagen del lado izquierdo |
| `imagen_derecha` | IMAGE | Sí | - | Imagen del lado derecho |
| `effect_scene` | COMBO | Sí | Múltiples opciones disponibles | El tipo de escena de efecto especial a aplicar en la generación del video |
| `model_name` | COMBO | No | Múltiples opciones disponibles | El modelo a utilizar para los efectos de personaje (valor por defecto: "kling-v1") |
| `modo` | COMBO | No | Múltiples opciones disponibles | El modo de generación de video (valor por defecto: "std") |
| `duración` | COMBO | Sí | Múltiples opciones disponibles | La duración del video generado |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `duración` | VIDEO | El video generado con efectos de doble personaje |
| `duración` | STRING | La información de duración del video generado |