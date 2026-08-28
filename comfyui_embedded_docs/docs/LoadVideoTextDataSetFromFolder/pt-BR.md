# Carregar Vídeo-Texto (da Pasta)

Este nó carrega arquivos de vídeo e suas legendas de texto associadas de uma subpasta selecionada no diretório de entrada do ComfyUI e os retorna como duas listas: vídeos e legendas. As entradas de vídeo são referências preguiçosas, portanto, os frames são decodificados somente quando um nó posterior precisar deles. Os formatos suportados são MP4, AVI, MOV, WEBM, MKV e FLV. Pastas aninhadas com prefixo de contagem de repetição (por exemplo, `5_classname/`, como usado por ferramentas como kohya-ss/sd-scripts) também são suportadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `pasta` | A pasta que contém arquivos de vídeo e legendas .txt. | COMBO | Sim | Múltiplas opções disponíveis: lista dinamicamente todas as subpastas dentro do diretório de entrada do ComfyUI |

A pasta selecionada deve ser uma subpasta do diretório de entrada do ComfyUI; um nome de pasta que resolva para fora desse diretório gera um erro. Se a pasta selecionada não contiver arquivos com extensão de vídeo suportada (MP4, AVI, MOV, WEBM, MKV, FLV), o nó gera um erro. Para pastas aninhadas cujo nome começa com um número seguido de sublinhado (por exemplo, `5_classname`), cada vídeo dentro dessa pasta é incluído no conjunto de dados o número de vezes indicado por esse prefixo. A legenda de cada vídeo é lida de um arquivo `.txt` com o mesmo nome base; se não existir um arquivo `.txt` correspondente, a legenda é uma string vazia.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `vídeos` | Referências preguiçosas de vídeo; os frames são decodificados somente quando necessário a jusante. Uma entrada por arquivo de vídeo encontrado na pasta. | VIDEO (lista) |
| `textos` | Lista de legendas de texto. Uma legenda por vídeo; se um vídeo não tiver um arquivo `.txt` correspondente, sua legenda é uma string vazia. | STRING (lista) |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `21ed21bc3189e96be5c7f0415c65e8749d6591cf19bddf4350a3b0af48b92841`
