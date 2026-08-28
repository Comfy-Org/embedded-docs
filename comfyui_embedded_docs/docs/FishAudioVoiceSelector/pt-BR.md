# FishAudioVoiceSelector

O nó Fish Audio Voice Selector seleciona uma voz da biblioteca Fish Audio para geração de texto para fala. Você pode escolher uma das vozes predefinidas incorporadas ou selecionar "custom" para inserir qualquer ID de modelo de voz do fish.audio.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `voice` | Escolha uma voz, ou 'custom' para inserir qualquer ID de modelo de voz do fish.audio. | DYNAMIC_COMBO | Sim | "Energetic Male (en)"<br>"Friendly Women (en)"<br>"Sarah (en)"<br>"Verity (en)"<br>"Polo (en)"<br>"Adrian (en)"<br>"E-girl (en)"<br>"Narrator (en)"<br>"Warm Conversational Voice (en)"<br>"Warm Storyteller (en)"<br>"Dramatic Character Male (en)"<br>"News Narrator (zh)"<br>"Lively Female (zh)"<br>"Gentle Female (zh)"<br>"Energetic Female (ja)"<br>"Calm Female (ja)"<br>"Calm Male (ja)"<br>"custom" |

As opções de voz predefinidas cobrem vozes em inglês (en), chinês (zh) e japonês (ja) e não exigem nenhuma entrada adicional.

### Entradas personalizadas

Estas entradas aparecem quando `voice` é definido como "custom".

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `voice_id` | ID do modelo de voz do fish.audio, ex.: o ID em https://fish.audio/m/<id>/. Padrão: string vazia. | STRING | Sim | Qualquer ID de modelo de voz válido do Fish Audio |

Nota: Quando `voice` é definido como "custom", `voice_id` não pode ficar vazio após a remoção de espaços em branco; caso contrário, o nó gera um erro "Custom voice ID is empty." Se uma opção de voz não reconhecida for passada, o nó gera um erro "Unknown voice".

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `voice` | O ID do modelo de voz do Fish Audio selecionado. Para uma voz predefinida, o ID de voz correspondente da biblioteca Fish Audio é retornado; para "custom", o valor de `voice_id` inserido é retornado. | FISHAUDIO_VOICE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioVoiceSelector/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4f99a58aa7e6054f58fe84e61e4e1008b17828bd97d71ef0a4009c4de4052bbd`
