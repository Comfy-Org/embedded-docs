> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3VectorIllustrationNode/es.md)

Este nodo configura un estilo para usar con la API de Recraft, seleccionando específicamente el estilo `vector_illustration`. Permite elegir opcionalmente un subestilo más específico dentro de esa categoría. El nodo genera un objeto de configuración de estilo que puede pasarse a otros nodos de la API de Recraft.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `substyle` | STRING | No | `"vector_illustration"`<br>`"vector_illustration_flat"`<br>`"vector_illustration_3d"`<br>`"vector_illustration_hand_drawn"`<br>`"vector_illustration_retro"`<br>`"vector_illustration_modern"`<br>`"vector_illustration_abstract"`<br>`"vector_illustration_geometric"`<br>`"vector_illustration_organic"`<br>`"vector_illustration_minimalist"`<br>`"vector_illustration_detailed"`<br>`"vector_illustration_colorful"`<br>`"vector_illustration_monochrome"`<br>`"vector_illustration_grayscale"`<br>`"vector_illustration_pastel"`<br>`"vector_illustration_vibrant"`<br>`"vector_illustration_muted"`<br>`"vector_illustration_warm"`<br>`"vector_illustration_cool"`<br>`"vector_illustration_neutral"`<br>`"vector_illustration_bold"`<br>`"vector_illustration_subtle"`<br>`"vector_illustration_playful"`<br>`"vector_illustration_serious"`<br>`"vector_illustration_elegant"`<br>`"vector_illustration_rustic"`<br>`"vector_illustration_urban"`<br>`"vector_illustration_nature"`<br>`"vector_illustration_fantasy"`<br>`"vector_illustration_sci_fi"`<br>`"vector_illustration_historical"`<br>`"vector_illustration_futuristic"`<br>`"vector_illustration_whimsical"`<br>`"vector_illustration_surreal"`<br>`"vector_illustration_realistic"`<br>`"vector_illustration_stylized"`<br>`"vector_illustration_cartoony"`<br>`"vector_illustration_anime"`<br>`"vector_illustration_comic"`<br>`"vector_illustration_pixel"`<br>`"vector_illustration_low_poly"`<br>`"vector_illustration_high_poly"`<br>`"vector_illustration_isometric"`<br>`"vector_illustration_orthographic"`<br>`"vector_illustration_perspective"`<br>`"vector_illustration_2d"`<br>`"vector_illustration_2.5d"`<br>`"vector_illustration_3d"`<br>`"vector_illustration_4d"` | Un subestilo opcional y más específico dentro de la categoría `vector_illustration`. Si no se selecciona, se utiliza el estilo base `vector_illustration`. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | Un objeto de configuración de estilo para la API de Recraft que contiene el estilo `vector_illustration` seleccionado y el subestilo opcional. Esto puede conectarse a otros nodos de Recraft. |
