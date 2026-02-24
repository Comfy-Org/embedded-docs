> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToVectorNode/pt-BR.md)

O nó Recraft V4 Text to Vector gera ilustrações em Scalable Vector Graphics (SVG) a partir de uma descrição textual. Ele se conecta a uma API externa para usar o modelo Recraft V4 ou Recraft V4 Pro para geração de imagens. O nó gera uma ou mais imagens SVG com base no seu prompt.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | N/A | Prompt para a geração da imagem. Máximo de 10.000 caracteres. |
| `negative_prompt` | STRING | Não | N/A | Uma descrição textual opcional de elementos indesejados na imagem. |
| `model` | COMBO | Sim | `"recraftv4"`<br>`"recraftv4_pro"` | O modelo a ser usado para a geração. A seleção de um modelo altera as opções de `size` disponíveis. |
| `size` | COMBO | Sim | Para `recraftv4`: `"1024x1024"`, `"1152x896"`, `"896x1152"`, `"1216x832"`, `"832x1216"`, `"1344x768"`, `"768x1344"`, `"1536x640"`, `"640x1536"`<br>Para `recraftv4_pro`: `"2048x2048"`, `"2304x1792"`, `"1792x2304"`, `"2432x1664"`, `"1664x2432"`, `"2688x1536"`, `"1536x2688"`, `"3072x1280"`, `"1280x3072"` | O tamanho da imagem gerada. As opções disponíveis dependem do `model` selecionado. O padrão é `"1024x1024"` para `recraftv4` e `"2048x2048"` para `recraftv4_pro`. |
| `n` | INT | Sim | 1 a 6 | O número de imagens a serem geradas (padrão: 1). |
| `seed` | INT | Sim | 0 a 18446744073709551615 | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente. |
| `recraft_controls` | CUSTOM | Não | N/A | Controles adicionais opcionais sobre a geração via o nó Recraft Controls. |

**Observação:** O parâmetro `size` é uma entrada dinâmica cujas opções disponíveis mudam com base no `model` selecionado. O valor de `seed` não garante resultados reproduzíveis da API externa.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | SVG | A(s) imagem(ns) Scalable Vector Graphics (SVG) gerada(s). |