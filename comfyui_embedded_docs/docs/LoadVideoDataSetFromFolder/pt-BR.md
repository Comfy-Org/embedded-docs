# Carregar Vídeo (da Pasta)

Carrega todos os arquivos de vídeo suportados de uma pasta selecionada dentro do diretório de entrada do ComfyUI e os retorna como uma lista de referências de vídeo. Este nó retorna referências lazy de vídeo, portanto os quadros são decodificados apenas quando outro nó realmente precisa deles.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `pasta` | A pasta que contém os arquivos de vídeo. Selecione entre as subpastas disponíveis dentro do diretório de entrada do ComfyUI. | STRING | Sim | Todas as subpastas disponíveis no diretório de entrada do ComfyUI |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
**Observação:** A pasta selecionada deve conter pelo menos um arquivo de vídeo suportado. As extensões suportadas são MP4, AVI, MOV, WEBM, MKV e FLV. Se nenhum arquivo de vídeo suportado for encontrado, o nó gera um erro.
|---------------|-----------|---------------|
| `videos` | Uma lista de referências lazy de vídeo, uma para cada arquivo de vídeo na pasta selecionada. Os quadros do vídeo são decodificados apenas quando a saída é consumida por outro nó. | VIDEO (list) |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `74017c46993c38a72e529cef59ea1282f7b88b6a33b9028cf200cb3eb37de395`
