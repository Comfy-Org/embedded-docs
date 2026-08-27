# OpenAI GPT Image 2

Este nó gera imagens usando a API GPT Image da OpenAI. Ele suporta vários modelos (`gpt-image-2`, `gpt-image-1.5` e `gpt-image-1`), permite fornecer imagens de referência para edição e pode usar uma máscara para especificar quais partes de uma imagem modificar.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo GPT Image da OpenAI a ser usado. Selecionar um modelo revela parâmetros adicionais específicos desse modelo. | DYNAMIC_COMBO | Sim | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `prompt` | Prompt de texto para GPT Image (padrão: `""`). | STRING | Sim | N/A |
| `n` | Quantas imagens gerar (padrão: `1`). | INT | Sim | 1 a 8 |
| `semente` | Semente para reprodutibilidade (padrão: `0`). Ainda não implementado no backend. | INT | Sim | 0 a 2147483647 |

### Entradas do gpt-image-2

Estas entradas aparecem quando `model` está definido como `gpt-image-2`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `tamanho` | Tamanho da imagem. Selecione "Custom" para usar a largura e a altura personalizadas (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `largura_personalizada` | Utilizado somente quando `model.size` for "Custom". Deve ser um múltiplo de 16 (padrão: `1024`). | INT | Não | 1024 a 3840 |
| `altura_personalizada` | Utilizado somente quando `model.size` for "Custom". Deve ser um múltiplo de 16 (padrão: `1024`). | INT | Não | 1024 a 3840 |
| `fundo` | Retorna a imagem com ou sem fundo (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"opaque"` |
| `qualidade` | Qualidade da imagem; afeta o custo e o tempo de geração (padrão: `"low"`). | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Imagens de referência opcionais para edição de imagem. Até 16 imagens. Consulte as Entradas de referência para obter detalhes. | IMAGE | Não | 0 a 16 |
| `model.mask` | Máscara opcional para inpainting (as áreas brancas serão substituídas). Requer exatamente uma imagem de referência. | MASK | Não | N/A |

### Entradas do gpt-image-1.5 e gpt-image-1

Estas entradas aparecem quando `model` está definido como `gpt-image-1.5` ou `gpt-image-1`. Ambos os modelos compartilham o mesmo conjunto de parâmetros.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `tamanho` | Tamanho da imagem (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `fundo` | Retorna a imagem com ou sem fundo (padrão: `"auto"`). | COMBO | Sim | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `qualidade` | Qualidade da imagem; afeta o custo e o tempo de geração (padrão: `"low"`). | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Imagens de referência opcionais para edição de imagem. Até 16 imagens. Consulte as Entradas de referência para obter detalhes. | IMAGE | Não | 0 a 16 |
| `model.mask` | Máscara opcional para inpainting (as áreas brancas serão substituídas). Requer exatamente uma imagem de referência. | MASK | Não | N/A |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model.images` | Slot expansível: conecte de 1 a N itens (ex.: `image_1`...`image_16`); até 16 imagens de referência para todos os modelos. | IMAGE | Não | 1 a 16 |
| `model.mask` | Máscara opcional para inpainting (as áreas brancas serão substituídas). Requer exatamente uma imagem de referência. | MASK | Não | N/A |

**Restrições e limitações dos parâmetros:**

- Quando `model.size` for "Custom" (somente no gpt-image-2), `model.custom_width` e `model.custom_height` devem ser ambos múltiplos de 16, o maior lado não deve exceder 3840, a razão de aspecto não deve exceder 3:1 e o número total de pixels deve estar entre 655.360 e 8.294.400.
- O parâmetro `model.mask` requer exatamente uma imagem de referência em `model.images`: não pode ser usado sem uma imagem nem com mais de uma imagem.
- Ao usar `model.mask`, suas dimensões devem corresponder às dimensões da imagem de referência.
- Quando o parâmetro `model.images` é fornecido, o nó opera no modo de edição de imagem; sem `model.images`, ele gera imagens apenas a partir do prompt.
- As imagens de referência são reduzidas em escala antes de serem enviadas à API.
- O parâmetro `seed` atualmente não está implementado no backend.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `image` | A imagem ou as imagens geradas. Todas as imagens retornadas são empilhadas em um único lote; se as dimensões forem diferentes, elas são redimensionadas para corresponder à primeira imagem. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fb3491f949151fbd3f5825ec9f9ae124019767d083f56966ef34af278aef50c0`
