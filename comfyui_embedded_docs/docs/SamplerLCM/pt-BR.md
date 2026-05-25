> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/pt-BR.md)

O nó SamplerLCM fornece um amostrador LCM (Modelo de Consistência Latente) com parâmetros de ruído ajustáveis por etapa. Ele permite controlar o ruído aplicado em cada etapa de amostragem, possibilitando um ajuste fino do processo de amostragem.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `s_noise` | FLOAT | Sim | 0.0 a 64.0 (passo: 0.01) | Multiplicador de ruído por etapa na primeira etapa. Um valor de 1.0 corresponde à escala de ruído de treinamento do modelo. (padrão: 1.0) |
| `s_noise_end` | FLOAT | Sim | 0.0 a 64.0 (passo: 0.01) | Multiplicador de ruído por etapa na última etapa. Defina como igual a `s_noise` para uma programação de ruído constante. (padrão: 1.0) |
| `noise_clip_std` | FLOAT | Sim | 0.0 a 10.0 (passo: 0.01) | Limita o ruído por etapa a dentro de +/- N desvios padrão. Um valor de 0 desativa a limitação. (padrão: 0.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `SAMPLER` | SAMPLER | O objeto amostrador LCM configurado, pronto para ser usado em um fluxo de trabalho de amostragem. |

---
**Source fingerprint (SHA-256):** `e6f9007f66625baeee8850018784187cf45117591c443f117c593eef547ada98`
