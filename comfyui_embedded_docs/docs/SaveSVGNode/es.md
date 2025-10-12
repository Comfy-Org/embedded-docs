> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/es.md)

Guarda archivos SVG en disco. Este nodo toma datos SVG como entrada y los guarda en tu directorio de salida con opción de incrustar metadatos. El nodo maneja automáticamente la nomenclatura de archivos con sufijos contadores y puede incrustar información del prompt del flujo de trabajo directamente en el archivo SVG.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `svg` | SVG | Sí | - | Los datos SVG que se guardarán en disco |
| `filename_prefix` | STRING | Sí | - | El prefijo para el archivo a guardar. Puede incluir información de formato como %date:yyyy-MM-dd% o %Empty Latent Image.width% para incluir valores de nodos. (valor por defecto: "svg/ComfyUI") |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `ui` | DICT | Devuelve información del archivo incluyendo nombre de archivo, subcarpeta y tipo para mostrar en la interfaz de ComfyUI |

**Nota:** Este nodo incrusta automáticamente metadatos del flujo de trabajo (prompt e información PNG extra) en el archivo SVG cuando está disponible. Los metadatos se insertan como una sección CDATA dentro del elemento de metadatos del SVG.
