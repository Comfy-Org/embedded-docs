> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/es.md)

Este nodo genera modelos 3D de forma síncrona utilizando la API de Tripo, procesando hasta cuatro imágenes que muestran diferentes vistas de un objeto. Requiere una imagen frontal y al menos una vista adicional (izquierda, trasera o derecha) para crear un modelo 3D completo con opciones de textura y material.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `imagen` | IMAGE | Sí | - | Imagen de la vista frontal del objeto (obligatoria) |
| `imagen_izquierda` | IMAGE | No | - | Imagen de la vista izquierda del objeto |
| `imagen_posterior` | IMAGE | No | - | Imagen de la vista trasera del objeto |
| `imagen_derecha` | IMAGE | No | - | Imagen de la vista derecha del objeto |
| `versión_del_modelo` | COMBO | No | Múltiples opciones disponibles | Versión del modelo a utilizar para la generación |
| `orientación` | COMBO | No | Múltiples opciones disponibles | Configuración de orientación para el modelo 3D (predeterminado: "default") |
| `textura` | BOOLEAN | No | - | Si se deben generar texturas para el modelo (predeterminado: True) |
| `pbr` | BOOLEAN | No | - | Si se deben generar materiales PBR (renderizado basado en física) (predeterminado: True) |
| `semilla_del_modelo` | INT | No | - | Semilla aleatoria para la generación del modelo (predeterminado: 42) |
| `semilla_de_textura` | INT | No | - | Semilla aleatoria para la generación de texturas (predeterminado: 42) |
| `calidad_de_textura` | COMBO | No | `"standard"`<br>`"detailed"` | Nivel de calidad para la generación de texturas (predeterminado: "standard") |
| `alineación_de_textura` | COMBO | No | `"original_image"`<br>`"geometry"` | Método para alinear texturas al modelo (predeterminado: "original_image") |
| `límite_de_caras` | INT | No | -1 a 500000 | Número máximo de caras en el modelo generado. Establecer en -1 para sin límite (predeterminado: -1) |
| `cuadrilátero` | BOOLEAN | No | - | Este parámetro está obsoleto y no tiene efecto (predeterminado: False) |
| `geometry_quality` | COMBO | No | `"standard"`<br>`"detailed"` | Nivel de calidad para la generación de geometría (predeterminado: "standard") |

**Nota:** La imagen frontal (`image`) siempre es obligatoria. Se debe proporcionar al menos una imagen de vista adicional (`image_left`, `image_back` o `image_right`) para el procesamiento multivista.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `id_de_tarea_de_modelo` | STRING | Ruta de archivo o identificador del modelo 3D generado (solo para compatibilidad hacia atrás) |
| `GLB` | MODEL_TASK_ID | Identificador de tarea para rastrear el proceso de generación del modelo |
| `GLB` | FILE3DGLB | Archivo del modelo 3D generado en formato GLB |

---
**Source fingerprint (SHA-256):** `4ad433f4a0060d0ac2ce14463497db3168a1bf3348f17b98e958409e9a63baaf`
