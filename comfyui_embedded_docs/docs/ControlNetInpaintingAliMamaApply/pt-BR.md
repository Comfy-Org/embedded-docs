O nó ControlNetInpaintingAliMamaApply aplica o condicionamento ControlNet para tarefas de inpaint, combinando condicionamentos positivo e negativo com uma imagem de controle e máscara. Ele processa a imagem de entrada e a máscara para criar condicionamentos modificados que guiam o processo de geração, permitindo controle preciso sobre quais áreas da imagem serão inpaintadas. O nó suporta ajuste de intensidade e controles de temporização para ajustar a influência do ControlNet durante diferentes estágios do processo de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | O condicionamento positivo que guia a geração em direção ao conteúdo desejado | CONDITIONING | Sim | - |
| `negativo` | O condicionamento negativo que afasta a geração de conteúdo indesejado | CONDITIONING | Sim | - |
| `control_net` | O modelo ControlNet que fornece controle adicional sobre a geração | CONTROL_NET | Sim | - |
| `vae` | O VAE (Autoencoder Variacional) usado para codificar e decodificar imagens | VAE | Sim | - |
| `imagem` | A imagem de entrada que serve como guia de controle para o ControlNet | IMAGE | Sim | - |
| `mask` | A máscara que define quais áreas da imagem devem ser inpaintadas | MASK | Sim | - |
| `força` | A intensidade do efeito do ControlNet (padrão: 1.0) | FLOAT | Sim | 0.0 a 10.0 |
| `percentual_inicial` | O ponto inicial (como porcentagem) em que a influência do ControlNet começa durante a geração (padrão: 0.0) | FLOAT | Sim | 0.0 a 1.0 |
| `percentual_final` | O ponto final (como porcentagem) em que a influência do ControlNet termina durante a geração (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |

**Nota:** Quando o ControlNet tem `concat_mask` ativado, a máscara é invertida e aplicada à imagem antes do processamento, e a máscara é incluída nos dados extras de concatenação enviados ao ControlNet.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | O condicionamento positivo modificado com ControlNet aplicado para inpaint | CONDITIONING |
| `negativo` | O condicionamento negativo modificado com ControlNet aplicado para inpaint | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/pt-BR.md)

---
**Source fingerprint (SHA-256):** `30b49991b5ead039122a282fb48e3ed30477f89ce1430c371529bc42f921020d`
