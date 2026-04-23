> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/pt-BR.md)

O nó Seletor de Resolução calcula a largura e altura em pixels de uma imagem com base em uma proporção de aspecto escolhida e uma resolução total alvo em megapixels. Ele é útil para gerar dimensões consistentes para outros nós, como o nó Imagem Latente Vazia. As dimensões de saída são sempre arredondadas para o múltiplo de 8 mais próximo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `aspect_ratio` | COMBO | Sim | `"SQUARE"`<br>`"PORTRAIT_2_3"`<br>`"PORTRAIT_3_4"`<br>`"PORTRAIT_9_16"`<br>`"LANDSCAPE_3_2"`<br>`"LANDSCAPE_4_3"`<br>`"LANDSCAPE_16_9"` | A proporção de aspecto para as dimensões de saída (padrão: `"SQUARE"`). |
| `megapixels` | FLOAT | Sim | 0.1 - 16.0 | Total de megapixels alvo. 1,0 MP ≈ 1024×1024 para uma proporção de aspecto quadrada (padrão: 1,0). |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `width` | INT | A largura calculada em pixels, que é um múltiplo de 8. |
| `height` | INT | A altura calculada em pixels, que é um múltiplo de 8. |