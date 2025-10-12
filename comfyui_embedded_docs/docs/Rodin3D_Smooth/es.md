> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Smooth/es.md)

El nodo Rodin 3D Smooth genera activos 3D utilizando la API de Rodin procesando imágenes de entrada y convirtiéndolas en modelos 3D suavizados. Toma múltiples imágenes como entrada y produce un archivo de modelo 3D descargable. El nodo maneja automáticamente todo el proceso de generación, incluyendo la creación de tareas, el sondeo de estado y la descarga de archivos.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | Sí | - | Imágenes de entrada para usar en la generación del modelo 3D |
| `Seed` | INT | Sí | - | Valor de semilla aleatoria para consistencia en la generación |
| `Material_Type` | STRING | Sí | - | Tipo de material a aplicar al modelo 3D |
| `Polygon_count` | STRING | Sí | - | Cantidad objetivo de polígonos para el modelo 3D generado |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | Ruta del archivo al modelo 3D descargado |
