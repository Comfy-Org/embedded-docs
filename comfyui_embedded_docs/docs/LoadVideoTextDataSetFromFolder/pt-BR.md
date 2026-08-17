# Carregar Vídeo-Texto (da Pasta)

Este nó carrega um conjunto de dados de pares vídeo-texto de uma subpasta selecionada no diretório de entrada do ComfyUI e os retorna como duas listas: vídeos e legendas de texto. Os itens de vídeo são referências lazy; portanto, os quadros só são decodificados quando um nó downstream precisa deles. Os formatos compatíveis são MP4, AVI, MOV, WEBM, MKV e FLV. As legendas são lidas de arquivos `.txt` que têm o mesmo nome de cada arquivo de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `folder` | A pasta que contém os arquivos de vídeo e as legendas .txt. | COMBO | Sim | Todas as subpastas dentro do diretório de entrada do ComfyUI (lista dinâmica) |

Observações:
- A pasta selecionada deve ser uma subpasta do diretório de entrada do ComfyUI; caminhos que resolvam fora dele são rejeitados.
- Se a pasta não contiver arquivos com uma extensão de vídeo compatível, o nó gera um erro.
- Subpastas aninhadas cujo nome começa com um número seguido de sublinhado (por exemplo, `5_classname/`, como usado por ferramentas como kohya-ss/sd-scripts) também são compatíveis: cada vídeo dentro dessa pasta é incluído no conjunto de dados o número de vezes indicado por esse prefixo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `videos` | Referências lazy de vídeo; os quadros são decodificados somente quando necessário downstream. Uma entrada para cada arquivo de vídeo encontrado na pasta. | VIDEO (lista) |
| `texts` | Lista de legendas de texto. Uma legenda por vídeo; se um vídeo não tiver um arquivo `.txt` correspondente, sua legenda será uma string vazia. | STRING (lista) |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `21ed21bc3189e96be5c7f0415c65e8749d6591cf19bddf4350a3b0af48b92841`
