# Obtener parámetros IC-LoRA

## Resumen

Este nodo extrae los parámetros IC-LoRA de los metadatos de un modelo cargado con LoRA. Lee los metadatos de safetensors para encontrar valores como el factor de reducción de escala de referencia y los emite como un objeto de parámetros estructurado, que puede conectarse al nodo LTXVAddGuide para el manejo especial de guías. Si los metadatos faltan o no se puede leer el factor de reducción de escala de referencia, el valor predeterminado es 1; cuando se encuentra, el valor se redondea y se limita a un mínimo de 1.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `iclora_model` | Salida directa de un cargador de LoRA para el IC-LoRA específico del cual se extraen los metadatos. | MODEL | Sí | N/A |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `iclora_parameters` | Parámetros IC-LoRA extraídos de los metadatos de LoRA (p. ej., reference_downscale_factor). Conéctelo a LTXVAddGuide si el LoRA requiere un manejo especial de las guías. | IC_LORA_PARAMETERS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/es.md)

---
**Source fingerprint (SHA-256):** `5f6becad0c7673b8cde1e099bd7ba5be7106da958b8967f8e693ba2a704baaef`
