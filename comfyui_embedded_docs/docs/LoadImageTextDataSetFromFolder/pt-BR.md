# Carregar Conjunto de Dados de Imagem e Texto da Pasta

Este nó carrega um conjunto de pares de imagens e legendas de texto de uma pasta especificada e os retorna como uma lista. Formatos suportados: PNG, JPG, JPEG, WEBP. Para cada arquivo de imagem, o nó procura automaticamente um arquivo `.txt` correspondente com o mesmo nome base para usar como legenda. O nó também suporta uma estrutura de pastas onde os nomes das subpastas começam com um prefixo numérico (como `10_folder_name`), o que faz com que as imagens dentro dessa subpasta sejam repetidas esse número de vezes na saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `folder` | A pasta de onde carregar as imagens e legendas de texto. As opções disponíveis são as subpastas dentro do diretório de entrada do ComfyUI. | COMBO | Sim | *Carregado dinamicamente de `folder_paths.get_input_subfolders()`* |

**Nota:** O nó espera uma estrutura de arquivos específica. Para cada arquivo de imagem (`.png`, `.jpg`, `.jpeg`, `.webp`), ele procurará um arquivo `.txt` com o mesmo nome para usar como legenda. Se um arquivo de legenda não for encontrado, uma string vazia é usada. O nó também suporta uma estrutura especial em que o nome de uma subpasta começa com um número e um sublinhado (ex.: `5_cats`), o que fará com que todas as imagens dentro dessa subpasta sejam repetidas esse número de vezes na lista final de saída. A pasta selecionada deve estar dentro do diretório de entrada do ComfyUI; nomes de pastas que resolvam para fora dele são rejeitados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `images` | Uma lista de tensores de imagem carregados. | IMAGE |
| `texts` | Uma lista de legendas de texto correspondentes a cada imagem carregada. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d34494d59a65edb38d7e6a5f12c241fb0093371db0b0bf1e52789e84209ad3f5`
