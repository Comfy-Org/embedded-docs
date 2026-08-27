# NodoGuardarSVG

Guardar archivos SVG en disco. Este nodo toma datos SVG como entrada y los guarda en el directorio de salida con incrustación opcional de metadatos. El nodo maneja automáticamente el nombre de los archivos con sufijos de contador y puede incrustar información del prompt del flujo de trabajo directamente en el archivo SVG.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `svg` | Los datos SVG que se guardarán en disco | SVG | Sí | - |
| `prefijo_nombre_archivo` | El prefijo para el archivo a guardar. Puede incluir información de formato como %date:yyyy-MM-dd% o %Empty Latent Image.width% para incluir valores de nodos. (por defecto: "svg/ComfyUI") | STRING | Sí | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `svg` | Los datos SVG originales, pasados después de guardarlos | SVG |
| `ui` | Información del archivo guardado, incluyendo nombre, subcarpeta y tipo para mostrar en la interfaz de ComfyUI | DICT |

**Nota:** Este nodo incrusta automáticamente los metadatos del flujo de trabajo (prompt e información PNG adicional) en el archivo SVG cuando estén disponibles. Los metadatos se insertan como una sección CDATA dentro del elemento de metadatos del SVG. Los archivos se guardan usando el patrón `filename_prefix_00001_.svg`; al procesar un lote, `%batch_num%` en el prefijo se reemplaza con el índice del elemento actual del lote.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/es.md)

---
**Source fingerprint (SHA-256):** `365137d5dacab3142c25945fd97bce4b827d9d7d4dd839986c68f491a28fb805`
