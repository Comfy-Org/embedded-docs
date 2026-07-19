# Aplicar Controlnet com VAE

Esta documentação foi gerada por IA. Caso encontre erros ou tenha sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/en.md)

Este nó aplica a orientação do ControlNet ao condicionamento do Stable Diffusion 3. Ele recebe entradas de condicionamento positivo e negativo, juntamente com um modelo ControlNet e uma imagem, e então aplica a orientação de controle com parâmetros ajustáveis de intensidade e temporização para influenciar o processo de geração.

**Nota:** Este nó foi marcado como obsoleto e pode ser removido em versões futuras.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | O condicionamento positivo ao qual aplicar a orientação do ControlNet | CONDITIONING | Sim | - |
| `negativo` | O condicionamento negativo ao qual aplicar a orientação do ControlNet | CONDITIONING | Sim | - |
| `control_net` | O modelo ControlNet a ser usado para orientação | CONTROL_NET | Sim | - |
| `vae` | O modelo VAE utilizado no processo | VAE | Sim | - |
| `imagem` | A imagem de entrada que o ControlNet usará como orientação | IMAGE | Sim | - |
| `força` | A intensidade do efeito do ControlNet (padrão: 1.0) | FLOAT | Sim | 0.0 - 10.0 |
| `percentual_inicial` | O ponto inicial no processo de geração onde o ControlNet começa a aplicar (padrão: 0.0) | FLOAT | Sim | 0.0 - 1.0 |
| `percentual_final` | O ponto final no processo de geração onde o ControlNet para de aplicar (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | O condicionamento positivo modificado com a orientação do ControlNet aplicada | CONDITIONING |
| `negativo` | O condicionamento negativo modificado com a orientação do ControlNet aplicada | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7bd24b19c159374bc86a773be9b563760bfae7e10d3333596788dbc52ef2f294`
