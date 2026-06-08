O nó SamplerLCM fornece um amostrador LCM (Modelo de Consistência Latente) com parâmetros de ruído ajustáveis por etapa. Ele permite controlar o ruído aplicado em cada etapa de amostragem, possibilitando um ajuste fino do processo de amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `s_noise` | Multiplicador de ruído por etapa na primeira etapa. Um valor de 1.0 corresponde à escala de ruído de treinamento do modelo. (padrão: 1.0) | FLOAT | Sim | 0.0 a 64.0 (passo: 0.01) |
| `s_noise_end` | Multiplicador de ruído por etapa na última etapa. Defina como igual a `s_noise` para uma programação de ruído constante. (padrão: 1.0) | FLOAT | Sim | 0.0 a 64.0 (passo: 0.01) |
| `noise_clip_std` | Limita o ruído por etapa a dentro de +/- N desvios padrão. Um valor de 0 desativa a limitação. (padrão: 0.0) | FLOAT | Sim | 0.0 a 10.0 (passo: 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `SAMPLER` | O objeto amostrador LCM configurado, pronto para ser usado em um fluxo de trabalho de amostragem. | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e6f9007f66625baeee8850018784187cf45117591c443f117c593eef547ada98`
