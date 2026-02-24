> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/pt-BR.md)

O nó Create Video gera um arquivo de vídeo a partir de uma sequência de imagens. Você pode especificar a velocidade de reprodução usando quadros por segundo e, opcionalmente, adicionar áudio ao vídeo. O nó combina suas imagens em um formato de vídeo que pode ser reproduzido com a taxa de quadros especificada.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sim | - | As imagens a partir das quais criar um vídeo. |
| `fps` | FLOAT | Sim | 1.0 - 120.0 | Os quadros por segundo para a velocidade de reprodução do vídeo (padrão: 30.0). |
| `audio` | AUDIO | Não | - | O áudio a ser adicionado ao vídeo. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado contendo as imagens de entrada e o áudio opcional. |
