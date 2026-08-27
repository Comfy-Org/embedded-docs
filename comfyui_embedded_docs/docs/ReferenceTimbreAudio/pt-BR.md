# ReferenceTimbreAudio

Este nó define um timbre de áudio de referência para uso no processo "ace step 1.5". Ele funciona recebendo uma entrada de condicionamento e, opcionalmente, uma representação latente do áudio, e então anexa esses dados latentes ao condicionamento para uso por nós subsequentes no fluxo de trabalho. Este nó está atualmente marcado como experimental.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `condicionamento` | Os dados de condicionamento aos quais as informações de áudio de referência serão anexadas. | CONDITIONING | Sim |  |
| `latente` | Uma representação latente opcional do áudio de referência. Quando fornecida, suas amostras são adicionadas (anexadas) ao condicionamento para que possam ser usadas como latentes de timbre de áudio de referência. | LATENT | Não |  |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `conditioning` | Os dados de condicionamento modificados, agora contendo os latentes de timbre de áudio de referência, caso a entrada opcional `latent` tenha sido fornecida. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`
