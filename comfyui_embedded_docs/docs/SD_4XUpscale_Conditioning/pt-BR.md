# SD_4XUpscale_Conditioning

O nó SD_4XUpscale_Conditioning prepara dados de condicionamento para ampliar imagens com modelos de difusão. Ele escala as imagens de entrada por uma proporção escolhida, adiciona aumento de ruído opcional e retorna condicionamentos positivo e negativo modificados junto com um latent vazio para o tamanho ampliado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `images` | Imagens de entrada a serem ampliadas. | IMAGE | Sim | - |
| `positive` | Dados de condicionamento positivo que orientam a geração em direção ao conteúdo desejado. | CONDITIONING | Sim | - |
| `negative` | Dados de condicionamento negativo que afastam a geração de conteúdo indesejado. | CONDITIONING | Sim | - |
| `scale_ratio` | Multiplicador aplicado às dimensões da imagem de entrada ao preparar o condicionamento ampliado e o latent (padrão: 4.0). | FLOAT | Sim | 0.0 - 10.0 (passo 0.01) |
| `noise_augmentation` | Quantidade de ruído a ser adicionada durante o processo de ampliação (padrão: 0.0). | FLOAT | Sim | 0.0 - 1.0 (passo 0.001) |

Observação: `noise_augmentation` é um parâmetro avançado, exibido na interface do nó sob a opção "Avançado".

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo modificado com os dados da imagem escalada e as configurações de aumento de ruído aplicadas. | CONDITIONING |
| `negative` | Condicionamento negativo modificado com os dados da imagem escalada e as configurações de aumento de ruído aplicadas. | CONDITIONING |
| `latent` | Representação latent vazia correspondente às dimensões ampliadas. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f215e890bd86f42d4da9c6f575fc92e65844e2e2056c5610310d8089e5d61902`
