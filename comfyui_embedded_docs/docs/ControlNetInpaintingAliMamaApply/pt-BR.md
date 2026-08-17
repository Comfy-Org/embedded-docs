# Aplicar ControlNetInpaintingAliMama

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positive` | O condicionamento positivo que orienta a geração em direção ao conteúdo desejado. | CONDITIONING | Sim | - |
| `negative` | O condicionamento negativo que orienta a geração para longe de conteúdo indesejado. | CONDITIONING | Sim | - |
| `control_net` | O modelo ControlNet que fornece controle adicional sobre a geração. | CONTROL_NET | Sim | - |
| `vae` | O VAE usado para codificar e decodificar imagens. | VAE | Sim | - |
| `image` | A imagem de entrada usada como orientação de controle para o ControlNet. | IMAGE | Sim | - |
| `mask` | A máscara que define quais áreas da imagem devem receber inpainting. | MASK | Sim | - |
| `strength` | A intensidade do efeito do ControlNet (padrão: 1.0). | FLOAT | Sim | 0.0 a 10.0 |
| `start_percent` | Opção avançada. A fração do processo de geração em que a influência do ControlNet começa (padrão: 0.0). | FLOAT | Sim | 0.0 a 1.0 |
| `end_percent` | Opção avançada. A fração do processo de geração em que a influência do ControlNet termina (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 |

**Nota:** Quando o ControlNet selecionado estiver com `concat_mask` ativado, os valores da máscara são invertidos (1 - mask), uma versão redimensionada da máscara invertida é aplicada à imagem e a máscara invertida é incluída nos dados extras de concatenação passados ao ControlNet. Se `concat_mask` estiver desativado, a entrada `mask` não é usada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | O condicionamento positivo modificado com o ControlNet aplicado para inpainting. | CONDITIONING |
| `negative` | O condicionamento negativo modificado com o ControlNet aplicado para inpainting. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/pt-BR.md)

---
**Source fingerprint (SHA-256):** `307b55c7b4936826b9e4424c172248fa4b41921c2362de724e5cfa2f1c25de68`
