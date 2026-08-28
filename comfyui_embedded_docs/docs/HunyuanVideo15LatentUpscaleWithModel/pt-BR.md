# Hunyuan Video 15 Latent Upscale With Model

O nó Hunyuan Video 15 Latent Upscale With Model aumenta a resolução de uma representação de imagem latente. Ele primeiro faz o upscale das amostras latentes para um tamanho especificado usando um método de interpolação escolhido e, em seguida, refina o resultado com um modelo de upscale especializado Hunyuan Video 1.5 para melhorar a qualidade.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de upscale latente Hunyuan Video 1.5 usado para refinar as amostras com upscale. | LATENT_UPSCALE_MODEL | Sim | N/A |
| `amostras` | A representação de imagem latente que será submetida a upscale. | LATENT | Sim | N/A |
| `método_de_upscale` | O algoritmo de interpolação usado na etapa inicial de upscale (padrão: `"bilinear"`). | COMBO | Não | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` |
| `largura` | A largura alvo para o latente com upscale, em pixels. Um valor de 0 calculará a largura automaticamente com base na altura alvo e na proporção original. A largura final da saída será um múltiplo de 16 (padrão: 1280). | INT | Não | 0 a 16384 (passo: 8) |
| `altura` | A altura alvo para o latente com upscale, em pixels. Um valor de 0 calculará a altura automaticamente com base na largura alvo e na proporção original. A altura final da saída será um múltiplo de 16 (padrão: 720). | INT | Não | 0 a 16384 (passo: 8) |
| `corte` | Determina como o latente com upscale é cortado para se ajustar às dimensões alvo. | COMBO | Não | `"disabled"`<br>`"center"` |

**Nota sobre Dimensões:** Se `width` e `height` forem definidos como 0, o nó retorna as `samples` de entrada inalteradas. Se apenas uma dimensão for definida como 0, a outra dimensão será calculada para preservar a proporção original. As dimensões finais são sempre ajustadas para ter pelo menos 64 pixels e ser divisíveis por 16.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `LATENT` | A representação de imagem latente com upscale e refinada pelo modelo. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/pt-BR.md)

---
**Source fingerprint (SHA-256):** `71af49eefb010aadd30f8699b751ad901b1ee385d6cbeedd3a83995a1a623516`
