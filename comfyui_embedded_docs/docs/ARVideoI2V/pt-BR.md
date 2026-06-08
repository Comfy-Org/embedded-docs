Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/en.md)

## Visão Geral

Este nó prepara uma configuração de geração de vídeo a partir de imagem para modelos de vídeo AR (Auto-Regressivos). Ele recebe uma imagem inicial, a codifica no espaço latente usando um VAE e armazena a imagem codificada na configuração do modelo. Isso permite que o processo de amostragem de vídeo utilize a imagem como primeiro quadro, efetivamente semeando a geração sem a necessidade de uma arquitetura de modelo separada de imagem para vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de vídeo AR a ser usado para geração. | MODEL | Sim | - |
| `vae` | O modelo VAE usado para codificar a imagem inicial no espaço latente. | VAE | Sim | - |
| `imagem_inicial` | A imagem inicial que servirá como primeiro quadro do vídeo gerado. | IMAGE | Sim | - |
| `largura` | A largura dos quadros do vídeo gerado (padrão: 832). | INT | Sim | 16 a 8192 (passo: 16) |
| `altura` | A altura dos quadros do vídeo gerado (padrão: 480). | INT | Sim | 16 a 8192 (passo: 16) |
| `duração` | O número total de quadros no vídeo gerado (padrão: 81). | INT | Sim | 1 a 1024 (passo: 4) |
| `tamanho_do_lote` | O número de sequências de vídeo a serem geradas em um único lote (padrão: 1). | INT | Sim | 1 a 64 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `MODEL` | O modelo clonado com a imagem inicial codificada armazenada em sua configuração para geração de vídeo. | MODEL |
| `LATENT` | Um tensor latente vazio com as dimensões corretas para o processo de geração de vídeo. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0445b279ba49fa946050cfa70d1e6b13240eaa600b99dfe63f27c3203dc4b61b`
