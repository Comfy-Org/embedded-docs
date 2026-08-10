# Carregar Vídeo-Texto (da Pasta)

Este nó carrega arquivos de vídeo e suas legendas de texto associadas de uma subpasta selecionada dentro do diretório de entrada do ComfyUI e os retorna como duas listas: vídeos e legendas. As entradas de vídeo são referências lazy, portanto os quadros só são decodificados quando um nó downstream precisa deles. Os formatos suportados são MP4, AVI, MOV, WEBM, MKV e FLV. Pastas aninhadas com prefixo de contagem de repetições (por exemplo, `5_classname/`, como usado por ferramentas como kohya-ss/sd-scripts) também são suportadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `pasta` | A pasta que contém arquivos de vídeo e legendas .txt. | STRING | Sim | Combo: lista dinâmica de todas as subpastas dentro do diretório de entrada do ComfyUI |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
Se a pasta selecionada não contiver arquivos com uma extensão de vídeo suportada, o nó gera um erro. Para pastas aninhadas cujo nome começa com um número seguido de sublinhado (por exemplo, `5_classname`), cada vídeo dentro dessa pasta é incluído no conjunto de dados o número de vezes indicado por esse prefixo.
|---------------|-----------|--------------|
| `videos` | Referências de vídeo lazy; os quadros são decodificados apenas quando necessário downstream. Uma entrada para cada arquivo de vídeo encontrado na pasta. | VIDEO (list) |
| `texts` | Lista de legendas em texto. Uma legenda por vídeo; se um vídeo não tiver um arquivo `.txt` correspondente, sua legenda será uma string vazia. | STRING (list) |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `91236fcb1e42b8de1a1100b0aecaad49bd49c159d7d8f502032cd7f5b2b54845`
