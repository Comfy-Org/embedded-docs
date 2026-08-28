# Cargador Triple CLIP

TripleCLIPLoader carga tres modelos de codificador de texto al mismo tiempo y los combina en un único modelo CLIP. Se utiliza para flujos de trabajo que necesitan múltiples codificadores de texto trabajando juntos, como SD3, que usa modelos clip-l, clip-g y t5.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `nombre_clip1` | El primer modelo de codificador de texto para cargar de los codificadores de texto disponibles | COMBO | Sí | Múltiples opciones disponibles (todos los archivos en la carpeta text_encoders) |
| `nombre_clip2` | El segundo modelo de codificador de texto para cargar de los codificadores de texto disponibles | COMBO | Sí | Múltiples opciones disponibles (todos los archivos en la carpeta text_encoders) |
| `nombre_clip3` | El tercer modelo de codificador de texto para cargar de los codificadores de texto disponibles | COMBO | Sí | Múltiples opciones disponibles (todos los archivos en la carpeta text_encoders) |

**Nota:** Los tres parámetros son obligatorios. Las opciones disponibles son los archivos de codificador de texto en tu carpeta text_encoders. Si no se encuentra un archivo seleccionado, el nodo genera un error. El nodo carga los tres modelos seleccionados y los combina en un único modelo CLIP.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `CLIP` | Un modelo CLIP combinado que contiene los tres codificadores de texto cargados | CLIP |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/es.md)

---
**Source fingerprint (SHA-256):** `edb341093c4c86ec4d8e024dffa7e33311f600e61ec8ef1813da6d28474f8233`
