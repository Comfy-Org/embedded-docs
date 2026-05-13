> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLoraModelOnly/es.md)

Este nodo crea un hook que aplica un modelo LoRA (Adaptación de Bajo Rango) para modificar únicamente el componente de modelo de una red neuronal. Carga un archivo checkpoint y lo aplica con una intensidad específica al modelo, dejando el componente CLIP sin cambios. Este es un nodo experimental que extiende la funcionalidad de la clase base CreateHookModelAsLora.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|---------------|-----------|-------|-------------|
| `ckpt_name` | STRING | Sí | Múltiples opciones disponibles | El archivo checkpoint a cargar como modelo LoRA. Las opciones disponibles dependen del contenido de la carpeta de checkpoints. |
| `strength_model` | FLOAT | Sí | -20.0 a 20.0 | El multiplicador de intensidad para aplicar la LoRA al componente del modelo (predeterminado: 1.0) |
| `prev_hooks` | HOOKS | No | - | Hooks previos opcionales para encadenar con este hook |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `hooks` | HOOKS | El grupo de hooks creado que contiene la modificación del modelo LoRA |

---
**Source fingerprint (SHA-256):** `adbeaede65aa89d48c59225ca1c8edc4c9394a364f93a00dae4a83a2270f093b`
