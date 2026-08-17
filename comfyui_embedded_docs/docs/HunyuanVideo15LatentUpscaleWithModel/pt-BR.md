# Hunyuan Video 15 Latent Upscale With Model

O nó Hunyuan Video 15 Latent Upscale With Model aumenta a resolução de uma representação latente de imagem. Primeiro, ele amplia as amostras latentes para um tamanho especificado usando um método de interpolação escolhido e, em seguida, refina o resultado ampliado usando um modelo de ampliação especializado Hunyuan Video 1.5 para melhorar a qualidade.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo de ampliação latent Hunyuan Video 1.5 usado para refinar as amostras ampliadas. | LATENT_UPSCALE_MODEL | Sim | N/A |
| `samples` | A representação latente da imagem a ser ampliada. | LATENT | Sim | N/A |
| `upscale_method` | O algoritmo de interpolação usado para a etapa inicial de ampliação (padrão: `"bilinear"`). | COMBO | Não | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"bislerp"` |
| `width` | A largura alvo para o latent ampliado, em pixels. Um valor de 0 calcula a largura automaticamente com base na altura alvo e na proporção de aspecto original. A largura final da saída será um múltiplo de 16 (padrão: 1280). | INT | Não | 0 a 16384 (passo 8) |
| `height` | A altura alvo para o latent ampliado, em pixels. Um valor de 0 calcula a altura automaticamente com base na largura alvo e na proporção de aspecto original. A altura final da saída será um múltiplo de 16 (padrão: 720). | INT | Não | 0 a 16384 (passo 8) |
| `crop` | Determina como o latent ampliado é cortado para caber nas dimensões alvo. | COMBO | Não | `"disabled"`<br>`"center"` |

**Nota sobre Dimensões:** Se ambos `width` e `height` estiverem definidos como 0, o nó retorna as `samples` de entrada inalteradas. Se apenas uma dimensão estiver definida como 0, a outra é calculada para preservar a proporção de aspecto original. As dimensões finais são sempre ajustadas para ter pelo menos 64 pixels e são divisíveis por 16.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `LATENT` | A representação latente da imagem ampliada e refinada pelo modelo. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15LatentUpscaleWithModel/pt-BR.md)

---
**Source fingerprint (SHA-256):** `71af49eefb010aadd30f8699b751ad901b1ee385d6cbeedd3a83995a1a623516`
