El nodo `CLIPTextEncodeHunyuanDiT` convierte descripciones de texto en un formato que el modelo HunyuanDiT puede entender. Es un nodo de condicionamiento avanzado diseñado para la arquitectura de doble codificador de texto de HunyuanDiT, procesando dos entradas de texto separadas a través de diferentes tokenizadores.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `clip` | Una instancia del modelo CLIP utilizada para la tokenización y codificación de texto, esencial para generar condiciones. | CLIP | Sí | - |
| `bert` | Entrada de texto para codificar mediante el tokenizador BERT. Prefiere frases y palabras clave. Admite múltiples líneas y avisos dinámicos. | STRING | Sí | - |
| `mt5xl` | Entrada de texto para codificar mediante el tokenizador mT5-XL. Admite múltiples líneas y avisos dinámicos (multilingüe). Puede usar oraciones completas y descripciones complejas. | STRING | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `CONDITIONING` | La salida de condicionamiento codificada, que combina el texto tokenizado tanto de BERT como de mT5-XL, utilizada para procesamiento posterior en tareas de generación. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHunyuanDiT/es.md)

---
**Source fingerprint (SHA-256):** `6a8d649708b315c42b7933b52fad7e0b45aa34c168616f18a2178041148eeea1`
