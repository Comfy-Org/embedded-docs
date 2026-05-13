> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeKandinsky5/es.md)

El nodo CLIPTextEncodeKandinsky5 prepara indicaciones de texto para su uso con el modelo Kandinsky 5. Toma dos entradas de texto separadas, las tokeniza utilizando un modelo CLIP proporcionado y las combina en una única salida de condicionamiento. Esta salida se utiliza para guiar el proceso de generación de imágenes.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `clip` | CLIP | Sí | | El modelo CLIP utilizado para tokenizar y codificar las indicaciones de texto. |
| `clip_l` | STRING | Sí | | La indicación de texto principal. Esta entrada admite texto multilínea e indicaciones dinámicas. |
| `qwen25_7b` | STRING | Sí | | Una indicación de texto secundaria. Esta entrada admite texto multilínea e indicaciones dinámicas. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Los datos de condicionamiento combinados generados a partir de ambas indicaciones de texto, listos para ser introducidos en un modelo Kandinsky 5 para la generación de imágenes. |

---
**Source fingerprint (SHA-256):** `80227cf87d46bfa42b07976ab29996ae9583a4c461b2f2408db4b7016d3e1a0c`
