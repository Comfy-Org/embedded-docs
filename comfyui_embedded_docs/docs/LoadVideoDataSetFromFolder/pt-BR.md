# Carregar Vídeo (da Pasta)

Carrega um conjunto de dados de vídeos de uma pasta selecionada dentro do diretório de entrada do ComfyUI e os retorna como uma lista de referências de vídeo lazy. Este nó carrega um conjunto de dados de vídeos: os quadros são decodificados somente quando outro nó realmente precisa deles. Os formatos suportados são MP4, AVI, MOV, WEBM, MKV e FLV.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `pasta` | A pasta contendo arquivos de vídeo. | COMBO | Sim | Todas as subpastas disponíveis no diretório de entrada do ComfyUI (populadas dinamicamente) |

**Nota:** A pasta selecionada deve ser uma subpasta do diretório de entrada do ComfyUI e deve conter pelo menos um arquivo de vídeo suportado. As extensões suportadas são MP4, AVI, MOV, WEBM, MKV e FLV. Se nenhum arquivo de vídeo suportado for encontrado, ou se o caminho da pasta for resolvido fora do diretório de entrada, o nó gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `vídeos` | Uma lista de referências de vídeo lazy, uma para cada arquivo de vídeo suportado na pasta selecionada, ordenada alfabeticamente por nome de arquivo. Os quadros de vídeo são decodificados somente quando a saída é consumida por outro nó. | VIDEO (lista) |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6a7e6115872bb994fa554bb9de84bcd419106485403a3d2db654cbdd6c72bbe5`
