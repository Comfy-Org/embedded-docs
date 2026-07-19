# Sampler AR Video

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerARVideo/en.md)

O nó Amostrador de Vídeo AR fornece um método de amostragem especializado para modelos de vídeo autorregressivos, como aqueles que utilizam técnicas de Forçagem Causal ou Auto-Forçagem. Ele gerencia todos os parâmetros relacionados ao loop autorregressivo (AR) diretamente no fluxo de trabalho, facilitando a configuração de como o modelo gera quadros de vídeo um passo de cada vez.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `num_frame_per_block` | Quadros por bloco autorregressivo. Um valor de 1 significa que o modelo gera um quadro por vez (quadro a quadro), enquanto um valor de 3 significa que ele gera três quadros juntos (por bloco). Esta configuração deve corresponder ao modo de treinamento do checkpoint. Padrão: 1. | INT | Sim | 1 a 64 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `SAMPLER` | Um objeto amostrador configurado que utiliza a função de amostragem "ar_video" com os parâmetros autorregressivos especificados. | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerARVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5b735f98fdde074ee9483503fee0e2322d510aed846336b382a8ea89a363c9e4`
