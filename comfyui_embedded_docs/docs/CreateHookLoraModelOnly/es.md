> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLoraModelOnly/es.md)

Este nodo crea un hook LoRA (Adaptación de Bajo Rango) que se aplica únicamente al componente del modelo, dejando el componente CLIP completamente sin cambios. Carga un archivo LoRA y lo aplica con una intensidad específica al modelo, mientras establece la intensidad CLIP en cero. El nodo puede encadenarse con hooks anteriores para construir pipelines de modificación complejas.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `lora_name` | STRING | Sí | Múltiples opciones disponibles | El nombre del archivo LoRA a cargar desde la carpeta loras |
| `strength_model` | FLOAT | Sí | -20.0 a 20.0 | El multiplicador de intensidad para aplicar el LoRA al componente del modelo (predeterminado: 1.0) |
| `prev_hooks` | HOOKS | No | - | Hooks anteriores opcionales para encadenar con este hook |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `hooks` | HOOKS | El hook LoRA creado que puede aplicarse al procesamiento del modelo |

---
**Source fingerprint (SHA-256):** `10adbdfc2e37fcf317e93130f87d9a7038d00b091cb6d1b45f4658c81632ef80`
