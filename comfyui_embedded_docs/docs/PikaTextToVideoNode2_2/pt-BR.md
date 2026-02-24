> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaTextToVideoNode2_2/pt-BR.md)

O nó Pika Text2Video v2.2 envia um prompt de texto para a API Pika versão 2.2 para gerar um vídeo. Ele converte sua descrição textual em um vídeo usando o serviço de geração de vídeo por IA da Pika. O nó permite personalizar vários aspectos do processo de geração de vídeo, incluindo proporção, duração e resolução.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt_text` | STRING | Sim | - | A descrição textual principal que descreve o que você deseja gerar no vídeo |
| `negative_prompt` | STRING | Sim | - | Texto descrevendo o que você não quer que apareça no vídeo gerado |
| `seed` | INT | Sim | - | Um número que controla a aleatoriedade da geração para resultados reproduzíveis |
| `resolution` | STRING | Sim | - | A configuração de resolução para o vídeo de saída |
| `duration` | INT | Sim | - | A duração do vídeo em segundos |
| `aspect_ratio` | FLOAT | Não | 0.4 - 2.5 | Proporção (largura / altura) (padrão: 1.7777777777777777) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado retornado pela API Pika |
