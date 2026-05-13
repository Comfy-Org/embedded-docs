> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/pt-BR.md)

Este nó gera respostas de texto a partir de um modelo OpenAI. Ele envia seu prompt de texto (e, opcionalmente, imagens ou arquivos) para um modelo OpenAI e retorna a resposta de texto gerada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | - | Entradas de texto para o modelo, usadas para gerar uma resposta (padrão: vazio) |
| `persist_context` | BOOLEAN | Sim | - | Este parâmetro está obsoleto e não tem efeito (padrão: False) |
| `model` | COMBO | Sim | Vários modelos OpenAI disponíveis | O modelo usado para gerar a resposta |
| `images` | IMAGE | Não | - | Imagem(ns) opcional(is) para usar como contexto para o modelo. Para incluir várias imagens, você pode usar o nó Batch Images |
| `files` | OPENAI_INPUT_FILES | Não | - | Arquivo(s) opcional(is) para usar como contexto para o modelo. Aceita entradas do nó OpenAI Chat Input Files |
| `advanced_options` | OPENAI_CHAT_CONFIG | Não | - | Configuração opcional para o modelo. Aceita entradas do nó OpenAI Chat Advanced Options |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output_text` | STRING | A resposta de texto gerada pelo modelo OpenAI |

---
**Source fingerprint (SHA-256):** `ea66b58b23305b0d97bfc76cc39cfdfe8e01b70edcbfd60c2c640a07ad507ee6`
