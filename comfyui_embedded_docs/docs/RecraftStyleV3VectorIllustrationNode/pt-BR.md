> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3VectorIllustrationNode/pt-BR.md)

Este nó configura um estilo para uso com a API Recraft, selecionando especificamente o estilo `vector_illustration`. Ele permite que você escolha opcionalmente um subestilo mais específico dentro dessa categoria. O nó gera um objeto de configuração de estilo que pode ser passado para outros nós da API Recraft.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `substyle` | STRING | Não | `"vector_illustration"`<br>`"vector_illustration_flat"`<br>`"vector_illustration_3d"`<br>`"vector_illustration_hand_drawn"`<br>`"vector_illustration_retro"`<br>`"vector_illustration_modern"`<br>`"vector_illustration_abstract"`<br>`"vector_illustration_geometric"`<br>`"vector_illustration_organic"`<br>`"vector_illustration_minimalist"`<br>`"vector_illustration_detailed"`<br>`"vector_illustration_colorful"`<br>`"vector_illustration_monochrome"`<br>`"vector_illustration_grayscale"`<br>`"vector_illustration_pastel"`<br>`"vector_illustration_vibrant"`<br>`"vector_illustration_muted"`<br>`"vector_illustration_warm"`<br>`"vector_illustration_cool"`<br>`"vector_illustration_neutral"`<br>`"vector_illustration_bold"`<br>`"vector_illustration_subtle"`<br>`"vector_illustration_playful"`<br>`"vector_illustration_serious"`<br>`"vector_illustration_elegant"`<br>`"vector_illustration_rustic"`<br>`"vector_illustration_urban"`<br>`"vector_illustration_nature"`<br>`"vector_illustration_fantasy"`<br>`"vector_illustration_sci_fi"`<br>`"vector_illustration_historical"`<br>`"vector_illustration_futuristic"`<br>`"vector_illustration_whimsical"`<br>`"vector_illustration_surreal"`<br>`"vector_illustration_realistic"`<br>`"vector_illustration_stylized"`<br>`"vector_illustration_cartoony"`<br>`"vector_illustration_anime"`<br>`"vector_illustration_comic"`<br>`"vector_illustration_pixel"`<br>`"vector_illustration_low_poly"`<br>`"vector_illustration_high_poly"`<br>`"vector_illustration_isometric"`<br>`"vector_illustration_orthographic"`<br>`"vector_illustration_perspective"`<br>`"vector_illustration_2d"`<br>`"vector_illustration_2.5d"`<br>`"vector_illustration_3d"`<br>`"vector_illustration_4d"` | Um subestilo opcional e mais específico dentro da categoria `vector_illustration`. Se não for selecionado, o estilo base `vector_illustration` será usado. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | Um objeto de configuração de estilo da API Recraft contendo o estilo `vector_illustration` selecionado e o subestilo opcional. Isso pode ser conectado a outros nós Recraft. |
