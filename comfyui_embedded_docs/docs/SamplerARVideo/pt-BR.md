# Sampler AR Video

O nó Sampler AR Video fornece um método de amostragem especializado para modelos de vídeo autorregressivos, como aqueles que usam técnicas de Causal Forcing ou Self-Forcing. Ele gerencia todos os parâmetros relacionados ao loop autorregressivo (AR) diretamente no fluxo de trabalho, facilitando a configuração de como o modelo gera quadros de vídeo passo a passo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `num_frame_per_block` | Quadros por bloco autorregressivo. Um valor de 1 significa que o modelo gera um quadro por vez (quadro a quadro), enquanto um valor de 3 significa que gera três quadros juntos (em blocos). Esta definição deve corresponder ao modo de treinamento do checkpoint. Padrão: 1. | INT | Sim | 1 a 64 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `SAMPLER` | Um objeto de amostrador configurado que usa a função de amostragem "ar_video" com os parâmetros autorregressivos especificados. | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerARVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9ec72f52f5b77746f1587e64966bfa6cfd80ce8bb40a4fcb267f5197d09189fc`
