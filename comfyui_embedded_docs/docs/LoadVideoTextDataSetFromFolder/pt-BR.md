# Carregar Vídeo-Texto (da Pasta)

This node loads video files and their matching text captions from a folder inside the ComfyUI input directory, and returns them as two lists: videos and captions. The video entries are lazy references, so frames are decoded only when a downstream node needs them. Supported formats are MP4, AVI, MOV, WEBM, MKV, and FLV, and nested folders with a repeat-count prefix (for example `5_classname/`, as used by tools like kohya-ss/sd-scripts) are also supported.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `pasta` | A pasta que contém arquivos de vídeo e legendas .txt. | COMBO | Sim | Lista dinamicamente todas as subpastas dentro do diretório de entrada do ComfyUI |

A pasta selecionada deve ser uma subpasta do diretório de entrada do ComfyUI; um nome de pasta que resolve para fora desse diretório gera um erro. Se a pasta selecionada não contiver nenhum arquivo com uma extensão de vídeo suportada (MP4, AVI, MOV, WEBM, MKV, FLV), o nó gera um erro. Para pastas aninhadas cujo nome começa com um número seguido de um sublinhado (por exemplo, `5_classname`), cada vídeo dentro dessa pasta é incluído no conjunto de dados o número de vezes indicado por esse prefixo. A legenda de cada vídeo é lida de um arquivo `.txt` com o mesmo nome base; se não existir um arquivo `.txt` correspondente, a legenda será uma string vazia.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `videos` | Referências de vídeo sob demanda; os frames são decodificados apenas quando necessário a jusante. Uma entrada por arquivo de vídeo encontrado na pasta. | VIDEO (list) |
| `texts` | Lista de legendas de texto. Uma legenda por vídeo; se um vídeo não tiver um arquivo `.txt` correspondente, sua legenda será uma string vazia. | STRING (list) |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `21ed21bc3189e96be5c7f0415c65e8749d6591cf19bddf4350a3b0af48b92841`
