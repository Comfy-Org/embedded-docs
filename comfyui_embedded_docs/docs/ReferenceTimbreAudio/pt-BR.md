# ReferenceTimbreAudio

Este nó define o áudio de referência para o processo "ace step 1.5". Ele recebe uma entrada de condicionamento e, opcionalmente, uma representação latente de áudio; em seguida, anexa esses dados latentes ao condicionamento para que nós posteriores possam usá-los como latents de timbre de áudio de referência. Este nó está marcado como experimental.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `conditioning` | Os dados de condicionamento aos quais as informações de áudio de referência serão anexadas. | CONDITIONING | Sim |  |
| `latent` | Uma representação latente opcional do áudio de referência (padrão: None). Quando fornecida, suas amostras são anexadas ao condicionamento como latents de timbre de áudio de referência. | LATENT | Não |  |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `conditioning` | Os dados de condicionamento modificados, agora contendo os latents de timbre de áudio de referência se a entrada opcional `latent` tiver sido fornecida. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`
