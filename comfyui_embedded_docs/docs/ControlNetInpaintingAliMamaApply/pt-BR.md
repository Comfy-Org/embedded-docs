# Aplicar ControlNetInpaintingAliMama

O nó ControlNetInpaintingAliMamaApply aplica condicionamento do ControlNet para tarefas de inpainting ao combinar o condicionamento positivo e negativo com uma imagem de controle e uma máscara. Ele processa a imagem e a máscara de entrada para criar um condicionamento modificado que orienta o processo de geração, permitindo controle preciso sobre quais áreas da imagem passarão por inpainting. O nó suporta ajuste de força e controles de tempo para ajustar finamente a influência do ControlNet durante diferentes estágios do processo de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | O condicionamento positivo que orienta a geração em direção ao conteúdo desejado | CONDITIONING | Sim | - |
| `negativo` | O condicionamento negativo que afasta a geração de conteúdo indesejado | CONDITIONING | Sim | - |
| `control_net` | O modelo ControlNet que fornece controle adicional sobre a geração | CONTROL_NET | Sim | - |
| `vae` | O VAE (Autoencoder Variacional) usado para codificar e decodificar imagens | VAE | Sim | - |
| `imagem` | A imagem de entrada que serve como orientação de controle para o ControlNet | IMAGE | Sim | - |
| `mask` | A máscara que define quais áreas da imagem devem passar por inpainting | MASK | Sim | - |
| `força` | A força do efeito do ControlNet (padrão: 1.0, passo: 0.01) | FLOAT | Sim | 0.0 a 10.0 |
| `percentual_inicial` | Parâmetro avançado. O ponto inicial (em porcentagem) em que a influência do ControlNet começa durante a geração (padrão: 0.0, passo: 0.001) | FLOAT | Sim | 0.0 a 1.0 |
| `percentual_final` | Parâmetro avançado. O ponto final (em porcentagem) em que a influência do ControlNet cessa durante a geração (padrão: 1.0, passo: 0.001) | FLOAT | Sim | 0.0 a 1.0 |

**Nota:** Quando o ControlNet está com `concat_mask` habilitado, a máscara é invertida e aplicada à imagem antes do processamento, e a máscara invertida é incluída nos dados extras de concatenação enviados ao ControlNet.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | O condicionamento positivo modificado com o ControlNet aplicado para inpainting | CONDITIONING |
| `negativo` | O condicionamento negativo modificado com o ControlNet aplicado para inpainting | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/pt-BR.md)

---
**Source fingerprint (SHA-256):** `307b55c7b4936826b9e4424c172248fa4b41921c2362de724e5cfa2f1c25de68`
