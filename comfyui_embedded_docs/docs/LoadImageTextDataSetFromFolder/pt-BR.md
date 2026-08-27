# Carregar Conjunto de Dados de Imagem e Texto da Pasta

Este nó carrega um conjunto de dados de pares imagem-legenda a partir de uma pasta selecionada e os retorna como uma lista. Ele suporta imagens PNG, JPG, JPEG e WEBP e, para cada imagem, procura uma legenda em um arquivo `.txt` com o mesmo nome base. O nó também suporta a estrutura de pastas do kohya-ss/sd-scripts, em que um nome de subpasta que começa com um número (como `10_cats`) repete as imagens dentro dessa subpasta esse número de vezes na saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `pasta` | A pasta de onde carregar as imagens e legendas de texto. | COMBO | Sim | Subpastas dentro do diretório de entrada do ComfyUI (carregadas dinamicamente) |

**Nota:** A pasta selecionada deve ser uma subpasta do diretório de entrada do ComfyUI. O nó espera um arquivo de legenda `.txt` para cada imagem: para cada arquivo de imagem (`.png`, `.jpg`, `.jpeg`, `.webp`), ele procura um arquivo `.txt` com o mesmo nome base no mesmo local e usa seu conteúdo com espaços iniciais e finais removidos como legenda. Se nenhum arquivo de legenda for encontrado, usa-se uma string vazia. O nó também suporta a estrutura de pastas do kohya-ss/sd-scripts: subpastas cujo nome começa com um número e um sublinhado (por exemplo, `5_cats`) repetem as imagens dentro delas esse número de vezes na lista final de saída. Se a pasta selecionada não contiver imagens válidas, o nó gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `imagens` | Lista de imagens carregadas. As imagens são convertidas para RGB e normalizadas para a faixa de ponto flutuante de 0 a 1. | IMAGE |
| `textos` | Lista de legendas de texto, uma para cada imagem carregada. As legendas são o conteúdo com espaços iniciais e finais removidos do arquivo `.txt` correspondente, ou uma string vazia quando nenhum arquivo de legenda existe. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d34494d59a65edb38d7e6a5f12c241fb0093371db0b0bf1e52789e84209ad3f5`
