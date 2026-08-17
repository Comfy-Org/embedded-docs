# CodificarTextoCLIPHunyuanDiT

El nodo `CLIPTextEncodeHunyuanDiT` convierte descripciones de texto en un formato que el modelo HunyuanDiT puede entender. Es un nodo de condicionamiento avanzado diseñado para la arquitectura de doble codificador de texto de HunyuanDiT, que procesa dos entradas de texto separadas mediante diferentes tokenizadores y las combina en una única salida de condicionamiento.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `clip` | Una instancia del modelo CLIP utilizada para la tokenización y codificación de texto, que es fundamental para generar condiciones. | CLIP | Sí | - |
| `bert` | Entrada de texto para codificar mediante el tokenizador BERT. Prefiere frases y palabras clave. Admite múltiples líneas y prompts dinámicos. | STRING | Sí | - |
| `mt5xl` | Entrada de texto para codificar mediante el tokenizador mT5-XL. Admite múltiples líneas y prompts dinámicos (multilingüe). Puede utilizar oraciones completas y descripciones complejas. | STRING | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `CONDITIONING` | La salida de condicionamiento codificada, que combina el texto tokenizado de BERT y mT5-XL, utilizada para el procesamiento posterior en tareas de generación. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHunyuanDiT/es.md)

---
**Source fingerprint (SHA-256):** `550e8c09b8b74974576a852a9b690a87a0156ef49fe7ec1050b10415c6af78aa`
