# OpenAI ChatGPT

Este nó gera respostas de texto a partir de um modelo OpenAI. Ele envia seu prompt de texto (e, opcionalmente, imagens ou arquivos) para um modelo OpenAI e retorna a resposta de texto gerada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Entradas de texto para o modelo, usadas para gerar uma resposta (padrão: vazio) | STRING | Sim | - |
| `persist_context` | Este parâmetro está obsoleto e não tem efeito (padrão: False) | BOOLEAN | Sim | - |
| `model` | O modelo usado para gerar a resposta (padrão: `gpt-5`) | COMBO | Sim | `gpt-5.6-sol`<br>`gpt-5.6-terra`<br>`gpt-5.6-luna`<br>`gpt-5.5-pro`<br>`gpt-5.5`<br>`gpt-5`<br>`gpt-5-mini`<br>`gpt-5-nano`<br>`gpt-4.1`<br>`gpt-4.1-mini`<br>`gpt-4.1-nano`<br>`o4-mini`<br>`o3`<br>`o1-pro`<br>`o1` |
| `images` | Imagem(ns) opcional(is) para usar como contexto para o modelo. Para incluir várias imagens, você pode usar o nó Batch Images | IMAGE | Não | - |
| `files` | Arquivo(s) opcional(is) para usar como contexto para o modelo. Aceita entradas do nó OpenAI Chat Input Files | OPENAI_INPUT_FILES | Não | - |
| `advanced_options` | Configuração opcional para o modelo. Aceita entradas do nó OpenAI Chat Advanced Options | OPENAI_CHAT_CONFIG | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output_text` | A resposta de texto gerada pelo modelo OpenAI | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `25bb3648a4e1ea5668486375153ac4c96b542082c88958d4f62b93adf1db5b2a`
