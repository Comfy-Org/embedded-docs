> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Smooth/es.md)

El nodo **Rodin 3D Smooth** genera activos 3D utilizando la API de Rodin, procesando imágenes de entrada y convirtiéndolas en modelos 3D suaves. Toma múltiples imágenes como entrada y produce un archivo de modelo 3D descargable. El nodo maneja todo el proceso de generación, incluyendo la creación de tareas, la verificación periódica del estado y la descarga automática de archivos.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `Imágenes` | IMAGE | Sí | - | Imágenes de entrada para usar en la generación del modelo 3D. Se pueden proporcionar múltiples imágenes. |
| `Semilla` | INT | Sí | - | Valor de semilla aleatoria para la consistencia de la generación. |
| `Tipo_de_Material` | STRING | Sí | - | Tipo de material que se aplicará al modelo 3D. |
| `Recuento_de_Polígonos` | STRING | Sí | - | Número objetivo de polígonos para el modelo 3D generado. Determina la calidad de la malla y el nivel de detalle. |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `GLB` | STRING | Ruta del archivo al modelo 3D descargado (solo para compatibilidad con versiones anteriores). |
| `GLB` | FILE3DGLB | El modelo 3D generado en formato GLB. |

---
**Source fingerprint (SHA-256):** `18783d4a3010234a3640d20c73cdd78e35a0eef7090bd433dba0fcc58e35ad3f`
