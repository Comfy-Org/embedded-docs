# Recraft V4 Texto para Imagem

Este nó gera imagens a partir de descrições textuais usando os modelos de IA Recraft V4 e V4.1. Ele envia o prompt e as configurações de geração para o serviço de geração de imagens Recraft e retorna a imagem ou as imagens resultantes. Você pode escolher o modelo, o tamanho da imagem e o número de imagens a serem geradas.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo a ser usado na geração. A seleção de um modelo determina as opções de `size` disponíveis. | DYNAMIC_COMBO | Sim | `"recraftv4_1"`<br>`"recraftv4_1_utility"`<br>`"recraftv4_1_pro"`<br>`"recraftv4_1_utility_pro"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | Prompt para a geração da imagem. Máximo de 10.000 caracteres. | STRING | Sim | 1 a 10000 caracteres |
| `negative_prompt` | Esta entrada é ignorada: o prompt negativo não é suportado pelos modelos Recraft V4 e V4.1. | STRING | Sim | N/A |
| `n` | O número de imagens a gerar (padrão: 1). | INT | Sim | 1 a 6 |
| `seed` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0). | INT | Sim | 0 a 18446744073709551615 |
| `recraft_controls` | Controles adicionais opcionais sobre a geração por meio do nó Recraft Controls. | CUSTOM | Não | N/A |

### Entradas de recraftv4_1, recraftv4_1_utility e recraftv4

Compartilhadas pelos modelos `recraftv4_1`, `recraftv4_1_utility` e `recraftv4`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `size` | O tamanho da imagem gerada (padrão: 1024x1024). | COMBO | Sim | Várias opções disponíveis (tamanhos padrão do Recraft V4) |

### Entradas de recraftv4_1_pro, recraftv4_1_utility_pro e recraftv4_pro

Compartilhadas pelos modelos `recraftv4_1_pro`, `recraftv4_1_utility_pro` e `recraftv4_pro`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `size` | O tamanho da imagem gerada (padrão: 2048x2048). | COMBO | Sim | Várias opções disponíveis (tamanhos Pro do Recraft V4) |

**Notas:**

- A entrada `size` aparece quando um modelo é selecionado, e suas opções disponíveis dependem do modelo: os modelos padrão (`recraftv4_1`, `recraftv4_1_utility`, `recraftv4`) compartilham um conjunto de tamanhos, enquanto os modelos Pro (`recraftv4_1_pro`, `recraftv4_1_utility_pro`, `recraftv4_pro`) compartilham um conjunto diferente.
- A entrada `negative_prompt` é exibida na interface, mas não é enviada ao modelo; prompts negativos não são suportados pelos modelos Recraft V4 e V4.1.
- O valor de `seed` apenas determina se o nó é executado novamente quando o valor muda; os resultados reais da imagem são não determinísticos independentemente da semente.
- Se você usar um ID de estilo da Infinite Style Library por meio da entrada Recraft Controls, certifique-se de que não seja um estilo de arte vetorial, pois isso pode retornar dados SVG em vez de uma imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A imagem gerada ou o lote de imagens. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0b345a2f84d20a5a86681c358796a3ee3a5a101aab62441a978c610854e02c8a`
