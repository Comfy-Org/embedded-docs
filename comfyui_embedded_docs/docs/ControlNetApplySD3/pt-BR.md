# Aplicar Controlnet com VAE

Este nó aplica a orientação do ControlNet ao condicionamento do Stable Diffusion 3. Ele recebe entradas de condicionamento positivo e negativo, juntamente com um modelo ControlNet e uma imagem, e então aplica a orientação com parâmetros ajustáveis de força e temporização para influenciar o processo de geração.

**Nota:** Este nó foi marcado como obsoleto e pode ser removido em versões futuras.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | O condicionamento positivo para aplicar a orientação do ControlNet | CONDITIONING | Sim | - |
| `negativo` | O condicionamento negativo para aplicar a orientação do ControlNet | CONDITIONING | Sim | - |
| `control_net` | O modelo ControlNet a ser usado para a orientação | CONTROL_NET | Sim | - |
| `vae` | O modelo VAE usado no processo | VAE | Sim | - |
| `imagem` | A imagem de entrada que o ControlNet usará como orientação | IMAGE | Sim | - |
| `força` | A força do efeito do ControlNet (padrão: 1.0). Quando definido como 0.0, o nó pula a aplicação do ControlNet e retorna o condicionamento inalterado. | FLOAT | Sim | 0.0 - 10.0 |
| `percentual_inicial` | O ponto inicial no processo de geração em que o ControlNet começa a ser aplicado (padrão: 0.0) | FLOAT | Sim | 0.0 - 1.0 |
| `percentual_final` | O ponto final no processo de geração em que o ControlNet para de ser aplicado (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |

**Nota:** Quando `strength` é definido como 0.0, nenhuma orientação do ControlNet é aplicada e o condicionamento de entrada é passado inalterado para ambas as saídas.

**Nota:** Se o mesmo condicionamento for reutilizado em outro lugar e já contiver informações de controle, o novo ControlNet é vinculado após o anterior, de modo que vários ControlNets podem ser aplicados em sequência.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | O condicionamento positivo modificado com a orientação do ControlNet aplicada | CONDITIONING |
| `negativo` | O condicionamento negativo modificado com a orientação do ControlNet aplicada | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b76b0683c05e38102280ca8b0bd23f39a9b9b1b4f52125c77c95686c0a06f398`
