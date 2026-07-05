# Tripo: Multivista a Modelo

Este nodo genera modelos 3D de forma síncrona utilizando la API de Tripo, procesando hasta cuatro imágenes que muestran diferentes vistas de un objeto. Requiere una imagen frontal y al menos una vista adicional (izquierda, trasera o derecha) para crear un modelo 3D completo con opciones de textura y material.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | Imagen de la vista frontal del objeto (obligatoria) | IMAGE | Sí | - |
| `imagen_izquierda` | Imagen de la vista izquierda del objeto | IMAGE | No | - |
| `imagen_posterior` | Imagen de la vista trasera del objeto | IMAGE | No | - |
| `imagen_derecha` | Imagen de la vista derecha del objeto | IMAGE | No | - |
| `versión_del_modelo` | Versión del modelo a utilizar para la generación | COMBO | No | Múltiples opciones disponibles |
| `orientación` | Configuración de orientación para el modelo 3D (predeterminado: "default") | COMBO | No | Múltiples opciones disponibles |
| `textura` | Si se deben generar texturas para el modelo (predeterminado: True) | BOOLEAN | No | - |
| `pbr` | Si se deben generar materiales PBR (renderizado basado en física) (predeterminado: True) | BOOLEAN | No | - |
| `semilla_del_modelo` | Semilla aleatoria para la generación del modelo (predeterminado: 42) | INT | No | - |
| `semilla_de_textura` | Semilla aleatoria para la generación de texturas (predeterminado: 42) | INT | No | - |
| `calidad_de_textura` | Nivel de calidad para la generación de texturas (predeterminado: "standard") | COMBO | No | `"standard"`<br>`"detailed"` |
| `alineación_de_textura` | Método para alinear texturas al modelo (predeterminado: "original_image") | COMBO | No | `"original_image"`<br>`"geometry"` |
| `límite_de_caras` | Número máximo de caras en el modelo generado. Establecer en -1 para sin límite (predeterminado: -1) | INT | No | -1 a 500000 |
| `cuadrilátero` | Este parámetro está obsoleto y no tiene efecto (predeterminado: False) | BOOLEAN | No | - |
| `geometry_quality` | Nivel de calidad para la generación de geometría (predeterminado: "standard") | COMBO | No | `"standard"`<br>`"detailed"` |

**Nota:** La imagen frontal (`image`) siempre es obligatoria. Se debe proporcionar al menos una imagen de vista adicional (`image_left`, `image_back` o `image_right`) para el procesamiento multivista.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `archivo_de_modelo` | Ruta de archivo o identificador del modelo 3D generado (solo para compatibilidad hacia atrás) | STRING |
| `id_de_tarea_de_modelo` | Identificador de tarea para rastrear el proceso de generación del modelo | MODEL_TASK_ID |
| `GLB` | Archivo del modelo 3D generado en formato GLB | FILE3DGLB |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `4ad433f4a0060d0ac2ce14463497db3168a1bf3348f17b98e958409e9a63baaf`
