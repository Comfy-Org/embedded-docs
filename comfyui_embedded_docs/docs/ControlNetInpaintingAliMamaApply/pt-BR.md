> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/pt-BR.md)

O nó ControlNetInpaintingAliMamaApply aplica o condicionamento ControlNet para tarefas de inpaint, combinando condicionamentos positivo e negativo com uma imagem de controle e máscara. Ele processa a imagem de entrada e a máscara para criar condicionamentos modificados que guiam o processo de geração, permitindo controle preciso sobre quais áreas da imagem serão inpaintadas. O nó suporta ajuste de intensidade e controles de temporização para ajustar a influência do ControlNet durante diferentes estágios do processo de geração.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `positivo` | CONDITIONING | Sim | - | O condicionamento positivo que guia a geração em direção ao conteúdo desejado |
| `negativo` | CONDITIONING | Sim | - | O condicionamento negativo que afasta a geração de conteúdo indesejado |
| `control_net` | CONTROL_NET | Sim | - | O modelo ControlNet que fornece controle adicional sobre a geração |
| `vae` | VAE | Sim | - | O VAE (Autoencoder Variacional) usado para codificar e decodificar imagens |
| `imagem` | IMAGE | Sim | - | A imagem de entrada que serve como guia de controle para o ControlNet |
| `mask` | MASK | Sim | - | A máscara que define quais áreas da imagem devem ser inpaintadas |
| `força` | FLOAT | Sim | 0.0 a 10.0 | A intensidade do efeito do ControlNet (padrão: 1.0) |
| `percentual_inicial` | FLOAT | Sim | 0.0 a 1.0 | O ponto inicial (como porcentagem) em que a influência do ControlNet começa durante a geração (padrão: 0.0) |
| `percentual_final` | FLOAT | Sim | 0.0 a 1.0 | O ponto final (como porcentagem) em que a influência do ControlNet termina durante a geração (padrão: 1.0) |

**Nota:** Quando o ControlNet tem `concat_mask` ativado, a máscara é invertida e aplicada à imagem antes do processamento, e a máscara é incluída nos dados extras de concatenação enviados ao ControlNet.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positivo` | CONDITIONING | O condicionamento positivo modificado com ControlNet aplicado para inpaint |
| `negativo` | CONDITIONING | O condicionamento negativo modificado com ControlNet aplicado para inpaint |

---
**Source fingerprint (SHA-256):** `30b49991b5ead039122a282fb48e3ed30477f89ce1430c371529bc42f921020d`
