# EmptyLTXVLatentVideo

O nó EmptyLTXVLatentVideo cria um tensor latente vazio para processamento de vídeo. Ele gera um ponto de partida em branco com a largura, altura, comprimento e tamanho de lote especificados, que pode ser usado como entrada para fluxos de trabalho de geração de vídeo. O nó produz uma representação latente preenchida com zeros, cujas dimensões espaciais são 32 vezes menores que a largura e a altura configuradas, e cujo número de quadros é comprimido por um fator de 8.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `largura` | A largura do tensor latente de vídeo (padrão: 768, passo: 32) | INT | Sim | 64 a MAX_RESOLUTION |
| `altura` | A altura do tensor latente de vídeo (padrão: 512, passo: 32) | INT | Sim | 64 a MAX_RESOLUTION |
| `comprimento` | O número de quadros no vídeo latente (padrão: 97, passo: 8) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | O número de vídeos latentes a serem gerados em um lote (padrão: 1) | INT | Sim | 1 a 4096 |

Observação: O vídeo latente é comprimido em comparação às dimensões de entrada: as dimensões espaciais (largura e altura) são divididas por 32, e o número de quadros (comprimento) é dividido por 8 e arredondado para cima para o número inteiro mais próximo. Os valores de passo para largura, altura e comprimento ajudam a manter essas divisões uniformes.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `samples` | O tensor latente vazio gerado com valores zero nas dimensões especificadas, juntamente com uma proporção de redução espacial de 32 | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`
