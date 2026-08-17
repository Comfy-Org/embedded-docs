# Carregar Conjunto de Imagens da Pasta

Este nó carrega um conjunto de imagens de uma pasta selecionada e as retorna como uma lista. A pasta deve ser uma subpasta dentro do diretório de entrada principal do ComfyUI. Os formatos de imagem suportados são PNG, JPG, JPEG e WEBP.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `folder` | A pasta de onde carregar as imagens. As opções disponíveis são as subpastas presentes no diretório de entrada principal do ComfyUI. Valores que resolvem fora deste diretório (por exemplo, usando "..") são rejeitados. | COMBO | Sim | *Múltiplas opções disponíveis* — as subpastas presentes no diretório de entrada do ComfyUI |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `images` | Lista de imagens carregadas. O nó carrega todo arquivo de imagem válido (PNG, JPG, JPEG, WEBP) encontrado na pasta selecionada e os retorna como uma lista. Se a pasta não contém arquivos de imagem suportados, um erro é gerado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cdee4e372890c126dd5f09654a7dd4103bba97a7901b6f5df8e02f29c4064ed2`
