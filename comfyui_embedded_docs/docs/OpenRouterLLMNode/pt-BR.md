> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/en.md)

## Visão Geral

O nó OpenRouter LLM envia um prompt de texto para um conjunto selecionado de modelos de linguagem populares disponíveis através do serviço OpenRouter e retorna a resposta de texto gerada. Ele suporta modelos de provedores como xAI, DeepSeek, Qwen, Mistral, Z.AI (GLM), Moonshot (Kimi) e Perplexity Sonar, e pode opcionalmente incluir imagens ou vídeos na requisição.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | N/A | Entrada de texto para o modelo. |
| `model` | STRING | Sim | Múltiplas opções disponíveis (veja nota abaixo) | O modelo OpenRouter usado para gerar a resposta. |
| `seed` | INT | Sim | 0 a 2147483647 | Semente para amostragem. Defina como 0 para omitir. A maioria dos modelos trata isso apenas como uma sugestão. (padrão: 0) |
| `system_prompt` | STRING | Não | N/A | Instruções fundamentais que determinam o comportamento do modelo. (padrão: "") |

**Nota sobre o parâmetro `model`:** As opções de modelo disponíveis são construídas dinamicamente e podem incluir modelos com diferentes capacidades. Alguns modelos suportam recursos adicionais como esforço de raciocínio, pesquisa na web ou entrada de imagem/vídeo. O nó validará se o número de imagens ou vídeos fornecidos não excede o número máximo suportado pelo modelo.

**Nota sobre o parâmetro `seed`:** O parâmetro `seed` tem um comportamento de "controle após geração", o que significa que pode ser configurado para mudar automaticamente (por exemplo, aleatorizar, incrementar ou fixo) após cada execução do nó, dependendo das configurações do widget do usuário.

**Nota sobre `system_prompt`:** Este parâmetro é opcional e é marcado como um parâmetro avançado na interface do usuário.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | STRING | A resposta de texto gerada pelo modelo OpenRouter. |

---
**Source fingerprint (SHA-256):** `24757e36bf2356cc1805a6f071db88ca455e17944695672f19845a4cd1826c8a`
