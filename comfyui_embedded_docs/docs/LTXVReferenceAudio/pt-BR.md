# LTXV Reference Audio (ID-LoRA)

O nó LTXV Reference Audio define um clipe de áudio de referência para a transferência de identidade do locutor via ID-LoRA na geração de áudio. Ele codifica o clipe no condicionamento para que o áudio gerado adote as características de voz do locutor e, opcionalmente, aplica um patch no modelo com orientação de identidade, o que executa uma passagem direta extra sem a referência para amplificar o efeito de identidade do locutor.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo a ser modificado com a orientação de identidade. | MODEL | Sim | - |
| `positive` | A entrada de condicionamento positivo. | CONDITIONING | Sim | - |
| `negative` | A entrada de condicionamento negativo. | CONDITIONING | Sim | - |
| `reference_audio` | Clipe de áudio de referência cuja identidade de locutor deve ser transferida. Recomenda-se cerca de 5 segundos (duração do treinamento). Clipes mais curtos ou mais longos podem degradar a transferência de identidade de voz. | AUDIO | Sim | - |
| `audio_vae` | LTXV Audio VAE para codificação. | VAE | Sim | - |
| `identity_guidance_scale` | Força da orientação de identidade. Executa uma passagem direta extra sem a referência a cada etapa para amplificar a identidade do locutor. Defina para 0 para desativar (sem passagem extra). (padrão: 3.0) | FLOAT | Não | 0.0 - 100.0 |
| `start_percent` | Início do intervalo de sigma em que a orientação de identidade está ativa. (padrão: 0.0) | FLOAT | Não | 0.0 - 1.0 |
| `end_percent` | Fim do intervalo de sigma em que a orientação de identidade está ativa. (padrão: 1.0) | FLOAT | Não | 0.0 - 1.0 |

Nota: a orientação de identidade só fica ativa para valores de sigma dentro do intervalo definido por `start_percent` e `end_percent`; fora desse intervalo, a saída de denoising permanece inalterada. O áudio de referência é adicionado tanto ao condicionamento positivo quanto ao negativo. Se a taxa de amostragem do áudio de referência for diferente da taxa de amostragem do VAE de áudio, o áudio é reamostrado automaticamente para corresponder ao VAE.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com a função de orientação de identidade. | MODEL |
| `positive` | O condicionamento positivo, agora contendo os dados codificados do áudio de referência. | CONDITIONING |
| `negative` | O condicionamento negativo, agora contendo os dados codificados do áudio de referência. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ae15c5838656324667d099614b325b863341f05afda43054658999574522dd49`
