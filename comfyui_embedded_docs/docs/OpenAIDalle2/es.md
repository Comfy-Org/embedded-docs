> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/es.md)

# OpenAIDalle2

Genera imágenes de forma síncrona a través del endpoint DALL·E 2 de OpenAI.

## Cómo funciona

Este nodo se conecta a la API DALL·E 2 de OpenAI para crear imágenes basadas en descripciones textuales. Cuando proporcionas un prompt de texto, el nodo lo envía a los servidores de OpenAI, que generan las imágenes correspondientes y las devuelven a ComfyUI. El nodo puede operar en dos modos: generación estándar de imágenes usando solo un prompt de texto, o modo de edición de imágenes cuando se proporcionan tanto una imagen como una máscara. En el modo de edición, utiliza la máscara para determinar qué partes de la imagen original deben modificarse mientras mantiene otras áreas sin cambios.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Valor por Defecto | Rango | Descripción |
|-----------|--------------|-----------------|-------------------|-------|-------------|
| `prompt` | STRING | requerido | "" | - | Prompt de texto para DALL·E |
| `seed` | INT | opcional | 0 | 0 a 2147483647 | aún no implementado en el backend |
| `tamaño` | COMBO | opcional | "1024x1024" | "256x256", "512x512", "1024x1024" | Tamaño de la imagen |
| `n` | INT | opcional | 1 | 1 a 8 | Cantidad de imágenes a generar |
| `imagen` | IMAGE | opcional | None | - | Imagen de referencia opcional para edición de imágenes. |
| `mask` | MASK | opcional | None | - | Máscara opcional para inpainting (las áreas blancas serán reemplazadas) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `IMAGE` | IMAGE | La(s) imagen(es) generada(s) o editada(s) desde DALL·E 2 |

---
**Source fingerprint (SHA-256):** `ad10b149ac28559ad18c09e0f071286509680603d953833106ad6a2d578f7efe`
