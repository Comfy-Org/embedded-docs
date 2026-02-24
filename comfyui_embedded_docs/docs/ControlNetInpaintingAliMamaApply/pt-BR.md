> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/pt-BR.md)

O nó ControlNetInpaintingAliMamaApply aplica o condicionamento ControlNet para tarefas de inpainting, combinando condicionamentos positivo e negativo com uma imagem de controle e uma máscara. Ele processa a imagem e a máscara de entrada para criar um condicionamento modificado que orienta o processo de geração, permitindo um controle preciso sobre quais áreas da imagem serão preenchidas. O nó suporta ajuste de intensidade e controles de tempo para refinar a influência do ControlNet durante diferentes estágios do processo de geração.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | O condicionamento positivo que orienta a geração em direção ao conteúdo desejado |
| `negative` | CONDITIONING | Sim | - | O condicionamento negativo que orienta a geração para longe de conteúdo indesejado |
| `control_net` | CONTROL_NET | Sim | - | O modelo ControlNet que fornece controle adicional sobre a geração |
| `vae` | VAE | Sim | - | O VAE (Variational Autoencoder) usado para codificar e decodificar imagens |
| `image` | IMAGE | Sim | - | A imagem de entrada que serve como guia de controle para o ControlNet |
| `mask` | MASK | Sim | - | A máscara que define quais áreas da imagem devem ser preenchidas (inpainting) |
| `strength` | FLOAT | Sim | 0.0 a 10.0 | A intensidade do efeito do ControlNet (padrão: 1.0) |
| `start_percent` | FLOAT | Sim | 0.0 a 1.0 | O ponto de início (em porcentagem) de quando a influência do ControlNet começa durante a geração (padrão: 0.0) |
| `end_percent` | FLOAT | Sim | 0.0 a 1.0 | O ponto de término (em porcentagem) de quando a influência do ControlNet para durante a geração (padrão: 1.0) |

**Observação:** Quando o ControlNet tem a opção `concat_mask` habilitada, a máscara é invertida e aplicada à imagem antes do processamento, e a máscara é incluída nos dados de concatenação extras enviados ao ControlNet.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | O condicionamento positivo modificado com o ControlNet aplicado para inpainting |
| `negative` | CONDITIONING | O condicionamento negativo modificado com o ControlNet aplicado para inpainting |
