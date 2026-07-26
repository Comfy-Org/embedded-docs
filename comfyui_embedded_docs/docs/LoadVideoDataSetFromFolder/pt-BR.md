# Carregar Vídeo (da Pasta)

Carregar um conjunto de dados de vídeos de uma pasta especificada dentro do diretório de entrada do ComfyUI. O nó varre a pasta em busca de arquivos de vídeo compatíveis e retorna referências lazy — os quadros reais são decodificados apenas quando necessário adiante no fluxo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `pasta` | A pasta que contém os arquivos de vídeo. Selecione entre as subpastas disponíveis dentro do diretório de entrada do ComfyUI. | STRING | Sim | *(preenchido a partir das subpastas de entrada)* |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `videos` | Uma lista de referências lazy de vídeo (uma por arquivo). Os quadros do vídeo são decodificados apenas quando a saída é consumida por outro nó. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `74017c46993c38a72e529cef59ea1282f7b88b6a33b9028cf200cb3eb37de395`
