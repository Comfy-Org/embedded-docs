> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsAudioIsolation/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsAudioIsolation/en.md)

O nó de Isolamento de Voz ElevenLabs remove o ruído de fundo de um arquivo de áudio, isolando os vocais ou a fala. Ele envia o áudio para a API ElevenLabs para processamento e retorna o áudio limpo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `áudio` | AUDIO | Sim | | Áudio a ser processado para remoção de ruído de fundo. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `áudio` | AUDIO | O áudio processado com o ruído de fundo removido. |

---
**Source fingerprint (SHA-256):** `eca7919ff853fe48f8419a4135a99589e350d3d113631e27f6e7cb3cbb3faa3b`
