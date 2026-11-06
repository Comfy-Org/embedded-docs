# OpenAI GPT Image 2.6

Este nó gera imagens usando a API GPT Image da OpenAI. Ele oferece suporte a seis modelos — `gpt-image-2.6-flare`, `gpt-image-2.6-sunburst`, `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, `gpt-image-2` e `gpt-image-1.5` — permite anexar imagens de referência para edição de imagem e pode usar uma máscara para especificar quais partes de uma imagem devem ser substituídas.

## Entradas

### Entradas comuns

Estas entradas estão sempre visíveis.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo GPT Image da OpenAI a usar. Selecionar um modelo revela parâmetros adicionais específicos desse modelo. | DYNAMIC_COMBO | Sim | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"`<br>`"gpt-image-2.5-flare"`<br>`"gpt-image-2.5-sunburst"`<br>`"gpt-image-2"`<br>`"gpt-image-1.5"` |
| `prompt` | Prompt de texto para o GPT Image (padrão: `""`). | STRING | Sim | N/A |
| `n` | Quantas imagens gerar (padrão: `1`). | INT | Sim | 1 a 8 |
| `semente` | Semente para reprodutibilidade (padrão: `0`). Ainda não implementado no backend. | INT | Sim | 0 a 2147483647 |

### Entradas do gpt-image-2.6-flare e do gpt-image-2.6-sunburst

Estas entradas aparecem quando `model` está definido como `gpt-image-2.6-flare` ou `gpt-image-2.6-sunburst`. Ambos os modelos compartilham o mesmo conjunto de parâmetros.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `tamanho` | Tamanho da imagem. Selecione "Custom" para usar a largura e a altura personalizadas (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `largura_personalizada` | Usado somente quando `model.size` é "Custom". Deve ser um múltiplo de 16 (padrão: `1024`). | INT | Não | 480 a 3840 (passo 16) |
| `altura_personalizada` | Usado somente quando `model.size` é "Custom". Deve ser um múltiplo de 16 (padrão: `1024`). | INT | Não | 480 a 3840 (passo 16) |
| `fundo` | Retorna a imagem com ou sem fundo (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `qualidade` | Qualidade da imagem; afeta o custo e o tempo de geração (padrão: `"low"`). | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.images` | Imagens de referência opcionais para edição de imagem. Até 16 imagens. Consulte Entradas de referência para obter detalhes. | IMAGE | Não | 0 a 16 |
| `model.mask` | Máscara opcional para inpainting (as áreas brancas serão substituídas). Requer exatamente uma imagem de referência. | MASK | Não | N/A |
| `model.complexity` | Quanto o modelo planeja a imagem antes da renderização. Valores menores retornam mais rápido; valores maiores planejam mais. Padrão: `"high"`. | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"` |

### Entradas do gpt-image-2

Estas entradas aparecem quando `model` está definido como `gpt-image-2`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `tamanho` | Tamanho da imagem. Selecione "Custom" para usar a largura e a altura personalizadas (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `largura_personalizada` | Usado somente quando `model.size` é "Custom". Deve ser um múltiplo de 16 (padrão: `1024`). | INT | Não | 480 a 3840 (passo 16) |
| `altura_personalizada` | Usado somente quando `model.size` é "Custom". Deve ser um múltiplo de 16 (padrão: `1024`). | INT | Não | 480 a 3840 (passo 16) |
| `fundo` | Retorna a imagem com ou sem fundo (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"opaque"` |
| `qualidade` | Qualidade da imagem; afeta o custo e o tempo de geração (padrão: `"low"`). | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Imagens de referência opcionais para edição de imagem. Até 16 imagens. Consulte Entradas de referência para obter detalhes. | IMAGE | Não | 0 a 16 |
| `model.mask` | Máscara opcional para inpainting (as áreas brancas serão substituídas). Requer exatamente uma imagem de referência. | MASK | Não | N/A |

### Entradas do gpt-image-1.5

Estas entradas aparecem quando `model` está definido como `gpt-image-1.5`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `tamanho` | Tamanho da imagem (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `fundo` | Retorna a imagem com ou sem fundo (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `qualidade` | Qualidade da imagem; afeta o custo e o tempo de geração (padrão: `"low"`). | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Imagens de referência opcionais para edição de imagem. Até 16 imagens. Consulte Entradas de referência para obter detalhes. | IMAGE | Não | 0 a 16 |
| `model.mask` | Máscara opcional para inpainting (as áreas brancas serão substituídas). Requer exatamente uma imagem de referência. | MASK | Não | N/A |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model.images` | Slot expansível: conecte 1..N itens (ex.: `image_1`...`image_16`); até 16 imagens de referência para todos os modelos. | IMAGE | Não | 0 a 16 |
| `model.mask` | Máscara opcional para inpainting (as áreas brancas serão substituídas). Requer exatamente uma imagem de referência. | MASK | Não | N/A |

**Restrições e limitações dos parâmetros:**

- Quando `model.size` é "Custom" (somente `gpt-image-2.6-flare`, `gpt-image-2.6-sunburst`, `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst` e `gpt-image-2`), `model.custom_width` e `model.custom_height` devem ser ambos múltiplos de 16, a aresta mais longa não deve exceder 3840, a proporção não deve exceder 3:1 e a contagem total de pixels deve estar entre 655,360 e 8,294,400.
- `model.mask` requer exatamente uma imagem de referência em `model.images`: não pode ser usado sem uma imagem e não pode ser usado com mais de uma imagem.
- Quando `model.mask` é usado, sua altura e largura devem corresponder à altura e à largura da imagem de referência.
- Quando `model.images` é fornecido, o nó é executado no modo de edição de imagem; sem `model.images`, ele gera imagens apenas a partir do prompt.
- As imagens de referência e a máscara são reduzidas antes de serem enviadas à API.
- Os níveis de qualidade `"xhigh"` e `"max"` estão disponíveis apenas para `gpt-image-2.6-flare`, `gpt-image-2.6-sunburst`, `gpt-image-2.5-flare` e `gpt-image-2.5-sunburst`.
- `model.complexity` está disponível apenas para `gpt-image-2.6-flare` e `gpt-image-2.6-sunburst`; os outros modelos usam uma profundidade de planejamento fixa.
- `seed` atualmente não está implementado no backend.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `image` | A imagem ou as imagens geradas. Todas as imagens retornadas são agrupadas em um único lote; se as dimensões forem diferentes, elas são redimensionadas para corresponder à primeira imagem. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `effc65978ac1cca52a8d8c85230784c23c9eb2afffd7f057aba9f9627e784a15`
