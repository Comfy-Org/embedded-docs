> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoNode/pt-BR.md)

Este nó gera vídeos usando o modelo Kling V3. Ele suporta dois modos principais: texto-para-vídeo, onde um vídeo é criado a partir de uma descrição textual, e imagem-para-vídeo, onde uma imagem existente é animada. Ele também oferece recursos avançados, como criar vídeos com múltiplos segmentos com prompts diferentes para cada parte (storyboards) e, opcionalmente, gerar áudio de acompanhamento.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `multi_shot` | COMBO | Sim | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` | Controla se deve gerar um único vídeo ou uma série de segmentos com prompts e durações individuais. Quando não for "disabled", entradas adicionais para o prompt e duração de cada storyboard aparecem. |
| `generate_audio` | BOOLEAN | Sim | `True` / `False` | Quando habilitado, o nó irá gerar áudio para o vídeo. O padrão é `True`. |
| `model` | COMBO | Sim | `"kling-v3"` | O modelo e suas configurações associadas. Selecionar esta opção revela os subparâmetros `resolution` e `aspect_ratio`. |
| `model.resolution` | COMBO | Sim | `"1080p"`<br>`"720p"` | A resolução para o vídeo gerado. Esta configuração está disponível quando o `model` está definido como "kling-v3". |
| `model.aspect_ratio` | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` | A proporção de aspecto para o vídeo gerado. Esta configuração é ignorada quando uma imagem é fornecida para `start_frame` (modo imagem-para-vídeo). Disponível quando o `model` está definido como "kling-v3". |
| `seed` | INT | Sim | 0 a 2147483647 | Um valor de semente para a geração. Alterar este valor fará com que o nó seja executado novamente, mas os resultados não são determinísticos. O padrão é `0`. |
| `start_frame` | IMAGE | Não | - | Uma imagem inicial opcional. Quando conectada, o nó alterna do modo texto-para-vídeo para o modo imagem-para-vídeo, animando a imagem fornecida. |

**Entradas para o modo `multi_shot`:**

* Quando `multi_shot` está definido como **"disabled"**, as seguintes entradas aparecem:
  * `prompt` (STRING): A descrição textual principal para o vídeo. Obrigatória. Deve ter entre 1 e 2500 caracteres.
  * `negative_prompt` (STRING): Texto descrevendo o que não deve aparecer no vídeo. Opcional.
  * `duration` (INT): A duração do vídeo em segundos. Deve ser entre 3 e 15. O padrão é `5`.
* Quando `multi_shot` está definido como uma opção de storyboard (ex.: `"3 storyboards"`), entradas para cada segmento do storyboard aparecem (ex.: `storyboard_1_prompt`, `storyboard_1_duration`). Cada prompt deve ter entre 1 e 512 caracteres. A **soma total de todas as durações dos storyboards** deve ser entre 3 e 15 segundos.

**Restrições:**

* O nó opera no modo **texto-para-vídeo** quando `start_frame` não está conectado. Ele usa a configuração `model.aspect_ratio` neste modo.
* O nó opera no modo **imagem-para-vídeo** quando `start_frame` está conectado. A configuração `model.aspect_ratio` é ignorada. A imagem de entrada deve ter pelo menos 300x300 pixels e ter uma proporção de aspecto entre 1:2.5 e 2.5:1.
* No modo storyboard (`multi_shot` não é "disabled"), as entradas principais `prompt` e `negative_prompt` ficam ocultas e não são usadas.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `video` | VIDEO | O arquivo de vídeo gerado. |
