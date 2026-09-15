# Recraft Imagem para Imagem

Este nó modifica uma imagem existente com base em um prompt de texto e uma configuração de intensidade. Ele envia a imagem para a API Recraft V3 e retorna uma nova imagem que segue o prompt, permanecendo mais ou menos semelhante à original, dependendo do valor de `strength`.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | A imagem de entrada a ser modificada. Quando um lote de imagens é fornecido, cada imagem é processada individualmente. | IMAGE | Sim | - |
| `prompt` | Prompt para a geração da imagem. Padrão: string vazia. Comprimento máximo: 1000 caracteres. | STRING | Sim | - |
| `n` | O número de imagens a gerar. Padrão: 1. | INT | Sim | 1-6 |
| `intensidade` | Define a diferença em relação à imagem original; deve estar em [0, 1], onde 0 significa quase idêntica e 1 significa similaridade mínima. Padrão: 0.5. | FLOAT | Sim | 0.0-1.0 (passo 0.01) |
| `semente` | Semente para determinar se o nó deve ser reexecutado; os resultados reais são não determinísticos independentemente da semente. Padrão: 0. | INT | Sim | 0-18446744073709551615 |
| `recraft_style` | Seleção de estilo opcional para a geração da imagem. Se não for fornecida, o padrão é `realistic_image`. | STYLEV3 | Não | - |
| `prompt_negativo` | Descrição de texto opcional de elementos indesejados em uma imagem. Padrão: string vazia. Fornecida como um soquete de entrada. | STRING | Não | - |
| `recraft_controls` | Controles adicionais opcionais sobre a geração por meio do nó Recraft Controls. | CONTROLS | Não | - |

**Nota:** O parâmetro `seed` apenas dispara a reexecução do nó, mas não garante resultados determinísticos. O parâmetro `strength` é arredondado para 2 casas decimais internamente. O `prompt` é validado e não deve exceder 1000 caracteres. Um `negative_prompt` vazio é tratado como ausência de prompt negativo. Se `recraft_style` não for fornecido, o nó usa o estilo `realistic_image` por padrão. Se você usar um `style_id` da Infinite Style Library, certifique-se de que ele não seja um estilo Vector art, pois isso pode fazer o nó receber dados SVG em vez de uma imagem, resultando em erro. Quando a `image` de entrada é um lote, cada imagem do lote é processada individualmente e todos os resultados são retornados juntos.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `image` | A(s) imagem(ns) gerada(s) com base na imagem de entrada, no prompt e na intensidade. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1932e55d1dc392e6bd42a0bd29f5aaba44b65997b597648a927fba38a27c90ad`
