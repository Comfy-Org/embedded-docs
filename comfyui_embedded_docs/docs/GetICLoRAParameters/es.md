# Obtener parámetros IC-LoRA

## Descripción general

Este nodo extrae los parámetros IC-LoRA de los metadatos de un modelo cargado con LoRA. Lee los metadatos de safetensors para encontrar valores como el factor de reducción de escala de referencia y los genera como un objeto de parámetros estructurado, que puede conectarse al nodo LTXVAddGuide para un manejo especial de guías.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `iclora_model` | Salida directa de un cargador LoRA para el IC-LoRA específico del cual extraer los metadatos. | MODEL | Sí | N/A |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `iclora_parameters` | Parámetros IC-LoRA extraídos de los metadatos LoRA (p. ej., factor de reducción de escala de referencia). Conéctelo a LTXVAddGuide si el LoRA requiere un manejo especial de las guías. | IC_LORA_PARAMETERS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/es.md)

---
**Source fingerprint (SHA-256):** `44673f0b06cb258014efd77f734c076865d59338ddf825598d85592f000aca50`
