> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageOutput/es.md)

El nodo LoadImageOutput carga imágenes desde la carpeta de salida. Al hacer clic en el botón de actualización, se actualiza la lista de imágenes disponibles y se selecciona automáticamente la primera, facilitando la iteración a través de tus imágenes generadas.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | COMBO | Sí | Múltiples opciones disponibles | Carga una imagen desde la carpeta de salida. Incluye una opción de carga y un botón de actualización para actualizar la lista de imágenes. |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `imagen` | IMAGE | La imagen cargada desde la carpeta de salida |
| `mask` | MASK | La máscara asociada con la imagen cargada |
