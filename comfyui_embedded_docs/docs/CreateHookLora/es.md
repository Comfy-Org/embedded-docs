> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLora/es.md)

El nodo Create Hook LoRA genera objetos hook para aplicar modificaciones LoRA (Low-Rank Adaptation) a modelos. Carga un archivo LoRA específico y crea hooks que pueden ajustar las intensidades del modelo y CLIP, luego combina estos hooks con cualquier hook existente que se le pase. El nodo gestiona eficientemente la carga de LoRA almacenando en caché los archivos LoRA cargados previamente para evitar operaciones redundantes.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `lora_name` | STRING | Sí | Múltiples opciones disponibles | El nombre del archivo LoRA a cargar desde el directorio loras |
| `strength_model` | FLOAT | Sí | -20.0 a 20.0 | El multiplicador de intensidad para ajustes del modelo (valor por defecto: 1.0) |
| `strength_clip` | FLOAT | Sí | -20.0 a 20.0 | El multiplicador de intensidad para ajustes de CLIP (valor por defecto: 1.0) |
| `prev_hooks` | HOOKS | No | N/A | Grupo de hooks existente opcional para combinar con los nuevos hooks LoRA |

**Restricciones de Parámetros:**
- Si tanto `strength_model` como `strength_clip` se establecen en 0, el nodo omitirá la creación de nuevos hooks LoRA y devolverá los hooks existentes sin cambios
- El nodo almacena en caché el último archivo LoRA cargado para optimizar el rendimiento cuando se usa el mismo LoRA repetidamente

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `HOOKS` | HOOKS | Un grupo de hooks que contiene los hooks LoRA combinados y cualquier hook anterior |