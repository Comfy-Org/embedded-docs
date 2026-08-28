# Recraft Imagem para Imagem

Este nó modifica uma imagem existente com base em um prompt de texto e um parâmetro de força. Ele usa a API Recraft V3 para transformar a imagem de entrada de acordo com a descrição fornecida, mantendo alguma similaridade com a imagem original, controlada pela configuração de força.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | A imagem de entrada a ser modificada | IMAGE | Sim | - |
| `prompt` | Prompt para a geração da imagem (padrão: string vazia, comprimento máximo: 1000 caracteres) | STRING | Sim | - |
| `n` | O número de imagens a serem geradas (padrão: 1) | INT | Sim | 1-6 |
| `intensidade` | Define a diferença em relação à imagem original; deve estar em [0, 1], em que 0 significa quase idêntica e 1 significa similaridade mínima (padrão: 0.5) | FLOAT | Sim | 0.0-1.0 |
| `semente` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0) | INT | Sim | 0-18446744073709551615 |
| `recraft_style` | Seleção opcional de estilo para a geração da imagem. Se não for fornecida, o padrão é `realistic_image` | STYLEV3 | Não | - |
| `prompt_negativo` | Uma descrição textual opcional de elementos indesejados em uma imagem (padrão: string vazia) | STRING | Não | - |
| `recraft_controls` | Controles adicionais opcionais sobre a geração por meio do nó Recraft Controls | CONTROLS | Não | - |

**Nota:** O parâmetro `seed` apenas aciona a reexecução do nó, mas não garante resultados determinísticos. O parâmetro `strength` é arredondado internamente para 2 casas decimais. O `prompt` é validado e não deve exceder 1000 caracteres. Um `negative_prompt` vazio é tratado como ausência de prompt negativo. Se `recraft_style` não for fornecido, o nó usa o estilo `realistic_image` por padrão. Se você usar um `style_id` da Infinite Style Library, certifique-se de que não seja um estilo de arte vetorial, pois isso pode fazer com que o nó receba dados SVG em vez de uma imagem, resultando em erro. Quando a `image` de entrada for um lote, cada imagem do lote é processada individualmente e todos os resultados são retornados em conjunto.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A(s) imagem(ns) gerada(s) com base na imagem de entrada e no prompt | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1932e55d1dc392e6bd42a0bd29f5aaba44b65997b597648a927fba38a27c90ad`
