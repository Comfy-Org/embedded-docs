> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Detail/es.md)

El nodo **Rodin 3D Detail** genera activos 3D detallados utilizando la API de Rodin. Toma imágenes de entrada y las procesa a través del servicio Rodin para crear modelos 3D de alta calidad con geometría y materiales detallados. El nodo gestiona todo el flujo de trabajo, desde la creación de la tarea hasta la descarga del archivo final del modelo 3D.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `Imágenes` | IMAGE | Sí | - | Imágenes de entrada utilizadas para la generación del modelo 3D. Se pueden proporcionar múltiples imágenes. |
| `Semilla` | INT | Sí | - | Valor de semilla aleatoria para obtener resultados reproducibles |
| `Tipo_Material` | STRING | Sí | - | Tipo de material que se aplicará al modelo 3D |
| `Recuento_Polígonos` | STRING | Sí | - | Cantidad objetivo de polígonos para el modelo 3D generado. Determina el nivel de calidad de la malla. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `GLB` | STRING | Ruta del archivo al modelo 3D generado (solo para compatibilidad hacia atrás) |
| `GLB` | FILE3DGLB | El modelo 3D generado en formato GLB |

---
**Source fingerprint (SHA-256):** `ed9ed2c8a55ca80d18da88ee2703c66057a09beeac7163fc270d81a492417b0a`
