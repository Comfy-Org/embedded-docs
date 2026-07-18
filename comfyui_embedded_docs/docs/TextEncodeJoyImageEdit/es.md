# TextEncodeJoyImageEdit

Este nodo codifica un mensaje de texto e imágenes opcionales en datos de condicionamiento para su uso con modelos JoyImage. Combina un codificador de texto CLIP con entradas de imagen opcionales para crear un condicionamiento enriquecido que puede guiar tareas de generación o edición de imágenes.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `clip` | El modelo CLIP utilizado para codificar el mensaje de texto | CLIP | Sí | - |
| `prompt` | El mensaje de texto a codificar, compatible con entrada multilínea y mensajes dinámicos | STRING | Sí | - |
| `vae` | Un modelo VAE para codificar imágenes en el espacio latente (opcional) | VAE | No | - |
| `images` | Una o más imágenes para incluir en el condicionamiento, hasta un máximo de 6 imágenes | IMAGE | No | 0 a 6 imágenes |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `CONDITIONING` | Los datos de condicionamiento codificados que combinan el mensaje de texto y cualquier imagen proporcionada | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeJoyImageEdit/es.md)

---
**Source fingerprint (SHA-256):** `ef48523aa9fc990b2839d755cef272bcdfbacef5af8d961736fde5200c6f082d`
