> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3DigitalIllustration/es.md)

Este nodo configura un estilo para usar con la API de Recraft, seleccionando específicamente el estilo "digital_illustration". Permite elegir un subestilo opcional para refinar aún más la dirección artística de la imagen generada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `subestilo` | STRING | No | `"digital_illustration"`<br>`"digital_illustration_anime"`<br>`"digital_illustration_cartoon"`<br>`"digital_illustration_comic"`<br>`"digital_illustration_concept_art"`<br>`"digital_illustration_fantasy"`<br>`"digital_illustration_futuristic"`<br>`"digital_illustration_graffiti"`<br>`"digital_illustration_graphic_novel"`<br>`"digital_illustration_hyperrealistic"`<br>`"digital_illustration_ink"`<br>`"digital_illustration_manga"`<br>`"digital_illustration_minimalist"`<br>`"digital_illustration_pixel_art"`<br>`"digital_illustration_pop_art"`<br>`"digital_illustration_retro"`<br>`"digital_illustration_sci_fi"`<br>`"digital_illustration_sticker"`<br>`"digital_illustration_street_art"`<br>`"digital_illustration_surreal"`<br>`"digital_illustration_vector"` | Un subestilo opcional para especificar un tipo particular de ilustración digital. Si no se selecciona, se utiliza el estilo base "digital_illustration". |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | Un objeto de estilo configurado que contiene el estilo "digital_illustration" seleccionado y el subestilo opcional, listo para ser pasado a otros nodos de la API de Recraft. |
