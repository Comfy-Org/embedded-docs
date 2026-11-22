# Crear Hook LoRA

El nodo **Create Hook LoRA** genera objetos de hook para aplicar modificaciones LoRA (Adaptación de Bajo Rango) a modelos. Carga un archivo LoRA específico y crea hooks que pueden ajustar las intensidades del modelo y CLIP, luego combina estos hooks con cualquier hook existente que se le pase. El nodo gestiona eficientemente la carga de LoRA almacenando en caché los archivos LoRA previamente cargados para evitar operaciones redundantes.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `nombre_de_lora` | Nombre del archivo LoRA a cargar desde el directorio de loras | STRING | Sí | Múltiples opciones disponibles |
| `fuerza_del_modelo` | Multiplicador de intensidad para ajustes del modelo (predeterminado: 1.0) | FLOAT | Sí | -20.0 a 20.0 |
| `fuerza_del_clip` | Multiplicador de intensidad para ajustes CLIP (predeterminado: 1.0) | FLOAT | Sí | -20.0 a 20.0 |
| `ganchos_anteriores` | Grupo opcional de hooks existentes para combinar con los nuevos hooks LoRA | HOOKS | No | N/A |

**Restricciones de parámetros:**

- Si tanto `strength_model` como `strength_clip` se establecen en 0, el nodo omitirá la creación de nuevos hooks LoRA y devolverá los hooks existentes sin cambios
- El nodo almacena en caché el último archivo LoRA cargado para optimizar el rendimiento cuando se usa el mismo LoRA repetidamente

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `HOOKS` | Grupo de hooks que contiene los hooks LoRA combinados y cualquier hook anterior | HOOKS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLora/es.md)

---
**Source fingerprint (SHA-256):** `42d5d776bfc9b239191952e2bce23513d183f904fc3c15039469381a547486f8`
