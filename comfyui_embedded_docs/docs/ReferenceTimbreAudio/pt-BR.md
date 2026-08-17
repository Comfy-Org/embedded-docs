# ReferenceTimbreAudio

Este nó define um timbre de áudio de referência para uso no processo "ace step 1.5". Ele recebe um condicionamento de entrada e uma representação latente opcional do áudio e, em seguida, anexa esses dados latentes ao condicionamento para que nós posteriores no fluxo de trabalho possam usá-los como áudio de referência. Se nenhum latente for fornecido, o condicionamento é retornado inalterado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `conditioning` | Os dados de condicionamento aos quais as informações do timbre de áudio de referência serão anexadas. | CONDITIONING | Sim |  |
| `latent` | Uma representação latente opcional do áudio de referência. Quando fornecida, suas amostras são adicionadas ao condicionamento. | LATENT | Não |  |

Quando a entrada `latent` é fornecida, suas amostras são anexadas aos latentes de timbre de áudio de referência do condicionamento. Se nenhuma entrada `latent` for fornecida, o condicionamento original é passado adiante inalterado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `conditioning` | Os dados de condicionamento modificados, agora contendo os latentes de timbre de áudio de referência, caso a entrada opcional `latent` tenha sido fornecida. Se nenhum latente for fornecido, o condicionamento original é retornado inalterado. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2ddccb7676fc45a5324ba32dde0cd2f8f24388ceec20c88a475e1aa9d4276be0`
