> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplySD3/pt-BR.md)

Este nó aplica orientação ControlNet ao condicionamento do Stable Diffusion 3. Ele recebe entradas de condicionamento positivo e negativo, juntamente com um modelo ControlNet e uma imagem, e então aplica a orientação de controle com parâmetros ajustáveis de força e temporização para influenciar o processo de geração.

**Nota:** Este nó foi marcado como obsoleto e pode ser removido em versões futuras.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | O condicionamento positivo ao qual aplicar a orientação ControlNet |
| `negative` | CONDITIONING | Sim | - | O condicionamento negativo ao qual aplicar a orientação ControlNet |
| `control_net` | CONTROL_NET | Sim | - | O modelo ControlNet a ser usado para orientação |
| `vae` | VAE | Sim | - | O modelo VAE usado no processo |
| `image` | IMAGE | Sim | - | A imagem de entrada que o ControlNet usará como orientação |
| `strength` | FLOAT | Sim | 0.0 - 10.0 | A força do efeito ControlNet (padrão: 1.0) |
| `start_percent` | FLOAT | Sim | 0.0 - 1.0 | O ponto de início no processo de geração onde o ControlNet começa a ser aplicado (padrão: 0.0) |
| `end_percent` | FLOAT | Sim | 0.0 - 1.0 | O ponto de término no processo de geração onde o ControlNet para de ser aplicado (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | O condicionamento positivo modificado com a orientação ControlNet aplicada |
| `negative` | CONDITIONING | O condicionamento negativo modificado com a orientação ControlNet aplicada |
