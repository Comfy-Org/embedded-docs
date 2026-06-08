El nodo Crear Video genera un archivo de video a partir de una secuencia de imágenes. Puedes especificar la velocidad de reproducción usando fotogramas por segundo y, opcionalmente, agregar audio al video. El nodo combina tus imágenes en un formato de video que se puede reproducir con la velocidad de fotogramas especificada.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imágenes` | Las imágenes a partir de las cuales crear el video. | IMAGE | Sí | - |
| `fps` | Los fotogramas por segundo para la velocidad de reproducción del video (valor predeterminado: 30.0). | FLOAT | Sí | 1.0 - 120.0 |
| `audio` | El audio que se agregará al video. | AUDIO | No | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El archivo de video generado que contiene las imágenes de entrada y el audio opcional. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/es.md)

---
**Source fingerprint (SHA-256):** `6da9a09542b5e357c0180c30018ec10facf06d1bdd3e4edee8172b8426802e3d`
