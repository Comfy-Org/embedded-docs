# Resumen

Genera respuestas de texto a partir de un modelo Anthropic Claude. Este nodo envía un mensaje de texto e imágenes opcionales a un modelo Claude y devuelve la respuesta de texto generada.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Entrada de texto para el modelo. (valor predeterminado: cadena vacía) | STRING | Sí | N/A |
| `model` | El modelo Claude utilizado para generar la respuesta. | COMBO | Sí | `"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` |
| `seed` | La semilla controla si el nodo debe re-ejecutarse; los resultados no son deterministas independientemente de la semilla. (valor predeterminado: 0) | INT | Sí | 0 a 2147483647 |
| `images` | Imagen(es) opcional(es) para usar como contexto del modelo. Hasta 20 imágenes. | IMAGE | No | 0 a 20 imágenes |
| `system_prompt` | Instrucciones fundamentales que determinan el comportamiento del modelo. (valor predeterminado: cadena vacía) | STRING | No | N/A |

### Restricciones de Parámetros

- **Límite de Imágenes**: Se puede proporcionar un máximo de 20 imágenes por solicitud.
- **Manejo de Temperatura**: Cuando el pensamiento está habilitado o al usar el modelo "Opus 4.7", el parámetro de temperatura se desactiva automáticamente (valor predeterminado 1.0) según lo requiere la API de Anthropic. Para otros modelos, la temperatura se puede configurar mediante la configuración del modelo.
- **Pensamiento/Razonamiento**: La configuración del modelo incluye un ajuste `reasoning_effort` que controla si el pensamiento está habilitado. Cuando está habilitado, el nodo configura automáticamente el modo de pensamiento apropiado (adaptativo o basado en presupuesto) dependiendo del modelo seleccionado.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | La respuesta de texto generada por el modelo Claude. Devuelve "Respuesta vacía del modelo Claude." si no se genera texto. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/es.md)

---
**Source fingerprint (SHA-256):** `e3bab004535d4d406582aa42f28bb64a2988f8331788d51ec1fa4e943d8d4382`
