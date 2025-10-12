> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Sketch/es.md)

Este nodo genera recursos 3D utilizando la API de Rodin. Toma imágenes de entrada y las convierte en modelos 3D a través de un servicio externo. El nodo maneja todo el proceso desde la creación de la tarea hasta la descarga de los archivos finales del modelo 3D.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `Images` | IMAGE | Sí | - | Imágenes de entrada que se convertirán en modelos 3D |
| `Seed` | INT | No | 0-65535 | Valor de semilla aleatoria para la generación (por defecto: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `3D Model Path` | STRING | Ruta del archivo del modelo 3D generado |
