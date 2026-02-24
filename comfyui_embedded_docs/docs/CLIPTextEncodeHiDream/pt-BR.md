> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHiDream/pt-BR.md)

O nó CLIPTextEncodeHiDream processa múltiplas entradas de texto usando diferentes modelos de linguagem e as combina em uma única saída de condicionamento. Ele tokeniza o texto de quatro fontes diferentes (CLIP-L, CLIP-G, T5-XXL e LLaMA) e os codifica usando uma abordagem de codificação programada. Isso permite um condicionamento de texto mais sofisticado, aproveitando vários modelos de linguagem simultaneamente.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | Entrada Obrigatória | - | - | O modelo CLIP usado para tokenização e codificação |
| `clip_l` | STRING | Texto Multilinha | - | - | Entrada de texto para processamento pelo modelo CLIP-L |
| `clip_g` | STRING | Texto Multilinha | - | - | Entrada de texto para processamento pelo modelo CLIP-G |
| `t5xxl` | STRING | Texto Multilinha | - | - | Entrada de texto para processamento pelo modelo T5-XXL |
| `llama` | STRING | Texto Multilinha | - | - | Entrada de texto para processamento pelo modelo LLaMA |

**Observação:** Todas as entradas de texto suportam prompts dinâmicos e entrada de texto multilinha. O nó requer que todos os quatro parâmetros de texto sejam fornecidos para funcionar corretamente, pois cada um contribui para a saída de condicionamento final através do processo de codificação programada.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | A saída de condicionamento combinada de todas as entradas de texto processadas |
