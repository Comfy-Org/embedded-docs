> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLoraModelOnly/es.md)

Este nodo crea un gancho LoRA (Adaptación de Bajo Rango) que se aplica únicamente al componente del modelo, permitiéndole modificar el comportamiento del modelo sin afectar el componente CLIP. Carga un archivo LoRA y lo aplica con una fuerza específica al modelo mientras mantiene el componente CLIP sin cambios. El nodo puede encadenarse con ganchos previos para crear pipelines de modificación complejos.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `lora_name` | STRING | Sí | Múltiples opciones disponibles | El nombre del archivo LoRA a cargar desde la carpeta loras |
| `strength_model` | FLOAT | Sí | -20.0 a 20.0 | El multiplicador de fuerza para aplicar el LoRA al componente del modelo (por defecto: 1.0) |
| `prev_hooks` | HOOKS | No | - | Ganchos previos opcionales para encadenar con este gancho |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `hooks` | HOOKS | El gancho LoRA creado que puede aplicarse al procesamiento del modelo |