# OpenAI GPT Image 2.6

## Visão geral

OpenAI GPT Image 2.6 gera imagens a partir de um prompt e as edita quando você conecta imagens de referência, usando os modelos GPT Image da OpenAI. O nó oferece quatro modelos: `gpt-image-2.6-flare`, `gpt-image-2.6-sunburst`, `gpt-image-2.5-flare` e `gpt-image-2.5-sunburst`. Desenhe anotações na primeira imagem de referência e conecte-as como um par de marcação para mostrar ao modelo exatamente onde editar.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo GPT Image a usar. Selecionar um modelo revela os parâmetros desse modelo. | DYNAMIC_COMBO | Sim | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"`<br>`"gpt-image-2.5-flare"`<br>`"gpt-image-2.5-sunburst"` |

### Entradas do gpt-image-2.6-flare e do gpt-image-2.6-sunburst

Essas entradas aparecem quando `model` está definido como `gpt-image-2.6-flare` ou `gpt-image-2.6-sunburst`. Os dois modelos compartilham os mesmos parâmetros.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model.prompt` | O que gerar, ou a edição a fazer. (padrão: `""`) | STRING | Sim | N/A |
| `model.size` | Tamanho da imagem. Selecione "Custom" para usar a largura e a altura personalizadas. (padrão: `"auto"`) | COMBO | Sim | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | Usado apenas quando `model.size` é "Custom". Deve ser um múltiplo de 16. (padrão: `1024`) | INT | Não | 480 a 3840 (passo 16) |
| `model.custom_height` | Usado apenas quando `model.size` é "Custom". Deve ser um múltiplo de 16. (padrão: `1024`) | INT | Não | 480 a 3840 (passo 16) |
| `model.background` | Retorna a imagem com ou sem fundo. (padrão: `"auto"`) | COMBO | Sim | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Qualidade da imagem. Níveis mais altos custam mais e demoram mais. (padrão: `"low"`) | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.complexity` | Quanto o modelo planeja a imagem antes de renderizar. (padrão: `"high"`) | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Imagens de referência opcionais para edição. Até 16. | AUTOGROW | Não | 0 a 16 |
| `model.markup` | Anotações desenhadas sobre a primeira imagem de referência, mostrando onde editar. Devem corresponder ao tamanho dessa imagem e devem ser conectadas junto com `model.markup_alpha`. | IMAGE | Não | N/A |
| `model.markup_alpha` | O branco marca as anotações em `model.markup`. A saída MASK do nó Painter se encaixa diretamente; uma máscara do nó Load Image precisa do Invert Mask primeiro. | MASK | Não | N/A |
| `model.seed` | Controla se o nó é executado novamente; os resultados não são determinísticos, independentemente da seed. (padrão: `42`) | INT | Sim | 0 a 2147483647 |

### Entradas do gpt-image-2.5-flare e do gpt-image-2.5-sunburst

Essas entradas aparecem quando `model` está definido como `gpt-image-2.5-flare` ou `gpt-image-2.5-sunburst`. Elas correspondem aos modelos 2.6, exceto que `model.complexity` não é oferecido.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model.prompt` | O que gerar, ou a edição a fazer. (padrão: `""`) | STRING | Sim | N/A |
| `model.size` | Tamanho da imagem. Selecione "Custom" para usar a largura e a altura personalizadas. (padrão: `"auto"`) | COMBO | Sim | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | Usado apenas quando `model.size` é "Custom". Deve ser um múltiplo de 16. (padrão: `1024`) | INT | Não | 480 a 3840 (passo 16) |
| `model.custom_height` | Usado apenas quando `model.size` é "Custom". Deve ser um múltiplo de 16. (padrão: `1024`) | INT | Não | 480 a 3840 (passo 16) |
| `model.background` | Retorna a imagem com ou sem fundo. (padrão: `"auto"`) | COMBO | Sim | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Qualidade da imagem. Níveis mais altos custam mais e demoram mais. (padrão: `"low"`) | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.images` | Imagens de referência opcionais para edição. Até 16. | AUTOGROW | Não | 0 a 16 |
| `model.markup` | Anotações desenhadas sobre a primeira imagem de referência, mostrando onde editar. Devem corresponder ao tamanho dessa imagem e devem ser conectadas junto com `model.markup_alpha`. | IMAGE | Não | N/A |
| `model.markup_alpha` | O branco marca as anotações em `model.markup`. A saída MASK do nó Painter se encaixa diretamente; uma máscara do nó Load Image precisa do Invert Mask primeiro. | MASK | Não | N/A |
| `model.seed` | Controla se o nó é executado novamente; os resultados não são determinísticos, independentemente da seed. (padrão: `42`) | INT | Sim | 0 a 2147483647 |

**Restrições e limitações dos parâmetros:**

- Com `model.size` definido como "Custom", `model.custom_width` e `model.custom_height` devem ser ambos múltiplos de 16, a aresta mais longa não deve exceder 3840, a proporção de aspecto não deve exceder 3:1 e a contagem total de pixels deve estar entre 655.360 e 8.294.400.
- `model.markup` e `model.markup_alpha` devem ser conectados juntos. A marcação precisa de pelo menos uma imagem de referência, e sua largura e altura devem corresponder à primeira imagem de referência.
- Sem `model.images`, o nó gera imagens apenas a partir do prompt; com imagens de referência, ele as edita e combina.
- As imagens de referência são reduzidas antes de serem enviadas à API.
- `model.complexity` existe apenas em `gpt-image-2.6-flare` e `gpt-image-2.6-sunburst`; os modelos 2.5 usam uma profundidade de planejamento fixa.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `image` | A imagem ou as imagens geradas. Todas as imagens retornadas são empilhadas em um único lote; se as dimensões delas forem diferentes, elas são redimensionadas para corresponder à primeira imagem. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV3/pt-BR.md)

---
**Source fingerprint (SHA-256):** `33f5d91af56c215cc7f7c704f9b123fe1c35bf287012072b818b76b551c04667`
