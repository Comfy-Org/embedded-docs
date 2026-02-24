> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/pt-BR.md)

O nó **Salvar Conjunto de Dados de Imagem e Texto em Pasta** salva uma lista de imagens e suas legendas de texto correspondentes em uma pasta especificada dentro do diretório de saída do ComfyUI. Para cada imagem salva como um arquivo PNG, um arquivo de texto correspondente com o mesmo nome base é criado para armazenar sua legenda. Isso é útil para criar conjuntos de dados organizados de imagens geradas e suas descrições.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sim | - | Lista de imagens a serem salvas. |
| `texts` | STRING | Sim | - | Lista de legendas de texto a serem salvas. |
| `folder_name` | STRING | Não | - | Nome da pasta para salvar as imagens (dentro do diretório de saída). (padrão: "dataset") |
| `filename_prefix` | STRING | Não | - | Prefixo para os nomes dos arquivos de imagem salvos. (padrão: "image") |

**Observação:** As entradas `images` e `texts` são listas. O nó espera que o número de legendas de texto corresponda ao número de imagens fornecidas. Cada legenda será salva em um arquivo `.txt` correspondente à sua imagem emparelhada.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| - | - | Este nó não possui saídas. Ele salva os arquivos diretamente no sistema de arquivos. |
