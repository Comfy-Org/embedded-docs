# OpenRouter LLM

O nó LLM do OpenRouter envia um prompt de texto para um conjunto selecionado de modelos de linguagem populares disponíveis por meio do serviço OpenRouter e retorna a resposta de texto gerada. Ele oferece suporte a modelos da Anthropic (Claude), OpenAI (GPT), Google (Gemini), xAI (Grok), DeepSeek, Qwen, Mistral, Z.AI (GLM), Moonshot (Kimi) e Perplexity Sonar, e pode incluir opcionalmente imagens ou vídeos como entradas de referência na solicitação.

## Entradas

Quando um modelo é selecionado no seletor `model`, o nó exibe widgets específicos do modelo acima das entradas comuns — esforço de raciocínio, tamanho da pesquisa na web e/ou slots de mídia de referência — dependendo das capacidades do modelo escolhido.

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Entrada de texto para o modelo. | STRING | Sim | N/A |
| `model` | O modelo OpenRouter usado para gerar a resposta. | DYNAMIC_COMBO | Sim | Múltiplas opções disponíveis (veja as seções de modelos abaixo) |
| `seed` | Semente para amostragem. Defina como 0 para omitir. A maioria dos modelos trata isso apenas como uma dica. (padrão: 0) | INT | Sim | 0 a 2147483647 |
| `system_prompt` | Instruções fundamentais que determinam o comportamento do modelo. (padrão: "") | STRING | Não | N/A |

### Entradas dos modelos Anthropic Claude

Compartilhadas por `anthropic/claude-opus-5`, `anthropic/claude-opus-4.8`, `anthropic/claude-opus-4.7`, `anthropic/claude-fable-5`, `anthropic/claude-sonnet-5` e `anthropic/claude-haiku-4.5`.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

Esses modelos suportam até 20 imagens de referência (veja Entradas de referência).

### Entradas dos modelos OpenAI GPT

Compartilhadas por `openai/gpt-5.6-sol-pro`, `openai/gpt-5.6-sol`, `openai/gpt-5.6-terra-pro`, `openai/gpt-5.6-terra`, `openai/gpt-5.6-luna-pro`, `openai/gpt-5.6-luna`, `openai/gpt-5.5-pro` e `openai/gpt-5.5`.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

Esses modelos suportam até 20 imagens de referência (veja Entradas de referência).

### Entradas do Google Gemini 3.5 Flash

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

Este modelo suporta até 20 imagens de referência e até 4 vídeos de referência (veja Entradas de referência).

### Entradas dos modelos xAI Grok

Compartilhadas por `x-ai/grok-4.5`, `x-ai/grok-4.20` e `x-ai/grok-4.3`.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

Esses modelos suportam até 20 imagens de referência (veja Entradas de referência).

### Entradas dos modelos DeepSeek

Compartilhadas por `deepseek/deepseek-v4-pro`, `deepseek/deepseek-v4-flash` e `deepseek/deepseek-v3.2`.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

Modelos somente de texto — sem imagens ou vídeos de referência.

### Entradas do Qwen 3.6 Max Preview

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

Modelo somente de texto — sem imagens ou vídeos de referência.

### Entradas do Qwen 3.6 Plus e Qwen 3.6 Flash

Compartilhadas por `qwen/qwen3.6-plus` e `qwen/qwen3.6-flash`.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

Esses modelos suportam até 10 imagens de referência e até 4 vídeos de referência (veja Entradas de referência).

### Entradas do Mistral Large 2512

Sem entradas específicas de perfil (perfil padrão). Este modelo suporta até 8 imagens de referência (veja Entradas de referência).

### Entradas do Mistral Medium 3.5

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

Este modelo suporta até 8 imagens de referência (veja Entradas de referência).

### Entradas dos modelos Z.AI GLM

Compartilhadas por `z-ai/glm-4.6` e `z-ai/glm-5`.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

Modelos somente de texto — sem imagens ou vídeos de referência.

### Entradas do Moonshot Kimi K3 e K2.6

Compartilhadas por `moonshotai/kimi-k3` e `moonshotai/kimi-k2.6`.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

Esses modelos suportam até 10 imagens de referência (veja Entradas de referência).

### Entradas do Moonshot Kimi K2 Thinking

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

Modelo somente de texto — sem imagens ou vídeos de referência.

### Entradas do Perplexity Sonar Pro

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | O quanto de contexto de pesquisa na web deve ser recuperado. Maior = mais fundamentado, porém mais lento/mais caro. (padrão: "medium") | COMBO | Não | "low"<br>"medium"<br>"high" |

Modelo somente de texto — sem imagens ou vídeos de referência.

