# NodoGuardarSVG

Guarda archivos SVG en el disco. Este nodo toma datos SVG como entrada y los guarda en su directorio de salida con incrustación de metadatos opcional. El nodo maneja automáticamente el nombre de los archivos con sufijos de contador y puede incrustar información del prompt del flujo de trabajo directamente en el archivo SVG.

## Entradas

| Parámetro | Descripción | Tipo de Datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `svg` | Los datos SVG que se guardarán en el disco | SVG | Sí | - |
| `filename_prefix` | El prefijo para el archivo a guardar. Puede incluir información de formato como %date:yyyy-MM-dd% o %Empty Latent Image.width% para incluir valores de nodos. (predeterminado: "svg/ComfyUI") | STRING | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Datos |
| --- | --- | --- |
| `svg` | Los datos SVG que se guardaron en el disco | SVG |
| `ui` | Devuelve información del archivo, incluidos nombre de archivo, subcarpeta y tipo, para mostrarla en la interfaz de ComfyUI | DICT |

**Nota:** Este nodo incrusta automáticamente metadatos del flujo de trabajo (información del prompt y PNG adicional) en el archivo SVG cuando están disponibles. Los metadatos se insertan como una sección CDATA dentro del elemento de metadatos del SVG.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/es.md)

---
**Source fingerprint (SHA-256):** `365137d5dacab3142c25945fd97bce4b827d9d7d4dd839986c68f491a28fb805`
