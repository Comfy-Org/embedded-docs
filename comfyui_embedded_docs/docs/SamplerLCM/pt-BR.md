# SamplerLCM

O nó SamplerLCM fornece um amostrador LCM (Modelo de Consistência Latente) com parâmetros de ruído ajustáveis por etapa. Ele permite controlar o ruído aplicado em cada etapa do processo de amostragem; `s_noise` é um multiplicador da escala de ruído de treinamento do modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `s_noise` | Multiplicador de ruído por etapa na primeira etapa (1.0 = corresponder ao treinamento). (padrão: 1.0) | FLOAT | Sim | 0.0 a 64.0 (step: 0.01) |
| `s_noise_end` | Multiplicador de ruído por etapa na última etapa. Defina igual a `s_noise` para uma agenda de ruído constante. (padrão: 1.0) | FLOAT | Sim | 0.0 a 64.0 (step: 0.01) |
| `noise_clip_std` | Limita o ruído por etapa a +/- N*std. 0 desativa. (padrão: 0.0) | FLOAT | Sim | 0.0 a 10.0 (step: 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `SAMPLER` | O objeto amostrador LCM configurado, pronto para ser usado em um fluxo de trabalho de amostragem. | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0d18f2f977ddadeedcd7807233b48ebcc4e94c6213f8540b9037a45a9c70c6cf`
