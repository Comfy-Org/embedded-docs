# Recraft V4 Texto para Imagem

Este nó gera imagens a partir de descrições textuais usando os modelos de IA Recraft V4 e V4.1. Ele envia seu prompt para uma API externa e retorna as imagens geradas. Você pode controlar a saída especificando o modelo, o tamanho da imagem e o número de imagens a serem criadas.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `modelo` | O modelo a ser usado para a geração. | DYNAMIC_COMBO | Sim | `"recraftv4_1"`<br>`"recraftv4_1_utility"`<br>`"recraftv4_1_pro"`<br>`"recraftv4_1_utility_pro"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | Prompt para a geração da imagem. Máximo de 10.000 caracteres. | STRING | Sim | N/A |
| `prompt_negativo` | Esta entrada é ignorada: o prompt negativo não é compatível com os modelos Recraft V4 e V4.1. | STRING | Sim | N/A |
| `n` | O número de imagens a serem geradas (padrão: 1). | INT | Sim | 1 a 6 |
| `semente` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos, independentemente da semente (padrão: 0). | INT | Sim | 0 a 18446744073709551615 |
| `recraft_controls` | Controles adicionais opcionais sobre a geração por meio do nó Recraft Controls. | CUSTOM | Não | N/A |

### Entradas de recraftv4_1, recraftv4_1_utility e recraftv4

Compartilhadas por `recraftv4_1`, `recraftv4_1_utility` e `recraftv4`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `size` | O tamanho da imagem gerada (padrão: "1024x1024"). | COMBO | Sim | Várias opções disponíveis (tamanhos padrão do Recraft V4, inclui "1024x1024") |

### Entradas de recraftv4_1_pro, recraftv4_1_utility_pro e recraftv4_pro

Compartilhadas por `recraftv4_1_pro`, `recraftv4_1_utility_pro` e `recraftv4_pro`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `size` | O tamanho da imagem gerada (padrão: "2048x2048"). | COMBO | Sim | Várias opções disponíveis (tamanhos Pro do Recraft V4, inclui "2048x2048") |

**Nota:** O parâmetro `size` é uma entrada dinâmica cujas opções disponíveis mudam de acordo com o `model` selecionado. O valor de `seed` não garante resultados de imagem reproduzíveis. Se você usar um ID de estilo da Infinite Style Library, certifique-se de que não seja um estilo de arte vetorial, pois isso pode retornar dados SVG em vez de uma imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `output` | A imagem gerada ou o lote de imagens. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0b345a2f84d20a5a86681c358796a3ee3a5a101aab62441a978c610854e02c8a`
