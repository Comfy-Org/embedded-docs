# Recraft Estilo - Ilustração Digital

Este nó configura um estilo para uso com a API Recraft, selecionando especificamente o estilo "digital_illustration". Ele permite que você escolha um subestilo opcional para refinar ainda mais a direção artística da imagem gerada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `subestilo` | Um subestilo opcional para especificar um tipo particular de ilustração digital. Se não for selecionado, o estilo base "digital_illustration" será usado. | STRING | Não | `"digital_illustration"`<br>`"digital_illustration_anime"`<br>`"digital_illustration_cartoon"`<br>`"digital_illustration_comic"`<br>`"digital_illustration_concept_art"`<br>`"digital_illustration_fantasy"`<br>`"digital_illustration_futuristic"`<br>`"digital_illustration_graffiti"`<br>`"digital_illustration_graphic_novel"`<br>`"digital_illustration_hyperrealistic"`<br>`"digital_illustration_ink"`<br>`"digital_illustration_manga"`<br>`"digital_illustration_minimalist"`<br>`"digital_illustration_pixel_art"`<br>`"digital_illustration_pop_art"`<br>`"digital_illustration_retro"`<br>`"digital_illustration_sci_fi"`<br>`"digital_illustration_sticker"`<br>`"digital_illustration_street_art"`<br>`"digital_illustration_surreal"`<br>`"digital_illustration_vector"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `recraft_style` | Um objeto de estilo configurado contendo o estilo "digital_illustration" selecionado e o subestilo opcional, pronto para ser passado para outros nós da API Recraft. | STYLEV3 |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3DigitalIllustration/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e52790a670839608ee1cb576e802a54d3bf2ca879ec288a24acd4ac7db27021a`
