> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLoraModelOnly/es.md)

Este nodo crea un hook que aplica un modelo LoRA (Low-Rank Adaptation) para modificar únicamente el componente modelo de una red neuronal. Carga un archivo de checkpoint y lo aplica con una fuerza específica al modelo, dejando el componente CLIP sin cambios. Este es un nodo experimental que extiende la funcionalidad de la clase base CreateHookModelAsLora.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `ckpt_name` | STRING | Sí | Múltiples opciones disponibles | El archivo de checkpoint a cargar como modelo LoRA. Las opciones disponibles dependen del contenido de la carpeta de checkpoints. |
| `strength_model` | FLOAT | Sí | -20.0 a 20.0 | El multiplicador de fuerza para aplicar el LoRA al componente modelo (por defecto: 1.0) |
| `prev_hooks` | HOOKS | No | - | Hooks anteriores opcionales para encadenar con este hook |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `hooks` | HOOKS | El grupo de hooks creado que contiene la modificación del modelo LoRA |