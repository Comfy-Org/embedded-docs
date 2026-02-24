> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/pt-BR.md)

Este nó gera respostas de texto a partir de um modelo da OpenAI. Ele permite que você tenha conversas com o modelo de IA enviando prompts de texto e recebendo respostas geradas. O nó suporta conversas com múltiplas interações, onde ele pode lembrar do contexto anterior, e também pode processar imagens e arquivos como contexto adicional para o modelo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Entradas de texto para o modelo, usadas para gerar uma resposta (padrão: vazio) |
| `persist_context` | BOOLEAN | Sim | - | Persistir o contexto do chat entre as chamadas para conversas com múltiplas interações (padrão: Verdadeiro) |
| `model` | COMBO | Sim | Múltiplos modelos OpenAI disponíveis | O modelo OpenAI a ser usado para gerar as respostas |
| `images` | IMAGE | Não | - | Imagem(ns) opcional(is) para usar como contexto para o modelo. Para incluir múltiplas imagens, você pode usar o nó Batch Images (padrão: Nenhum) |
| `files` | OPENAI_INPUT_FILES | Não | - | Arquivo(s) opcional(is) para usar como contexto para o modelo. Aceita entradas do nó OpenAI Chat Input Files (padrão: Nenhum) |
| `advanced_options` | OPENAI_CHAT_CONFIG | Não | - | Configuração opcional para o modelo. Aceita entradas do nó OpenAI Chat Advanced Options (padrão: Nenhum) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output_text` | STRING | A resposta de texto gerada pelo modelo OpenAI |
