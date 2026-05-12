> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseReferenceVideoApi/pt-BR.md)

## Visão Geral

Este nó gera um vídeo com uma pessoa ou objeto baseado em imagens de referência usando o modelo HappyHorse. Ele suporta a criação de vídeos com um único personagem ou múltiplos personagens interagindo entre si.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | COMBO | Sim | `"happyhorse-1.0-r2v"` | O modelo HappyHorse a ser usado para geração de vídeo. |
| `prompt` | STRING | Sim | N/A | Uma descrição textual do vídeo que você deseja gerar. Use identificadores como 'character1' e 'character2' para se referir aos personagens de referência. |
| `resolution` | COMBO | Sim | `"720P"`<br>`"1080P"` | A resolução do vídeo gerado. |
| `ratio` | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | A proporção de aspecto do vídeo gerado. |
| `duration` | INT | Sim | 3 a 15 | A duração do vídeo gerado em segundos (padrão: 5). |
| `reference_images` | IMAGE | Sim | 1 a 9 | Uma ou mais imagens de referência da pessoa ou objeto a ser exibido no vídeo. Você deve fornecer pelo menos uma imagem. |
| `seed` | INT | Não | 0 a 2147483647 | Um valor de semente para geração reproduzível (padrão: 0). A semente pode ser configurada para alterar automaticamente após cada geração. |
| `watermark` | BOOLEAN | Não | Verdadeiro ou Falso | Se deve adicionar uma marca d'água gerada por IA ao vídeo resultante (padrão: Falso). |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `VIDEO` | VIDEO | O arquivo de vídeo gerado. |