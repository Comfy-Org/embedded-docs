# OpenAI GPT Image 2

Este nó gera imagens usando a API GPT Image da OpenAI. Ele suporta vários modelos GPT Image, imagens de referência opcionais para edição e uma máscara opcional para inpaint. Quando imagens de referência são fornecidas, o nó envia uma solicitação de edição para a API; caso contrário, envia uma solicitação de geração simples.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo GPT Image da OpenAI a ser usado. Selecionar um modelo revela parâmetros adicionais específicos desse modelo. | DYNAMIC_COMBO | Sim | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `prompt` | Prompt de texto para o GPT Image (padrão: ""). | STRING | Sim | N/A |
| `n` | Quantas imagens gerar (padrão: 1). | INT | Sim | 1 a 8 |
| `seed` | Semente para reprodutibilidade (padrão: 0). Ainda não implementada no backend. | INT | Sim | 0 a 2147483647 |

### Entradas do gpt-image-2

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model.size` | Tamanho da imagem. Selecione "Custom" para usar largura e altura personalizadas (padrão: "auto"). | COMBO | Sim | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | Usado somente quando `size` é "Custom". Deve ser um múltiplo de 16 (padrão: 1024). | INT | Não | 1024 a 3840 |
| `model.custom_height` | Usado somente quando `size` é "Custom". Deve ser um múltiplo de 16 (padrão: 1024). | INT | Não | 1024 a 3840 |
| `model.background` | Retorna a imagem com ou sem fundo (padrão: "auto"). | COMBO | Sim | `"auto"`<br>`"opaque"` |
| `model.quality` | Qualidade da imagem, afeta o custo e o tempo de geração (padrão: "low"). | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"` |

### Entradas do gpt-image-1.5 e gpt-image-1

Esses dois modelos compartilham o mesmo conjunto de parâmetros específicos do modelo.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model.size` | Tamanho da imagem (padrão: "auto"). | COMBO | Sim | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `model.background` | Retorna a imagem com ou sem fundo (padrão: "auto"). | COMBO | Sim | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Qualidade da imagem, afeta o custo e o tempo de geração (padrão: "low"). | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"` |

### Entradas de referência

Estas entradas estão disponíveis para todos os modelos.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model.images` | Imagem(ns) de referência opcional(is) para edição de imagem. Slot expansível: conecte até 16 imagens (`image_1` a `image_16`). | IMAGE | Não | 0 a 16 imagens |
| `model.mask` | Máscara opcional para inpaint (áreas brancas serão substituídas). Requer exatamente uma imagem de referência. | MASK | Não | N/A |

**Restrições e limitações dos parâmetros:**

- Quando `model.size` for "Custom" (somente gpt-image-2), `model.custom_width` e `model.custom_height` devem ser múltiplos de 16, a maior aresta não deve exceder 3840 pixels, a proporção (aspect ratio) não deve exceder 3:1 e o número total de pixels deve estar entre 655.360 e 8.294.400.
- Uma máscara requer exatamente uma imagem de referência. Uma máscara não pode ser usada sem uma imagem de entrada e não pode ser usada com várias imagens de entrada.
- Quando uma máscara é fornecida, a altura e a largura da máscara devem corresponder à altura e largura da imagem de entrada.
- As imagens de referência são reduzidas para um máximo de 2048 x 2048 pixels totais antes de serem enviadas à API.
- O parâmetro `seed` ainda não foi implementado no backend.
- Se a API retornar imagens com dimensões diferentes em uma única resposta, todas as imagens são redimensionadas para corresponder às dimensões da primeira imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `image` | A(s) imagem(ns) gerada(s), empilhadas em um único tensor de lote de formato (N, H, W, C). | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fb3491f949151fbd3f5825ec9f9ae124019767d083f56966ef34af278aef50c0`
