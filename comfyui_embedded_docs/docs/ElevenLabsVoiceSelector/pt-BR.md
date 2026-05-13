> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsVoiceSelector/pt-BR.md)

O nó **Seletor de Voz ElevenLabs** permite que você escolha uma voz específica de uma lista predefinida de vozes de texto-para-fala da ElevenLabs. Ele recebe um nome de voz como entrada e retorna o identificador de voz correspondente necessário para a geração de áudio. Este nó simplifica o processo de seleção de uma voz compatível para uso com outros nós de áudio da ElevenLabs.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `voice` | STRING | Sim | `"Adam"`<br>`"Antoni"`<br>`"Arnold"`<br>`"Bella"`<br>`"Domi"`<br>`"Elli"`<br>`"Josh"`<br>`"Rachel"`<br>`"Sam"` | Escolha uma voz dentre as vozes predefinidas da ElevenLabs. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `voice` | STRING | O identificador único para a voz selecionada da ElevenLabs, que pode ser passado para outros nós para geração de texto-para-fala. |

---
**Source fingerprint (SHA-256):** `b87f5b2b8accca87d0593ab1f4bcfccaa84b393ddb3fd9121758a87871592cee`
