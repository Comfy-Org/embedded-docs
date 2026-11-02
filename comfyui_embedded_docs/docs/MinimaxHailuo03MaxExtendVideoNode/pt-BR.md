# MiniMax H3 Max Extend Video

Este nó continua um vídeo com novas filmagens guiadas por um prompt e referências de áudio opcionais. O vídeo de origem é enviado, a continuação é gerada, e o resultado é retornado como o vídeo inteiro renderizado novamente ou apenas como as novas filmagens. Dois modelos estão disponíveis: "MiniMax H3 Max" e "MiniMax H3 Max Turbo", que é mais barato por unidade.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo a ser usado para continuar o vídeo. Ambos os modelos expõem as mesmas entradas abaixo. | DYNAMIC_COMBO | Sim | "MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |

### Entradas do modelo

Estas entradas se aplicam a ambos os modelos.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `video` | Vídeo a ser estendido, com duração de 1,625 a 60 segundos, até 50 MB. A proporção de aspecto deve estar entre 0,4 e 2,5. | VIDEO | Sim | 1,625 a 60 segundos |
| `prompt` | O que acontece em seguida. Descreva a continuação, não a origem. Refira-se aos áudios de referência como `@Audio1`..`@Audio3`, por exemplo, "@Audio1 para a voz". | STRING | Sim | 1 a 50000 caracteres |
| `reference_audios` | Slot expansível: conecte até 3 clipes de áudio (`audio_1`...`audio_3`) para as novas filmagens, com pelo menos 2 segundos cada e 14,5 segundos no total. | AUDIO | Não | 0 a 3 clipes |
| `duration` | Segundos de novas filmagens a adicionar (padrão: 5). | INT | Sim | 1 a 15 |
| `resolution` | Resolução do vídeo de saída (padrão: "768P"). | COMBO | Sim | "480P"<br>"768P"<br>"1080P"<br>"2K" |
| `aspect_ratio` | Proporção de aspecto da saída. "auto" segue o vídeo de origem; os outros valores cortam o vídeo para a proporção selecionada (padrão: "auto"). | COMBO | Sim | "auto"<br>"21:9"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16" |
| `output` | "extended" retorna o vídeo inteiro, renderizado novamente na resolução selecionada, com as novas filmagens. "continuation" retorna apenas as novas filmagens, começando com uma repetição de 1,6 segundo do final do vídeo de origem (padrão: "extended"). | COMBO | Sim | "extended"<br>"continuation" |
| `prompt_expansion` | Reescreve o prompt usando o vídeo de origem para manter a continuação consistente. Desative para obter resultados reproduzíveis para a mesma seed (padrão: true). | BOOLEAN | Não | true<br>false |
| `seed` | Seed aleatória. A mesma solicitação com a mesma seed gera resultados semelhantes, mas não necessariamente idênticos (padrão: 42). | INT | Sim | 0 a 4294967295 |

### Restrições dos parâmetros

- Em resolução 2K, a saída "extended" é limitada a 45 segundos no total, vídeo de origem mais novas filmagens. Use "continuation" ou uma resolução menor para clipes mais longos.
- Cada clipe de áudio de referência deve ter pelo menos 2 segundos de duração, e todos juntos não podem exceder 14,5 segundos.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `video` | O vídeo estendido ou apenas as novas filmagens, dependendo da configuração `output`. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxExtendVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `db41a14db392fa450689c8d0d73d38b4ce9ea59ee30cfe4d6d2b0501cf0fc9a8`
