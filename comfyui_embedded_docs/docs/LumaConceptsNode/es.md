> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaConceptsNode/es.md)

Este documento fue generado por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaConceptsNode/en.md)

Almacena uno o más conceptos de cámara para usar con los nodos Luma Texto a Video y Luma Imagen a Video. Este nodo te permite seleccionar hasta cuatro conceptos de cámara y, opcionalmente, combinarlos con cadenas de conceptos existentes.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `concept1` | STRING | Sí | Múltiples opciones disponibles<br>Incluye opción "None" | Primera selección de concepto de cámara de los conceptos Luma disponibles |
| `concept2` | STRING | Sí | Múltiples opciones disponibles<br>Incluye opción "None" | Segunda selección de concepto de cámara de los conceptos Luma disponibles |
| `concept3` | STRING | Sí | Múltiples opciones disponibles<br>Incluye opción "None" | Tercera selección de concepto de cámara de los conceptos Luma disponibles |
| `concept4` | STRING | Sí | Múltiples opciones disponibles<br>Incluye opción "None" | Cuarta selección de concepto de cámara de los conceptos Luma disponibles |
| `luma_concepts` | LUMA_CONCEPTS | No | N/D | Conceptos de cámara opcionales para agregar a los seleccionados aquí |

**Nota:** Todos los parámetros de concepto (`concept1` a `concept4`) se pueden establecer en "None" si no deseas usar los cuatro espacios de concepto. El nodo fusionará cualquier `luma_concepts` proporcionado con los conceptos seleccionados para crear una cadena de conceptos combinada.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `luma_concepts` | LUMA_CONCEPTS | Cadena de conceptos de cámara combinada que contiene todos los conceptos seleccionados |

---
**Source fingerprint (SHA-256):** `d0e334104884eadab86987f188dff079e11ee4a3de05d2537d88fa9d2a30534a`
