# Recraft V4 Texto para Vetor

O nó Recraft V4 Text to Vector gera ilustrações em Gráficos Vetoriais Escaláveis (SVG) a partir de uma descrição em texto. Ele se conecta à API da Recraft para gerar imagens usando os modelos Recraft V4 e V4.1 e produz um ou mais arquivos SVG com base no seu prompt.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `modelo` | O modelo a ser usado para a geração. A seleção de um modelo altera as opções disponíveis de `size`. | DYNAMIC_COMBO | Sim | `"recraftv4_1_vector"`<br>`"recraftv4_1_utility_vector"`<br>`"recraftv4_1_pro_vector"`<br>`"recraftv4_1_utility_pro_vector"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | Prompt para a geração da imagem. Máximo de 10.000 caracteres. | STRING | Sim | N/A |
| `prompt_negativo` | Esta entrada é ignorada: o prompt negativo não é suportado pelos modelos Recraft V4 e V4.1. | STRING | Sim | N/A |
| `n` | O número de imagens a serem geradas (padrão: 1). | INT | Sim | 1 a 6 |
| `semente` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0). | INT | Sim | 0 a 18446744073709551615 |
| `recraft_controls` | Controles adicionais opcionais sobre a geração por meio do nó Recraft Controls. | CUSTOM | Não | N/A |

### Entradas do recraftv4_1_vector, recraftv4_1_utility_vector e recraftv4

Esses modelos compartilham as mesmas opções de `size`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `size` | O tamanho da imagem gerada. O padrão é `"1024x1024"`. | COMBO | Sim | `"1024x1024"`<br>`"1152x896"`<br>`"896x1152"`<br>`"1216x832"`<br>`"832x1216"`<br>`"1344x768"`<br>`"768x1344"`<br>`"1536x640"`<br>`"640x1536"` |

### Entradas do recraftv4_1_pro_vector, recraftv4_1_utility_pro_vector e recraftv4_pro

Esses modelos compartilham as mesmas opções de `size`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `size` | O tamanho da imagem gerada. O padrão é `"2048x2048"`. | COMBO | Sim | `"2048x2048"`<br>`"2304x1792"`<br>`"1792x2304"`<br>`"2432x1664"`<br>`"1664x2432"`<br>`"2688x1536"`<br>`"1536x2688"`<br>`"3072x1280"`<br>`"1280x3072"` |

**Observação:** O parâmetro `size` é uma entrada dinâmica cujas opções disponíveis mudam de acordo com o `model` selecionado. O valor de `seed` não garante resultados reproduzíveis pela API externa.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `output` | A(s) imagem(ns) em Gráficos Vetoriais Escaláveis (SVG) gerada(s). | SVG |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `822f6b9fef67ef6beb1eba099c41c72570a1f79e316612201c81f6e5eb91408d`
