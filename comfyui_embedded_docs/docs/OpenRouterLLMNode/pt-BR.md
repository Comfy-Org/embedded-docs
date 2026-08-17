# OpenRouter LLM

O nó OpenRouter LLM envia um prompt de texto (e, opcionalmente, imagens ou vídeos) para um conjunto selecionado de modelos de linguagem disponíveis por meio do serviço OpenRouter e retorna a resposta de texto gerada. Ele suporta modelos de Anthropic (Claude), OpenAI (GPT), Google (Gemini), xAI (Grok), DeepSeek, Qwen, Mistral, Z.AI (GLM), Moonshot (Kimi) e Perplexity Sonar, e exibe opções específicas do modelo, como esforço de raciocínio e contexto de pesquisa na web, quando o modelo selecionado as suporta.

## Entradas

O seletor `model` é dinâmico: escolher um modelo revela widgets específicos do modelo (esforço de raciocínio, contexto de pesquisa na web, slots de imagem e vídeo), além das entradas comuns abaixo.

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `model` | O modelo OpenRouter usado para gerar a resposta. Selecionar um modelo revela suas entradas específicas (consulte as seções de modelos abaixo). | DYNAMIC_COMBO | Sim | 34 opções selecionadas de modelos OpenRouter |
| `prompt` | Entrada de texto para o modelo. Deve conter pelo menos um caractere que não seja espaço em branco. | STRING | Sim | Texto de múltiplas linhas |
| `seed` | Semente para amostragem. Defina como 0 para omitir. A maioria dos modelos trata isso apenas como uma sugestão. (padrão: 0) | INT | Sim | 0 a 2147483647 |
| `system_prompt` | Instruções fundamentais que definem o comportamento do modelo. (padrão: "") | STRING | Não | Texto de múltiplas linhas |

**Nota sobre `seed`:** Este parâmetro tem um comportamento "control_after_generate", ou seja, ele pode ser configurado para mudar automaticamente (por exemplo, aleatorizar, incrementar ou manter fixo) após cada execução do nó, dependendo das configurações de widget do usuário.

**Nota sobre `system_prompt`:** Este parâmetro é opcional e está marcado como um parâmetro avançado na interface do usuário.

### Entradas do Anthropic Claude

Compartilhadas por `anthropic/claude-opus-5`, `anthropic/claude-opus-4.8`, `anthropic/claude-opus-4.7`, `anthropic/claude-fable-5`, `anthropic/claude-sonnet-5` e `anthropic/claude-haiku-4.5`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

### Entradas do OpenAI GPT

Compartilhadas por `openai/gpt-5.6-sol-pro`, `openai/gpt-5.6-sol`, `openai/gpt-5.6-terra-pro`, `openai/gpt-5.6-terra`, `openai/gpt-5.6-luna-pro`, `openai/gpt-5.6-luna`, `openai/gpt-5.5-pro` e `openai/gpt-5.5`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

### Entradas do Google Gemini 3.5 Flash

Aplica-se a `google/gemini-3.5-flash`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

### Entradas do xAI Grok

Compartilhadas por `x-ai/grok-4.5`, `x-ai/grok-4.20` e `x-ai/grok-4.3`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

### Entradas do DeepSeek

Compartilhadas por `deepseek/deepseek-v4-pro`, `deepseek/deepseek-v4-flash` e `deepseek/deepseek-v3.2`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

### Entradas do Qwen 3.6 Plus e Flash

Compartilhadas por `qwen/qwen3.6-plus` e `qwen/qwen3.6-flash`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

### Entradas do Mistral Large 2512

Aplica-se a `mistralai/mistral-large-2512`. Este modelo não adiciona widgets de parâmetro específicos; apenas as entradas comuns e o slot de referência `images` se aplicam.

### Entradas do Mistral Medium 3.5

Aplica-se a `mistralai/mistral-medium-3-5`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

### Entradas do Moonshot Kimi K3 e K2.6

Compartilhadas por `moonshotai/kimi-k3` e `moonshotai/kimi-k2.6`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

### Entradas do Perplexity Sonar Pro

Aplica-se a `perplexity/sonar-pro`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `search_context_size` | O quanto de contexto de pesquisa na web recuperar. Quanto maior, mais embasado, porém mais lento/caro. (padrão: "medium") | COMBO | Não | "low"<br>"medium"<br>"high" |

### Entradas do Perplexity Sonar Reasoning Pro e Deep Research

Compartilhadas por `perplexity/sonar-reasoning-pro` e `perplexity/sonar-deep-research`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `search_context_size` | O quanto de contexto de pesquisa na web recuperar. Quanto maior, mais embasado, porém mais lento/caro. (padrão: "medium") | COMBO | Não | "low"<br>"medium"<br>"high" |
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

### Modelos somente de raciocínio

Compartilhadas por `qwen/qwen3.6-max-preview`, `z-ai/glm-4.6`, `z-ai/glm-5` e `moonshotai/kimi-k2-thinking`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `images` | Imagem(ns) de referência opcional(is) — enviada(s) como URLs. Slot expansível: conecte `image_1` a `image_N`, em que N depende do modelo selecionado. | IMAGE | Não | 0 a N imagens (N = 8, 10 ou 20 dependendo do modelo) |
| `videos` | Vídeo(s) de referência opcional(is) — enviado(s) como URLs. Slot expansível: conecte `video_1` a `video_N`. Disponível apenas em modelos com suporte a vídeo. | VIDEO | Não | 0 a 4 vídeos |

**Nota sobre capacidades e limites dos modelos:**

- Suporte a imagens: até 20 imagens para os modelos Anthropic Claude, OpenAI GPT, Google Gemini 3.5 Flash e xAI Grok; até 10 imagens para Qwen 3.6 Plus/Flash e Moonshot Kimi K3/K2.6; até 8 imagens para Mistral Large 2512 e Mistral Medium 3.5. Os modelos DeepSeek, Qwen 3.6 Max Preview, Z.AI GLM, Moonshot Kimi K2 Thinking e Perplexity Sonar não aceitam imagens.
- Suporte a vídeos: apenas `google/gemini-3.5-flash`, `qwen/qwen3.6-plus` e `qwen/qwen3.6-flash` aceitam vídeos, com no máximo 4 vídeos.
- O nó gera um erro se mais imagens ou vídeos forem conectados do que o modelo selecionado suporta.
- Quando `reasoning_effort` é definido como "low", "medium" ou "high", o modelo raciocina internamente, mas não retorna o rastro de raciocínio; "off" desativa o raciocínio completamente.
- O widget `search_context_size` aparece apenas para os modelos Perplexity Sonar. Os widgets `reasoning_effort` e `search_context_size` são marcados como parâmetros avançados.
- O nó exibe um selo de preço aproximado (USD por 1K tokens) com base no modelo selecionado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `output` | A resposta de texto gerada pelo modelo OpenRouter selecionado. | STRING |

**Nota sobre erros:** o nó gera um erro se o OpenRouter retornar um erro de API, uma resposta vazia (sem choices) ou uma recusa do modelo.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `534ab9ecc12e35a23a4d8f3e10f4f82d95db8e902ac8a2f2ee0ea68246516f62`
