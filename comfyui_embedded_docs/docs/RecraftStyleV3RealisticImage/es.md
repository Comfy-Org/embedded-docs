> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3RealisticImage/es.md)

Este nodo crea una configuración de estilo para generar imágenes realistas utilizando la API de Recraft. Selecciona el estilo `realistic_image` y permite elegir un subestilo opcional para ajustar la apariencia del resultado.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-------------|-------------|-------|-------------|
| `substyle` | STRING | Sí | Múltiples opciones disponibles (determinadas por la API de Recraft) | El subestilo específico a aplicar al estilo `realistic_image`. Si se establece en "None", no se aplicará ningún subestilo. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|-------------|-------------|
| `recraft_style` | STYLEV3 | Un objeto de configuración de estilo de Recraft que contiene el estilo `realistic_image` y la configuración del subestilo seleccionado. Esta salida se puede conectar a otros nodos de Recraft que acepten una entrada de estilo. |

---
**Source fingerprint (SHA-256):** `23eafae0a00f1806052a6583db791a5c1fd418ea940ed6463824dffe843ed0d7`
