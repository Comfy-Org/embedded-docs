# Carregar Vídeo (da Pasta)

Carrega todos os arquivos de vídeo suportados de uma pasta selecionada dentro do diretório de entrada do ComfyUI e os retorna como uma lista de referências de vídeo. Este nó retorna referências de vídeo lentas (*lazy*), portanto os quadros são decodificados apenas quando outro nó realmente precisa deles. Formatos suportados: MP4, AVI, MOV, WEBM, MKV e FLV.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|---------------|-------------|-------|
| `folder` | A pasta que contém os arquivos de vídeo. Selecione entre as subpastas disponíveis dentro do diretório de entrada do ComfyUI. | COMBO | Sim | Todas as subpastas disponíveis no diretório de entrada do ComfyUI |

**Observação:** A pasta selecionada deve conter pelo menos um arquivo de vídeo suportado. As extensões suportadas são MP4, AVI, MOV, WEBM, MKV e FLV. Se nenhum arquivo de vídeo suportado for encontrado, o nó gera um erro. A pasta deve corresponder a um local dentro do diretório de entrada do ComfyUI; nomes de pasta que tentem sair dele (por exemplo, com "..") são rejeitados com erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `videos` | Uma lista de referências de vídeo lentas (*lazy*), uma para cada arquivo de vídeo na pasta selecionada. Os quadros são decodificados apenas quando a saída é consumida por outro nó. | VIDEO (lista) |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6a7e6115872bb994fa554bb9de84bcd419106485403a3d2db654cbdd6c72bbe5`
