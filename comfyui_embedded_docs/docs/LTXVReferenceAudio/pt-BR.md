# LTXV Reference Audio (ID-LoRA)

LTXV Reference Audio transfere a identidade vocal de um falante de um clipe de áudio de referência para o áudio gerado. Ele codifica o áudio de referência no condicionamento e, opcionalmente, aplica um patch ao modelo com orientação de identidade, que executa uma passagem forward extra sem a referência a cada etapa para amplificar o efeito da identidade do falante.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo ao qual será aplicado o patch com orientação de identidade. | MODEL | Sim | - |
| `positive` | A entrada de condicionamento positiva. | CONDITIONING | Sim | - |
| `negative` | A entrada de condicionamento negativa. | CONDITIONING | Sim | - |
| `reference_audio` | Clipe de áudio de referência cuja identidade do falante será transferida. Recomenda-se ~5 segundos (duração de treinamento). Clipes mais curtos ou mais longos podem degradar a transferência de identidade vocal. | AUDIO | Sim | - |
| `audio_vae` | VAE de áudio LTXV para codificação. | VAE | Sim | - |
| `identity_guidance_scale` | Força da orientação de identidade. Executa uma passagem forward extra sem referência a cada etapa para amplificar a identidade do falante. Defina como 0 para desabilitar (sem passagem extra). (padrão: 3.0) | FLOAT | Sim | 0.0 - 100.0 |
| `start_percent` | Início do intervalo de sigma em que a orientação de identidade está ativa. (padrão: 0.0) | FLOAT | Sim | 0.0 - 1.0 |
| `end_percent` | Fim do intervalo de sigma em que a orientação de identidade está ativa. (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |

Nota: A orientação de identidade só é aplicada quando `identity_guidance_scale` for maior que 0 e a etapa de amostragem atual estiver dentro do intervalo definido por `start_percent` e `end_percent`. O áudio de referência é reamostrado para a taxa de amostragem do VAE de áudio se as duas forem diferentes.

Nota: `start_percent` e `end_percent` são parâmetros avançados, exibidos apenas quando as opções avançadas estão habilitadas na interface.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo com o patch da função de orientação de identidade. | MODEL |
| `positive` | O condicionamento positivo, agora contendo os dados de áudio de referência codificados. | CONDITIONING |
| `negative` | O condicionamento negativo, agora contendo os dados de áudio de referência codificados. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ae15c5838656324667d099614b325b863341f05afda43054658999574522dd49`
