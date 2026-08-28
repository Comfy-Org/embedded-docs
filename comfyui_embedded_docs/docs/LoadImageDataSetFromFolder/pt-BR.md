# Carregar Conjunto de Imagens da Pasta

Este nó carrega várias imagens de uma subpasta selecionada no diretório de entrada principal do ComfyUI e as retorna como uma lista. Ele verifica a pasta escolhida em busca de arquivos de imagem nos formatos PNG, JPG, JPEG ou WEBP, o que o torna útil para processamento em lote ou preparação de conjuntos de dados de imagens.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `pasta` | A pasta de onde carregar as imagens. As opções são as subpastas presentes no diretório de entrada principal do ComfyUI. | COMBO | Sim | Múltiplas opções disponíveis |

Observação: A pasta selecionada deve ser uma subpasta do diretório de entrada principal do ComfyUI; qualquer valor que resolva para fora dele é rejeitado. Somente arquivos com as extensões .png, .jpg, .jpeg ou .webp são carregados, e a verificação de extensão não diferencia maiúsculas de minúsculas. Se a pasta selecionada não contiver arquivos de imagem válidos, o nó gera um erro. Este nó é marcado como experimental.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `imagens` | Lista de imagens carregadas. O nó carrega todos os arquivos de imagem válidos (PNG, JPG, JPEG, WEBP) encontrados na pasta selecionada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cdee4e372890c126dd5f09654a7dd4103bba97a7901b6f5df8e02f29c4064ed2`
