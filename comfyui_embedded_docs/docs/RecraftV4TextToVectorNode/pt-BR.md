# Recraft V4 Texto para Vetor

O nó Recraft V4 Text to Vector gera ilustrações em SVG (Scalable Vector Graphics) a partir de uma descrição textual usando os modelos Recraft V4 e V4.1. Ele se conecta à API da Recraft para gerar um ou mais arquivos SVG com base no seu prompt, e pode aplicar um estilo vetorial existente ou criar um novo a partir de imagens de referência — quando imagens de referência são usadas, o estilo criado é retornado como `style_id` para reutilização.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo a ser usado para a geração. Os modelos recraftv4_styles são criados para geração consistente de estilo e sempre exigem um style_id ou style_references. Selecionar um modelo altera as opções de `size` disponíveis. | DYNAMIC_COMBO | Sim | `"recraftv4_1_vector"`<br>`"recraftv4_1_utility_vector"`<br>`"recraftv4_1_pro_vector"`<br>`"recraftv4_1_utility_pro_vector"`<br>`"recraftv4"`<br>`"recraftv4_pro"`<br>`"recraftv4_styles_vector"`<br>`"recraftv4_styles_pro_vector"` |
| `prompt` | Prompt para a geração da imagem. Máximo de 10.000 caracteres. | STRING | Sim | N/D |
| `prompt_negativo` | Esta entrada é ignorada: prompt negativo não é suportado pelos modelos Recraft V4 e V4.1. | STRING | Sim | N/D |
| `n` | O número de imagens a gerar (padrão: 1). | INT | Sim | 1 a 6 |
| `semente` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0). | INT | Sim | 0 a 18446744073709551615 |
| `recraft_controls` | Controles adicionais opcionais sobre a geração por meio do nó Recraft Controls. | CUSTOM | Não | N/D |
| `style_id` | UUID de um estilo vetorial do Recraft V4 a ser aplicado, por exemplo, do nó Recraft V4 Create Style ou da saída style_id de uma execução anterior. Não pode ser combinado com style_references. | STRING | Não | N/D |
| `style_match` | O quão fielmente seguir o estilo: precise reproduz o estilo em detalhes, flexible corresponde à aparência geral. Usado apenas quando um estilo é fornecido (padrão: "precise"). | COMBO | Não | `"precise"`<br>`"flexible"` |

### Entradas de recraftv4_1_vector, recraftv4_1_utility_vector, recraftv4 e recraftv4_styles_vector

Estes modelos compartilham as mesmas opções de `size`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `size` | O tamanho da imagem gerada. O padrão é `"1024x1024"`. | COMBO | Sim | `"1024x1024"`<br>`"1152x896"`<br>`"896x1152"`<br>`"1216x832"`<br>`"832x1216"`<br>`"1344x768"`<br>`"768x1344"`<br>`"1536x640"`<br>`"640x1536"` |

### Entradas de recraftv4_1_pro_vector, recraftv4_1_utility_pro_vector, recraftv4_pro e recraftv4_styles_pro_vector

Estes modelos compartilham as mesmas opções de `size`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `size` | O tamanho da imagem gerada. O padrão é `"2048x2048"`. | COMBO | Sim | `"2048x2048"`<br>`"2304x1792"`<br>`"1792x2304"`<br>`"2432x1664"`<br>`"1664x2432"`<br>`"2688x1536"`<br>`"1536x2688"`<br>`"3072x1280"`<br>`"1280x3072"` |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `style_references` | Imagens de referência para criar um estilo vetorial em tempo real, cobradas além da geração. O estilo criado é retornado como style_id para reutilização. Não pode ser combinado com style_id. | IMAGE | Não | Slot expansível: conecte de 1 a N imagens de referência (até o máximo do nó) |

**Observação:** O parâmetro `size` é uma entrada dinâmica cujas opções disponíveis mudam com base no `model` selecionado. O valor de `seed` não garante resultados reproduzíveis da API externa. Os modelos `recraftv4_styles_vector` e `recraftv4_styles_pro_vector` sempre exigem um estilo: forneça um `style_id` ou conecte pelo menos uma imagem de `style_references`. `style_id` e `style_references` não podem ser usados juntos — fornecer ambos gera um erro, e `style_id` deve ser um UUID válido. As imagens de referência são limitadas em quantidade e seu tamanho total codificado não deve exceder 10 MB.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A(s) imagem(ns) em SVG (Scalable Vector Graphics) gerada(s). | SVG |
| `style_id` | O UUID do estilo retornado pela API da Recraft. Quando imagens de referência são fornecidas, o estilo criado é retornado aqui para reutilização; caso contrário, string vazia. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `182a40b206b164cf2e96c7344d23e4906b7d61b90e3000743a3fd31941e08539`
