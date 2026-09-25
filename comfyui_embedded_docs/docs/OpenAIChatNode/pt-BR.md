# OpenAI ChatGPT

Este nó gera respostas de texto a partir de um modelo da OpenAI. Ele envia seu prompt de texto e, opcionalmente, imagens ou arquivos para um modelo da OpenAI e retorna a resposta de texto gerada.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `prompt` | Entradas de texto para o modelo, usadas para gerar uma resposta (padrão: string vazia). | STRING | Sim | - |
| `persist_context` | Este parâmetro está obsoleto e não tem efeito (padrão: False). | BOOLEAN | Sim | - |
| `model` | O modelo usado para gerar a resposta (padrão: `gpt-5`) | COMBO | Sim | `gpt-6-astra`<br>`gpt-6-sol`<br>`gpt-6-luna`<br>`gpt-5.6-sol`<br>`gpt-5.6-terra`<br>`gpt-5.6-luna`<br>`gpt-5.5-pro`<br>`gpt-5.5`<br>`gpt-5`<br>`gpt-5-mini`<br>`gpt-5-nano`<br>`gpt-4.1`<br>`gpt-4.1-mini`<br>`gpt-4.1-nano`<br>`o4-mini`<br>`o3`<br>`o1-pro`<br>`o1` |
| `images` | Imagem(ns) opcional(is) para usar como contexto para o modelo. Para incluir várias imagens, você pode usar o nó Batch Images. | IMAGE | Não | - |
| `files` | Arquivo(s) opcional(is) para usar como contexto para o modelo. Aceita entradas do nó OpenAI Chat Input Files. | OPENAI_INPUT_FILES | Não | - |
| `advanced_options` | Configuração opcional para o modelo. Aceita entradas do nó OpenAI Chat Advanced Options. | OPENAI_CHAT_CONFIG | Não | - |

Observação: quando uma configuração `advanced_options` que define um esforço de raciocínio está conectada, o `model` selecionado deve oferecer suporte a esse valor de esforço. Por exemplo, a família de modelos gpt-4.1 não oferece suporte a nenhum esforço de raciocínio, `gpt-6-sol` e `gpt-6-luna` oferecem suporte a none, low, medium, high, xhigh e max, `gpt-5.5` oferece suporte a none, low, medium, high e xhigh, e `gpt-5.5-pro` oferece suporte a medium, high e xhigh. Se o esforço de raciocínio não for suportado pelo modelo selecionado, o nó gera um erro.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|---------------|-----------|---------------|
| `output_text` | A resposta de texto gerada pelo modelo da OpenAI. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `46b4558f1368191e2b4eb68f79e098f289c9eb80e1e05f7a516123c098295f2b`
