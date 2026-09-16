# OpenAI GPT Image 2.5

Este nó gera imagens usando a API GPT Image da OpenAI. Ele oferece suporte a cinco modelos — `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, `gpt-image-2`, `gpt-image-1.5` e `gpt-image-1` — permite anexar imagens de referência para edição de imagem e pode usar uma máscara para especificar quais partes de uma imagem devem ser substituídas.

## Entradas

### Entradas comuns

Essas entradas estão sempre visíveis.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo OpenAI GPT Image a ser usado. Selecionar um modelo revela parâmetros adicionais específicos desse modelo. | DYNAMIC_COMBO | Sim | `"gpt-image-2.5-flare"`<br>`"gpt-image-2.5-sunburst"`<br>`"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `prompt` | Prompt de texto para o GPT Image (padrão: `""`). | STRING | Sim | N/A |
| `n` | Quantas imagens gerar (padrão: `1`). | INT | Sim | 1 a 8 |
| `semente` | Seed para reprodutibilidade (padrão: `0`). Ainda não implementado no backend. | INT | Sim | 0 a 2147483647 |

### Entradas do gpt-image-2.5-flare e do gpt-image-2.5-sunburst

Essas entradas aparecem quando `model` está definido como `gpt-image-2.5-flare` ou `gpt-image-2.5-sunburst`. Ambos os modelos compartilham o mesmo conjunto de parâmetros.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `tamanho` | Tamanho da imagem. Selecione "Custom" para usar a largura e a altura personalizadas (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `largura_personalizada` | Usado somente quando `model.size` é "Custom". Deve ser múltiplo de 16 (padrão: `1024`). | INT | Não | 480 a 3840 (passo 16) |
| `altura_personalizada` | Usado somente quando `model.size` é "Custom". Deve ser múltiplo de 16 (padrão: `1024`). | INT | Não | 480 a 3840 (passo 16) |
| `fundo` | Retorna a imagem com ou sem fundo (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `qualidade` | Qualidade da imagem; afeta o custo e o tempo de geração (padrão: `"low"`). | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.images` | Imagem(ns) de referência opcional(is) para edição de imagem. Até 16 imagens. Consulte Entradas de referência para obter detalhes. | IMAGE | Não | 0 a 16 |
| `model.mask` | Máscara opcional para inpainting (áreas brancas serão substituídas). Requer exatamente uma imagem de referência. | MASK | Não | N/A |

### Entradas do gpt-image-2

Essas entradas aparecem quando `model` está definido como `gpt-image-2`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `tamanho` | Tamanho da imagem. Selecione "Custom" para usar a largura e a altura personalizadas (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `largura_personalizada` | Usado somente quando `model.size` é "Custom". Deve ser múltiplo de 16 (padrão: `1024`). | INT | Não | 480 a 3840 (passo 16) |
| `altura_personalizada` | Usado somente quando `model.size` é "Custom". Deve ser múltiplo de 16 (padrão: `1024`). | INT | Não | 480 a 3840 (passo 16) |
| `fundo` | Retorna a imagem com ou sem fundo (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `qualidade` | Qualidade da imagem; afeta o custo e o tempo de geração (padrão: `"low"`). | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Imagem(ns) de referência opcional(is) para edição de imagem. Até 16 imagens. Consulte Entradas de referência para obter detalhes. | IMAGE | Não | 0 a 16 |
| `model.mask` | Máscara opcional para inpainting (áreas brancas serão substituídas). Requer exatamente uma imagem de referência. | MASK | Não | N/A |

### Entradas do gpt-image-1.5 e do gpt-image-1

Essas entradas aparecem quando `model` está definido como `gpt-image-1.5` ou `gpt-image-1`. Ambos os modelos compartilham o mesmo conjunto de parâmetros.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `tamanho` | Tamanho da imagem (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `fundo` | Retorna a imagem com ou sem fundo (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `qualidade` | Qualidade da imagem; afeta o custo e o tempo de geração (padrão: `"low"`). | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Imagem(ns) de referência opcional(is) para edição de imagem. Até 16 imagens. Consulte Entradas de referência para obter detalhes. | IMAGE | Não | 0 a 16 |
| `model.mask` | Máscara opcional para inpainting (áreas brancas serão substituídas). Requer exatamente uma imagem de referência. | MASK | Não | N/A |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model.images` | Slot expansível: conecte 1..N itens (ex.: `image_1`...`image_16`); até 16 imagens de referência para todos os modelos. | IMAGE | Não | 0 a 16 |
| `model.mask` | Máscara opcional para inpainting (áreas brancas serão substituídas). Requer exatamente uma imagem de referência. | MASK | Não | N/A |

**Restrições e limitações dos parâmetros:**

- Quando `model.size` é "Custom" (somente `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst` e `gpt-image-2`), `model.custom_width` e `model.custom_height` devem ser ambos múltiplos de 16, a aresta mais longa não deve exceder 3840, a proporção de aspecto não deve exceder 3:1, e o número total de pixels deve estar entre 655.360 e 8.294.400.
- `model.mask` requer exatamente uma imagem de referência em `model.images`: não pode ser usado sem uma imagem, nem com mais de uma imagem.
- Quando `model.mask` é usado, sua altura e largura devem corresponder à altura e à largura da imagem de referência.
- Quando `model.images` é fornecido, o nó é executado no modo de edição de imagem; sem `model.images`, ele gera imagens apenas a partir do prompt.
- As imagens de referência e a máscara são reduzidas antes de serem enviadas à API.
- Os níveis de qualidade `"xhigh"` e `"max"` estão disponíveis apenas para `gpt-image-2.5-flare` e `gpt-image-2.5-sunburst`.
- `seed` atualmente não está implementado no backend.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `image` | A imagem ou imagens geradas. Todas as imagens retornadas são empilhadas em um único lote; se suas dimensões forem diferentes, elas são redimensionadas para corresponder à primeira imagem. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `804ea35d0e2aa0b2993a293cb10cb41e2f9c6a3732304306253f7f7b1eb59b8a`
