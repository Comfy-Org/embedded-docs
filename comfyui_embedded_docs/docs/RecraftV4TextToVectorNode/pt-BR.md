# Recraft V4 Texto para Vetor

O nó Recraft V4 Text to Vector gera imagens Scalable Vector Graphics (SVG) a partir de uma descrição em texto. Ele se conecta a uma API externa para gerar imagens usando os modelos Recraft V4 e V4.1. O nó gera uma ou mais imagens SVG com base no seu prompt.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo a ser usado para a geração. Selecionar um modelo altera as opções de `size` disponíveis. | DYNAMIC_COMBO | Sim | `"recraftv4_1_vector"`<br>`"recraftv4_1_utility_vector"`<br>`"recraftv4_1_pro_vector"`<br>`"recraftv4_1_utility_pro_vector"`<br>`"recraftv4"`<br>`"recraftv4_pro"` |
| `prompt` | Prompt para a geração da imagem. Máximo de 10.000 caracteres. | STRING | Sim | N/A |
| `negative_prompt` | Esta entrada é ignorada: o prompt negativo não é suportado pelos modelos Recraft V4 e V4.1. | STRING | Sim | N/A |
| `n` | O número de imagens a serem geradas (padrão: 1). | INT | Sim | 1 a 6 |
| `seed` | Seed para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos, independentemente da seed (padrão: 0). | INT | Sim | 0 a 18446744073709551615 |
| `recraft_controls` | Controles adicionais opcionais sobre a geração por meio do nó Recraft Controls. | CUSTOM | Não | N/A |

### Entradas de recraftv4_1_vector, recraftv4_1_utility_vector e recraftv4

Esses três modelos compartilham as mesmas opções de `size`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `size` | O tamanho da imagem gerada (padrão: `"1024x1024"`). | COMBO | Sim | `"1024x1024"`<br>`"1152x896"`<br>`"896x1152"`<br>`"1216x832"`<br>`"832x1216"`<br>`"1344x768"`<br>`"768x1344"`<br>`"1536x640"`<br>`"640x1536"` |

### Entradas de recraftv4_1_pro_vector, recraftv4_1_utility_pro_vector e recraftv4_pro

Esses três modelos compartilham as mesmas opções de `size`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `size` | O tamanho da imagem gerada (padrão: `"2048x2048"`). | COMBO | Sim | `"2048x2048"`<br>`"2304x1792"`<br>`"1792x2304"`<br>`"2432x1664"`<br>`"1664x2432"`<br>`"2688x1536"`<br>`"1536x2688"`<br>`"3072x1280"`<br>`"1280x3072"` |

**Nota:** O parâmetro `size` é uma entrada dinâmica cujas opções disponíveis mudam com base no `model` selecionado. O valor de `seed` não garante resultados reproduzíveis pela API externa. A entrada `negative_prompt` é ignorada porque os modelos Recraft V4 e V4.1 não suportam prompts negativos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A(s) imagem(ns) Scalable Vector Graphics (SVG) gerada(s). | SVG |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `822f6b9fef67ef6beb1eba099c41c72570a1f79e316612201c81f6e5eb91408d`
