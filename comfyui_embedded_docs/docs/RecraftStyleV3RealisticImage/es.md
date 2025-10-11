> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3RealisticImage/es.md)

Este nodo crea una configuración de estilo de imagen realista para usar con la API de Recraft. Permite seleccionar el estilo realistic_image y elegir entre varias opciones de subestilo para personalizar la apariencia de la salida.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `substyle` | STRING | Sí | Múltiples opciones disponibles | El subestilo específico a aplicar al estilo realistic_image. Si se establece en "None", no se aplicará ningún subestilo. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | Retorna un objeto de configuración de estilo Recraft que contiene el estilo realistic_image y la configuración del subestilo seleccionado. |