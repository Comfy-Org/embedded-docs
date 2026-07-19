# HeyGenTextToSpeechNode

Gere áudio de fala a partir de texto usando o mecanismo TTS Starfish da HeyGen. Este nó inclui as vozes mais populares da HeyGen em 17 idiomas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `text` | Texto a ser sintetizado (até 5000 caracteres). A fala gerada deve ter pelo menos 1 segundo de duração. | STRING | Sim | 1 a 5000 caracteres |
| `voice` | Voz a ser usada (selecionada entre as vozes compatíveis com Starfish mais populares da HeyGen). | STRING | Sim | Múltiplas opções disponíveis |
| `custom_voice_id` | ID de voz opcional da HeyGen. Quando definido, substitui a voz selecionada acima. A voz deve ser compatível com o mecanismo Starfish. | STRING | Não | Qualquer ID de voz válido da HeyGen |
| `speed` | Multiplicador de velocidade da fala (padrão: 1.0). | FLOAT | Não | 0.5 a 2.0 (passo: 0.05) |
| `ssml` | Tratar o texto como marcação SSML (para controle de pausas, ênfase e pronúncia) (padrão: Falso). | BOOLEAN | Não | Verdadeiro / Falso |
| `seed` | Não é enviado para a HeyGen; altere-o para forçar uma nova execução (padrão: 42). | INT | Não | 0 a 2147483647 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `AUDIO` | O áudio de fala sintetizado gerado a partir do texto de entrada. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenTextToSpeechNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `82300626657db8ab16e96ae96b7dfe3291b77bf75efec35971dc772e5123cce7`
