> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeControlnet/pt-BR.md)

O nó CLIPTextEncodeControlnet processa uma entrada de texto usando um modelo CLIP e a combina com dados de condicionamento existentes para criar uma saída de condicionamento aprimorada para aplicações de controlnet. Ele tokeniza o texto de entrada, o codifica através do modelo CLIP e adiciona os *embeddings* resultantes aos dados de condicionamento fornecidos como parâmetros de controlnet de atenção cruzada.

## Entradas

| Parâmetro | Tipo de Dado | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | Obrigatório | - | - | O modelo CLIP usado para tokenização e codificação do texto |
| `conditioning` | CONDITIONING | Obrigatório | - | - | Dados de condicionamento existentes a serem aprimorados com os parâmetros de controlnet |
| `text` | STRING | Multilinha, Prompts Dinâmicos | - | - | Texto de entrada a ser processado pelo modelo CLIP |

**Observação:** Este nó requer ambas as entradas `clip` e `conditioning` para funcionar corretamente. A entrada `text` suporta prompts dinâmicos e texto multilinha para um processamento de texto flexível.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Dados de condicionamento aprimorados com parâmetros de atenção cruzada de controlnet adicionados |
