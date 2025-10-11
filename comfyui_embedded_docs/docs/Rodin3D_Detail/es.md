> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Detail/es.md)

El nodo Rodin 3D Detail genera activos 3D detallados utilizando la API de Rodin. Toma imágenes de entrada y las procesa a través del servicio Rodin para crear modelos 3D de alta calidad con geometría y materiales detallados. El nodo maneja todo el flujo de trabajo desde la creación de la tarea hasta la descarga del archivo final del modelo 3D.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | Sí | - | Imágenes de entrada utilizadas para la generación del modelo 3D |
| `Seed` | INT | Sí | - | Valor de semilla aleatoria para resultados reproducibles |
| `Material_Type` | STRING | Sí | - | Tipo de material a aplicar al modelo 3D |
| `Polygon_count` | STRING | Sí | - | Cantidad objetivo de polígonos para el modelo 3D generado |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | Ruta del archivo al modelo 3D generado |