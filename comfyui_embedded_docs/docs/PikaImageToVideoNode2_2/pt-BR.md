> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaImageToVideoNode2_2/pt-BR.md)

O nó Pika Image to Video envia uma imagem e um prompt de texto para a API Pika versão 2.2 para gerar um vídeo. Ele converte sua imagem de entrada em formato de vídeo com base na descrição e configurações fornecidas. O nó gerencia a comunicação com a API e retorna o vídeo gerado como saída.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem a ser convertida em vídeo |
| `prompt_text` | STRING | Sim | - | A descrição textual que orienta a geração do vídeo |
| `negative_prompt` | STRING | Sim | - | Texto descrevendo o que evitar no vídeo |
| `seed` | INT | Sim | - | Valor de semente aleatória para resultados reproduzíveis |
| `resolution` | STRING | Sim | - | Configuração da resolução do vídeo de saída |
| `duration` | INT | Sim | - | Duração do vídeo gerado em segundos |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado |
