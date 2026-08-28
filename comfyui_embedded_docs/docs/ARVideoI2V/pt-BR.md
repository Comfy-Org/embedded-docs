# ARVideoI2V

## Visão Geral

Este nó prepara uma configuração de geração de imagem para vídeo para modelos de vídeo AR (Auto-Regressivos) que usam Causal Forcing ou Self-Forcing. Ele codifica uma imagem inicial no espaço latente com um VAE e a armazena nas opções do transformer do modelo, permitindo que o processo de amostragem de vídeo inicialize o cache KV antes da remoção de ruído. Ele usa o mesmo checkpoint do modelo de texto para vídeo, portanto não é necessária uma arquitetura separada de imagem para vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de vídeo AR a ser usado para a geração. | MODEL | Sim | - |
| `vae` | O modelo VAE usado para codificar a imagem inicial no espaço latente. | VAE | Sim | - |
| `imagem_inicial` | A imagem inicial que servirá como o primeiro quadro do vídeo gerado. Apenas a primeira imagem do lote de entrada é usada, e somente os canais RGB dela são codificados. | IMAGE | Sim | - |
| `largura` | A largura dos quadros do vídeo gerado (padrão: 832). | INT | Sim | 16 a 8192 (step: 16) |
| `altura` | A altura dos quadros do vídeo gerado (padrão: 480). | INT | Sim | 16 a 8192 (step: 16) |
| `duração` | O número total de quadros no vídeo gerado (padrão: 81). | INT | Sim | 1 a 1024 (step: 4) |
| `tamanho_do_lote` | O número de sequências de vídeo a serem geradas em um único lote (padrão: 1). | INT | Sim | 1 a 64 |

Nota: A imagem inicial é redimensionada para os valores `width` e `height` especificados antes de ser codificada. A dimensão temporal latente é calculada como `((length - 1) // 4) + 1`, e as dimensões espaciais latentes são `height / 8` e `width / 8`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `MODEL` | O modelo clonado com a imagem inicial codificada armazenada nas opções do transformer (`ar_config.initial_latent`), que o amostrador usa para semear o cache KV antes da remoção de ruído. | MODEL |
| `LATENT` | Um tensor latente preenchido com zeros, com formato `[batch_size, 16, lat_t, height // 8, width // 8]`, onde `lat_t = ((length - 1) // 4) + 1`. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/pt-BR.md)

---
**Source fingerprint (SHA-256):** `984834951b9d5a22aef51c85a5019fd8ba58cdb2d6fff235371ed29f316896d8`
