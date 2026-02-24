> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/pt-BR.md)

Este nó carrega múltiplas imagens de uma subpasta específica dentro do diretório de entrada do ComfyUI. Ele verifica a pasta escolhida em busca de tipos de arquivo de imagem comuns e os retorna como uma lista, sendo útil para processamento em lote ou preparação de conjuntos de dados.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `folder` | STRING | Sim | *Múltiplas opções disponíveis* | A pasta da qual carregar as imagens. As opções são as subpastas presentes no diretório de entrada principal do ComfyUI. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `images` | IMAGE | Lista de imagens carregadas. O nó carrega todos os arquivos de imagem válidos (PNG, JPG, JPEG, WEBP) encontrados na pasta selecionada. |
