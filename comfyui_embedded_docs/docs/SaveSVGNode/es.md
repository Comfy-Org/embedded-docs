# NodoGuardarSVG

Guarda archivos SVG en el disco. Este nodo recibe datos SVG como entrada y los guarda en tu directorio de salida con metadatos opcionales incrustados. El nodo maneja automáticamente la nomenclatura de archivos con sufijos de contador y puede incrustar información de flujo de trabajo directamente en el archivo SVG.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `svg` | Los datos SVG que se guardarán en el disco | SVG | Sí | - |
| `prefijo_nombre_archivo` | El prefijo para el archivo a guardar. Puede incluir información de formato como %date:yyyy-MM-dd% o %Empty Latent Image.width% para incluir valores de nodos. (predeterminado: "svg/ComfyUI") | STRING | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `svg` | Devuelve información del archivo, incluyendo nombre, subcarpeta y tipo para mostrar en la interfaz de ComfyUI | DICT |

**Nota:** Este nodo incrusta automáticamente metadatos del flujo de trabajo (información de prompt y PNG adicional) en el archivo SVG cuando están disponibles. Los metadatos se insertan como una sección CDATA dentro del elemento de metadatos del SVG.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/es.md)

---
**Source fingerprint (SHA-256):** `a294103d8d2306ce6765912a98c5572323bb5394909ee384591534b0b404ea70`
