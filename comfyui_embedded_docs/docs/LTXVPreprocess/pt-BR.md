> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVPreprocess/pt-BR.md)

O nó LTXVPreprocess aplica um pré-processamento de compressão a imagens. Ele recebe imagens de entrada e as processa com um nível de compressão especificado, gerando como saída as imagens processadas com as configurações de compressão aplicadas.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser processada |
| `img_compression` | INT | Não | 0-100 | Quantidade de compressão a ser aplicada na imagem (padrão: 35) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output_image` | IMAGE | A imagem de saída processada com a compressão aplicada |
