> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGLB/es.md)

El nodo SaveGLB guarda datos de mallas 3D como archivos GLB, que es un formato común para modelos 3D. Toma datos de malla como entrada y los exporta al directorio de salida con el prefijo de nombre de archivo especificado. El nodo puede guardar múltiples mallas si la entrada contiene múltiples objetos de malla, y añade automáticamente metadatos a los archivos cuando los metadatos están habilitados.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `malla` | MESH | Sí | - | Los datos de malla 3D que se guardarán como archivo GLB |
| `prefijo_nombre_archivo` | STRING | No | - | El prefijo para el nombre de archivo de salida (predeterminado: "mesh/ComfyUI") |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `ui` | UI | Muestra los archivos GLB guardados en la interfaz de usuario con información del nombre de archivo y subcarpeta |