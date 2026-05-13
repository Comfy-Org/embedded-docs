> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypassModelOnly/es.md)

Este nodo aplica una LoRA (Adaptación de Bajo Rango) a un modelo para modificar su comportamiento, pero solo afecta al componente del modelo en sí. Carga un archivo LoRA específico y ajusta los pesos del modelo según una intensidad determinada, dejando sin cambios otros componentes como el codificador de texto CLIP.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo base al que se aplicarán los ajustes de LoRA. |
| `lora_name` | STRING | Sí | (Lista de archivos LoRA disponibles) | El nombre del archivo LoRA a cargar y aplicar. Las opciones se obtienen de los archivos en el directorio `loras`. |
| `strength_model` | FLOAT | Sí | -100.0 a 100.0 | La intensidad del efecto de LoRA sobre los pesos del modelo. Un valor positivo aplica la LoRA, un valor negativo aplica la inversa y un valor de 0 no tiene efecto (valor predeterminado: 1.0). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `model` | MODEL | El modelo modificado con los ajustes de LoRA aplicados a sus pesos. |

---
**Source fingerprint (SHA-256):** `e0e1ad2d6481a1b9771d7eae833ffab0737a967d4af6e57b946d1b2223fe45bf`
