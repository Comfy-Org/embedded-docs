Este nó carrega múltiplas imagens de uma subpasta específica dentro do diretório de entrada do ComfyUI. Ele examina a pasta escolhida em busca de tipos de arquivo de imagem comuns e os retorna como uma lista, sendo útil para processamento em lote ou preparação de conjuntos de dados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `pasta` | A pasta de onde carregar as imagens. As opções são as subpastas presentes no diretório principal de entrada do ComfyUI. | STRING | Sim | *Múltiplas opções disponíveis* |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `images` | Lista de imagens carregadas. O nó carrega todos os arquivos de imagem válidos (PNG, JPG, JPEG, WEBP) encontrados na pasta selecionada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0f6e1b3d159f7d7c0c9530350ee057118a2618796f149586bae925253ecc8cf0`
