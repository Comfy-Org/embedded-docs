# ARVideoI2V

## Visão Geral

Este nó prepara uma configuração de geração de imagem para vídeo para modelos de vídeo AR (Autorregressivos). Ele recebe uma imagem inicial, codifica-a no espaço latente usando uma VAE e armazena a imagem codificada na configuração do modelo. Isso permite que o processo de amostragem de vídeo use a imagem como primeiro quadro, servindo efetivamente de base para a geração sem a necessidade de uma arquitetura de modelo separada de imagem para vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de vídeo AR a ser usado para a geração. | MODEL | Sim | - |
| `vae` | O modelo VAE usado para codificar a imagem inicial no espaço latente. | VAE | Sim | - |
| `start_image` | A imagem inicial que servirá como o primeiro quadro do vídeo gerado. | IMAGE | Sim | - |
| `width` | A largura dos quadros do vídeo gerado (padrão: 832). | INT | Sim | 16 a 8192 (passo: 16) |
| `height` | A altura dos quadros do vídeo gerado (padrão: 480). | INT | Sim | 16 a 8192 (passo: 16) |
| `length` | O número total de quadros no vídeo gerado (padrão: 81). | INT | Sim | 1 a 1024 (passo: 4) |
| `batch_size` | O número de sequências de vídeo a gerar em um único lote (padrão: 1). | INT | Sim | 1 a 64 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `MODEL` | O modelo clonado com a imagem inicial codificada armazenada em sua configuração para geração de vídeo. | MODEL |
| `LATENT` | Um tensor latente vazio com forma [batch_size, 16, lat_t, height/8, width/8], onde lat_t = ((length - 1) // 4) + 1 é o número de quadros latentes derivados do comprimento de vídeo solicitado. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/pt-BR.md)

---
**Source fingerprint (SHA-256):** `984834951b9d5a22aef51c85a5019fd8ba58cdb2d6fff235371ed29f316896d8`
