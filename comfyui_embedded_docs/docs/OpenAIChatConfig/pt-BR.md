> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/pt-BR.md)

O nó OpenAIChatConfig permite definir opções de configuração adicionais para o Nó de Chat da OpenAI. Ele fornece configurações avançadas que controlam como o modelo gera respostas, incluindo comportamento de truncamento, limites de comprimento da saída e instruções personalizadas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `truncation` | COMBO | Sim | `"auto"`<br>`"disabled"` | A estratégia de truncamento a ser usada para a resposta do modelo. auto: Se o contexto desta resposta e das anteriores exceder o tamanho da janela de contexto do modelo, o modelo truncará a resposta para caber na janela de contexto, descartando itens de entrada no meio da conversa. disabled: Se uma resposta do modelo exceder o tamanho da janela de contexto para um modelo, a solicitação falhará com um erro 400 (padrão: "auto") |
| `max_output_tokens` | INT | Não | 16-16384 | Um limite superior para o número de tokens que podem ser gerados para uma resposta, incluindo tokens de saída visíveis (padrão: 4096) |
| `instructions` | STRING | Não | - | Instruções adicionais para a resposta do modelo (suporte a entrada de múltiplas linhas) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `OPENAI_CHAT_CONFIG` | OPENAI_CHAT_CONFIG | Objeto de configuração contendo as configurações especificadas para uso com os Nós de Chat da OpenAI |
