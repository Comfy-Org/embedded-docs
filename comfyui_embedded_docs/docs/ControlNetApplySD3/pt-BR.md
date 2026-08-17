# Aplicar Controlnet com VAE

Este nó aplica a orientação do ControlNet ao condicionamento do Stable Diffusion 3. Ele recebe entradas de condicionamento positivo e negativo, juntamente com um modelo ControlNet e uma imagem, e então aplica a orientação de controle com parâmetros ajustáveis de intensidade e temporização para influenciar o processo de geração.

**Nota:** Este nó foi marcado como obsoleto e pode ser removido em versões futuras.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | O condicionamento positivo ao qual aplicar a orientação do ControlNet | CONDITIONING | Sim | - |
| `negative` | O condicionamento negativo ao qual aplicar a orientação do ControlNet | CONDITIONING | Sim | - |
| `control_net` | O modelo ControlNet a ser usado para orientação | CONTROL_NET | Sim | - |
| `vae` | O modelo VAE usado no processo | VAE | Sim | - |
| `image` | A imagem de entrada que o ControlNet usará como orientação | IMAGE | Sim | - |
| `strength` | A intensidade do efeito do ControlNet (padrão: 1.0) | FLOAT | Sim | 0.0 - 10.0 |
| `start_percent` | O ponto inicial no processo de geração em que o ControlNet começa a ser aplicado (padrão: 0.0) | FLOAT | Sim | 0.0 - 1.0 |
| `end_percent` | O ponto final no processo de geração em que o ControlNet deixa de ser aplicado (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |

**Nota:** Quando `strength` é definido como 0, o nó retorna o condicionamento positivo e negativo inalterado, sem aplicar o ControlNet.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positive` | O condicionamento positivo modificado com a orientação do ControlNet aplicada | CONDITIONING |
| `negative` | O condicionamento negativo modificado com a orientação do ControlNet aplicada | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b76b0683c05e38102280ca8b0bd23f39a9b9b1b4f52125c77c95686c0a06f398`
