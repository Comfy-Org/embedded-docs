# LTXV Reference Audio (ID-LoRA)

O LTXV Reference Audio transfere a identidade vocal de um locutor de um clipe de áudio de referência para o áudio gerado. Ele codifica o áudio de referência no condicionamento e, opcionalmente, aplica um patch no modelo com orientação de identidade, que executa uma passagem direta extra sem a referência a cada etapa para amplificar o efeito de identidade do locutor.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo a ser modificado com orientação de identidade. | MODEL | Sim | - |
| `positivo` | A entrada de condicionamento positiva. | CONDITIONING | Sim | - |
| `negativo` | A entrada de condicionamento negativa. | CONDITIONING | Sim | - |
| `áudio_de_referência` | Clipe de áudio de referência cuja identidade do locutor deve ser transferida. Recomenda-se cerca de 5 segundos (duração do treinamento). Clipes mais curtos ou mais longos podem degradar a transferência de identidade vocal. | AUDIO | Sim | - |
| `audio_vae` | VAE de áudio LTXV para codificação. | VAE | Sim | - |
| `escala_de_orientação_de_identidade` | Intensidade da orientação de identidade. Executa uma passagem direta extra sem a referência a cada etapa para amplificar a identidade do locutor. Defina como 0 para desativar (sem passagem extra). (padrão: 3.0) | FLOAT | Sim | 0.0 - 100.0 |
| `percentual_inicial` | Início da faixa de sigma onde a orientação de identidade está ativa. (padrão: 0.0) | FLOAT | Sim | 0.0 - 1.0 |
| `percentual_final` | Fim da faixa de sigma onde a orientação de identidade está ativa. (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |

Nota: A orientação de identidade só é aplicada quando `identity_guidance_scale` é maior que 0 e a etapa atual de amostragem está dentro da faixa definida por `start_percent` e `end_percent`. O áudio de referência é reamostrado para a taxa de amostragem do VAE de áudio se as duas forem diferentes.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com a função de orientação de identidade. | MODEL |
| `positivo` | O condicionamento positivo, agora contendo os dados de áudio de referência codificados. | CONDITIONING |
| `negativo` | O condicionamento negativo, agora contendo os dados de áudio de referência codificados. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ae15c5838656324667d099614b325b863341f05afda43054658999574522dd49`
