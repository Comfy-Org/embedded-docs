> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2V2/en.md)

## Visão Geral

Este nó gera ou edita imagens enviando um prompt de texto para a API Vertex AI do Google. Ele usa um modelo Gemini específico para criar novas imagens ou modificar imagens existentes com base em suas instruções.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | N/A | Prompt de texto descrevendo a imagem a ser gerada ou as edições a serem aplicadas. Inclua quaisquer restrições, estilos ou detalhes que o modelo deve seguir. |
| `model` | COMBO | Sim | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` | Seleciona o modelo Gemini a ser usado para geração de imagens. Atualmente, apenas uma opção está disponível. |
| `seed` | INT | Sim | 0 a 18446744073709551615 | Quando a semente é fixada em um valor específico, o modelo faz o melhor possível para fornecer a mesma resposta para solicitações repetidas. A saída determinística não é garantida. Além disso, alterar o modelo ou as configurações de parâmetros, como a temperatura, pode causar variações na resposta mesmo quando você usa o mesmo valor de semente. Por padrão, um valor de semente aleatório é usado. (padrão: 42) |
| `response_modalities` | COMBO | Sim | `"IMAGE"`<br>`"IMAGE+TEXT"` | Determina o formato da resposta. Escolha "IMAGE" para receber apenas uma imagem, ou "IMAGE+TEXT" para receber tanto uma imagem quanto uma descrição textual. (padrão: "IMAGE") |
| `system_prompt` | STRING | Não | N/A | Instruções fundamentais que ditam o comportamento de uma IA. Este é um parâmetro avançado. |

**Nota sobre o parâmetro `model`:** O parâmetro `model` é um combo dinâmico que inclui subparâmetros adicionais para resolução, proporção de aspecto e nível de raciocínio. Esses subparâmetros são definidos dentro da seleção do modelo e não são listados como entradas separadas nesta tabela.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `IMAGE` | IMAGE | A imagem gerada ou editada. |
| `STRING` | STRING | Uma descrição textual ou legenda gerada pelo modelo. |
| `thought_image` | IMAGE | Primeira imagem do processo de raciocínio do modelo. Disponível apenas com nível de raciocínio HIGH e modalidade IMAGE+TEXT. |