> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/en.md)

## Visão Geral

Este nó prepara uma configuração de geração de vídeo a partir de imagem para modelos de vídeo AR (Auto-Regressivos). Ele recebe uma imagem inicial, a codifica no espaço latente usando um VAE e armazena a imagem codificada na configuração do modelo. Isso permite que o processo de amostragem de vídeo utilize a imagem como primeiro quadro, efetivamente semeando a geração sem a necessidade de uma arquitetura de modelo separada de imagem para vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | MODEL | Sim | - | O modelo de vídeo AR a ser usado para geração. |
| `vae` | VAE | Sim | - | O modelo VAE usado para codificar a imagem inicial no espaço latente. |
| `imagem_inicial` | IMAGE | Sim | - | A imagem inicial que servirá como primeiro quadro do vídeo gerado. |
| `largura` | INT | Sim | 16 a 8192 (passo: 16) | A largura dos quadros do vídeo gerado (padrão: 832). |
| `altura` | INT | Sim | 16 a 8192 (passo: 16) | A altura dos quadros do vídeo gerado (padrão: 480). |
| `duração` | INT | Sim | 1 a 1024 (passo: 4) | O número total de quadros no vídeo gerado (padrão: 81). |
| `tamanho_do_lote` | INT | Sim | 1 a 64 | O número de sequências de vídeo a serem geradas em um único lote (padrão: 1). |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `MODEL` | MODEL | O modelo clonado com a imagem inicial codificada armazenada em sua configuração para geração de vídeo. |
| `LATENT` | LATENT | Um tensor latente vazio com as dimensões corretas para o processo de geração de vídeo. |

---
**Source fingerprint (SHA-256):** `0445b279ba49fa946050cfa70d1e6b13240eaa600b99dfe63f27c3203dc4b61b`
