> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/pt-BR.md)

O nó MaskPreview gera uma visualização de uma máscara convertendo-a em um formato de imagem de 3 canais e salvando-a como um arquivo temporário. Ele recebe uma máscara como entrada e a remodela em um formato adequado para exibição de imagem, depois salva o resultado no diretório temporário com um prefixo de nome de arquivo aleatório. Isso permite que os usuários inspecionem visualmente os dados da máscara durante a execução do fluxo de trabalho.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `mask` | MASK | Sim | - | Os dados da máscara a serem visualizados e convertidos para o formato de imagem |
| `filename_prefix` | STRING | Não | - | Prefixo para o nome do arquivo de saída (padrão: "ComfyUI") |
| `prompt` | PROMPT | Não | - | Informações do prompt para metadados (fornecido automaticamente) |
| `extra_pnginfo` | EXTRA_PNGINFO | Não | - | Informações PNG adicionais para metadados (fornecido automaticamente) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `ui` | DICT | Contém as informações da imagem de visualização e os metadados para exibição |