### Entradas do Perplexity Sonar Reasoning Pro e Sonar Deep Research

Compartilhadas por `perplexity/sonar-reasoning-pro` e `perplexity/sonar-deep-research`.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `search_context_size` | O quanto de contexto de pesquisa na web deve ser recuperado. Maior = mais fundamentado, porém mais lento/mais caro. (padrão: "medium") | COMBO | Não | "low"<br>"medium"<br>"high" |
| `reasoning_effort` | Esforço de raciocínio. 'off' desativa o raciocínio completamente. (padrão: "off") | COMBO | Não | "off"<br>"low"<br>"medium"<br>"high" |

Modelos somente de texto — sem imagens ou vídeos de referência.

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `images` | Imagem(ns) de referência opcional(is), enviadas como URLs. Slot expansível: conecte de 1 a N entradas de imagem (`image_1`, `image_2`, ...); o limite de quantidade depende do modelo selecionado (veja as seções de modelos). | IMAGE | Não | 0 a 20 (depende do modelo: 8, 10 ou 20) |
| `videos` | Vídeo(s) de referência opcional(is), enviados como URLs. Slot expansível: conecte de 1 a N entradas de vídeo (`video_1`, `video_2`, ...); o limite de quantidade depende do modelo selecionado (veja as seções de modelos). | VIDEO | Não | 0 a 4 (depende do modelo) |

**Notas:**

- **Modelos disponíveis:** As opções de modelos disponíveis são construídas dinamicamente e incluem modelos com diferentes capacidades. A lista completa dos 34 modelos é:
  - Anthropic: `anthropic/claude-opus-5`, `anthropic/claude-opus-4.8`, `anthropic/claude-opus-4.7`, `anthropic/claude-fable-5`, `anthropic/claude-sonnet-5`, `anthropic/claude-haiku-4.5`
  - OpenAI: `openai/gpt-5.6-sol-pro`, `openai/gpt-5.6-sol`, `openai/gpt-5.6-terra-pro`, `openai/gpt-5.6-terra`, `openai/gpt-5.6-luna-pro`, `openai/gpt-5.6-luna`, `openai/gpt-5.5-pro`, `openai/gpt-5.5`
  - Google: `google/gemini-3.5-flash`
  - xAI: `x-ai/grok-4.5`, `x-ai/grok-4.20`, `x-ai/grok-4.3`
  - DeepSeek: `deepseek/deepseek-v4-pro`, `deepseek/deepseek-v4-flash`, `deepseek/deepseek-v3.2`
  - Qwen: `qwen/qwen3.6-max-preview`, `qwen/qwen3.6-plus`, `qwen/qwen3.6-flash`
  - Mistral: `mistralai/mistral-large-2512`, `mistralai/mistral-medium-3-5`
  - Z.AI: `z-ai/glm-4.6`, `z-ai/glm-5`
  - Moonshot: `moonshotai/kimi-k3`, `moonshotai/kimi-k2.6`, `moonshotai/kimi-k2-thinking`
  - Perplexity: `perplexity/sonar-pro`, `perplexity/sonar-reasoning-pro`, `perplexity/sonar-deep-research`

- **Restrições de imagem e vídeo:** O número máximo de imagens e vídeos de referência depende do modelo selecionado. O nó gera um erro se o número total de imagens ou vídeos fornecidos exceder o limite do modelo. Modelos sem suporte a imagem ou vídeo não exibem os respectivos slots de referência.

- **Comportamento do raciocínio:** Quando `reasoning_effort` é definido como qualquer valor diferente de "off", a solicitação pede ao provedor para raciocinar internamente sem retornar o rastro do raciocínio.

- **Comportamento da semente:** O parâmetro `seed` tem um comportamento "control_after_generate", o que significa que ele pode ser configurado para alterar automaticamente (por exemplo, aleatorizar, incrementar ou fixo) após cada execução do nó, dependendo das configurações do widget do usuário.

- **Prompt do sistema:** O parâmetro `system_prompt` é opcional e está marcado como um parâmetro avançado na interface do usuário.

- **Casos de erro:** O nó gera um erro se o prompt estiver vazio após a remoção de espaços em branco, se o OpenRouter retornar um erro, se o modelo selecionado se recusar a responder ou se a resposta não contiver escolhas ou mensagem. Um selo de preço no nó mostra uma estimativa de custo aproximada por 1K tokens com base no modelo selecionado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `output` | A resposta de texto gerada pelo modelo OpenRouter. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenRouterLLMNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `534ab9ecc12e35a23a4d8f3e10f4f82d95db8e902ac8a2f2ee0ea68246516f62`
