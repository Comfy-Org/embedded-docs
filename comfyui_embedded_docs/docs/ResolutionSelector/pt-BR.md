# Seletor de Resolução

O nó Seletor de Resolução calcula a largura e altura em pixels de uma imagem com base em uma proporção de aspecto escolhida e uma resolução total alvo em megapixels. Ele é útil para gerar dimensões consistentes para outros nós, como o nó Imagem Latente Vazia. As dimensões de saída são sempre arredondadas para o múltiplo de 8 mais próximo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `proporção_de_aspecto` | A proporção de aspecto para as dimensões de saída (padrão: `"SQUARE"`). | COMBO | Sim | `"SQUARE"`<br>`"PORTRAIT_2_3"`<br>`"PORTRAIT_3_4"`<br>`"PORTRAIT_9_16"`<br>`"LANDSCAPE_3_2"`<br>`"LANDSCAPE_4_3"`<br>`"LANDSCAPE_16_9"` |
| `megapixels` | Total de megapixels alvo. 1,0 MP ≈ 1024×1024 para uma proporção de aspecto quadrada (padrão: 1,0). | FLOAT | Sim | 0.1 - 16.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `width` | A largura calculada em pixels, que é um múltiplo de 8. | INT |
| `height` | A altura calculada em pixels, que é um múltiplo de 8. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/pt-BR.md)

---
**Source fingerprint (SHA-256):** `221d38fa72c9989e06b706d33fd3e0dc4caa0f741dd2931864c58a6bd7f52613`
