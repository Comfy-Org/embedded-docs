Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/en.md)

Este nó define um timbre de áudio de referência para uso no processo "ace step 1.5". Ele funciona recebendo uma entrada de condicionamento e, opcionalmente, uma representação latente de áudio, e então anexa esses dados latentes ao condicionamento para uso por nós subsequentes no fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `condicionamento` | Os dados de condicionamento aos quais as informações do áudio de referência serão anexadas. | CONDITIONING | Sim |  |
| `latente` | Uma representação latente opcional do áudio de referência. Quando fornecida, suas amostras são adicionadas ao condicionamento. | LATENT | Não |  |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `condicionamento` | Os dados de condicionamento modificados, agora contendo os latentes do timbre de áudio de referência se a entrada opcional `latente` foi fornecida. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceTimbreAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2d39399eb79cfe76b72d01326b89863e2553bc23414b1166d310e5222b215b29`
