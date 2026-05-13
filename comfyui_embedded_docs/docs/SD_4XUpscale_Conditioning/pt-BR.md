> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/pt-BR.md)

O nó **SD_4XUpscale_Conditioning** prepara dados de condicionamento para ampliar imagens usando modelos de difusão. Ele recebe imagens de entrada e dados de condicionamento, aplica escalonamento e aumento de ruído para criar condicionamento modificado que guia o processo de ampliação. O nó gera tanto condicionamento positivo quanto negativo, juntamente com representações latentes para as dimensões ampliadas.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `images` | IMAGE | Sim | - | Imagens de entrada a serem ampliadas |
| `positive` | CONDITIONING | Sim | - | Dados de condicionamento positivo que guiam a geração em direção ao conteúdo desejado |
| `negative` | CONDITIONING | Sim | - | Dados de condicionamento negativo que afastam a geração de conteúdo indesejado |
| `scale_ratio` | FLOAT | Não | 0.0 - 10.0 | Fator de escalonamento aplicado às imagens de entrada (padrão: 4.0) |
| `noise_augmentation` | FLOAT | Não | 0.0 - 1.0 | Quantidade de ruído a ser adicionada durante o processo de ampliação (padrão: 0.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `positive` | CONDITIONING | Condicionamento positivo modificado com informações de ampliação aplicadas |
| `negative` | CONDITIONING | Condicionamento negativo modificado com informações de ampliação aplicadas |
| `latent` | LATENT | Representação latente vazia correspondente às dimensões ampliadas |

---
**Source fingerprint (SHA-256):** `ede1ea8f5a95e7f9e52070b5132a4ed3e87f92230d14a74b9d713f547c74d785`
