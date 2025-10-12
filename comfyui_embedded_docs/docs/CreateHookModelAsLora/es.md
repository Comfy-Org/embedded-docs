> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLora/es.md)

Este nodo crea un modelo de enlace como LoRA (Adaptación de Bajo Rango) cargando pesos de checkpoint y aplicando ajustes de intensidad tanto a los componentes del modelo como a CLIP. Permite aplicar modificaciones estilo LoRA a modelos existentes mediante un enfoque basado en enlaces, posibilitando el ajuste fino y la adaptación sin cambios permanentes en el modelo. El nodo puede combinarse con enlaces anteriores y almacena en caché los pesos cargados para mayor eficiencia.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `ckpt_name` | COMBO | Sí | Múltiples opciones disponibles | El archivo checkpoint desde el cual cargar los pesos (seleccionar entre los checkpoints disponibles) |
| `strength_model` | FLOAT | Sí | -20.0 a 20.0 | El multiplicador de intensidad aplicado a los pesos del modelo (valor por defecto: 1.0) |
| `strength_clip` | FLOAT | Sí | -20.0 a 20.0 | El multiplicador de intensidad aplicado a los pesos de CLIP (valor por defecto: 1.0) |
| `prev_hooks` | HOOKS | No | - | Enlaces anteriores opcionales para combinar con los nuevos enlaces LoRA creados |

**Restricciones de Parámetros:**

- El parámetro `ckpt_name` carga checkpoints desde la carpeta de checkpoints disponibles
- Ambos parámetros de intensidad aceptan valores de -20.0 a 20.0 con incrementos de 0.01
- Cuando no se proporciona `prev_hooks`, el nodo crea un nuevo grupo de enlaces
- El nodo almacena en caché los pesos cargados para evitar recargar el mismo checkpoint múltiples veces

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `HOOKS` | HOOKS | Los enlaces LoRA creados, combinados con cualquier enlace anterior si se proporcionó |
