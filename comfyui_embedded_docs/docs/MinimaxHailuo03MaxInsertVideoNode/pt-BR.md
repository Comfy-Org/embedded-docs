# MiniMax H3 Max Insert Video

Este nó substitui a parte de um vídeo entre os tempos de início e de retomada por uma cena recém-gerada, guiada por um prompt e por imagens e vídeos de referência opcionais. O vídeo de origem é cortado em `start_time` e retomado em `resume_time`; o trecho removido é regenerado e reinserido. Use-o para corrigir uma tomada, trocar uma ação ou fazer a ponte entre duas partes de um clipe.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Modelo a ser usado para geração de vídeo. | DYNAMIC_COMBO | Sim | "MiniMax H3 Max" |

### Entradas do MiniMax H3 Max

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `video` | Vídeo de origem, com até 60 segundos de duração. A proporção deve estar entre 0.4 e 2.5. | VIDEO | Sim | 0 a 60 segundos |
| `reference_images` | Slot expansível: conecte até 9 imagens de referência opcionais (`image_1`...`image_9`) para a nova cena, com pelo menos 256x256 pixels. Elas são referenciadas no prompt como `@Image1`..`@Image9` na ordem de conexão. | IMAGE | Não | 0 a 9 imagens |
| `reference_videos` | Slot expansível: conecte até 3 vídeos de referência opcionais (`video_1`...`video_3`) para a nova cena, com 2 a 15 segundos cada e 15 segundos no total. Eles são referenciados no prompt como `@Video1`..`@Video3` na ordem de conexão. | VIDEO | Não | 0 a 3 vídeos |
| `prompt` | A nova cena. É necessário um prompt ou pelo menos uma referência; referências sem prompt costumam ser ignoradas. | STRING | Sim | 0 a 50000 caracteres |
| `start_time` | Segundo em que o vídeo de origem é interrompido e a nova cena começa (padrão: 2.0). | FLOAT | Sim | 1.625 a 60.0 |
| `resume_time` | Segundo em que o vídeo de origem é retomado após a nova cena (padrão: 3.0). Deve ser posterior a `start_time` e pelo menos 1.375 segundos antes do fim do vídeo. O trecho de origem entre `start_time` e `resume_time` é removido. | FLOAT | Sim | 1.625 a 60.0 |
| `duration` | Duração da nova cena em segundos (padrão: 5). | INT | Sim | 5 a 13 |
| `resolution` | Resolução do vídeo de saída (padrão: "768P"). | COMBO | Sim | "480P"<br>"768P" |
| `color_match` | Igualar as cores da nova cena às do vídeo de origem (padrão: true). | BOOLEAN | Não | true<br>false |
| `prompt_expansion` | Reescreve o prompt usando o vídeo de origem. Desative para obter resultados reproduzíveis para a mesma seed (padrão: true). | BOOLEAN | Não | true<br>false |
| `seed` | Semente aleatória. A mesma solicitação com a mesma seed produz resultados semelhantes, mas não necessariamente idênticos (padrão: 42). | INT | Sim | 0 a 2147483647 |

### Restrições dos parâmetros

- `resume_time` deve ser maior que `start_time` e pelo menos 1.375 segundos antes do fim do vídeo; caso contrário, a solicitação será rejeitada.
- Cada vídeo de referência deve ter entre 2 e 15 segundos de duração, e todos juntos não podem ultrapassar 15 segundos.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `video` | O vídeo de origem com a nova cena inserida entre os tempos de início e de retomada. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxInsertVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `623ad0b37f51ce4640c0058676e008697e31563c2a77a3da79ba7936af2d3f99`
