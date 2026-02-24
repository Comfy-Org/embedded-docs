> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToImageNode/pt-BR.md)

Gera imagens de forma síncrona com base em prompt e resolução. Este nó conecta-se à API Recraft para criar imagens a partir de descrições de texto com dimensões e opções de estilo especificadas.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Prompt para a geração da imagem. (padrão: "") |
| `size` | COMBO | Sim | "1024x1024"<br>"1152x896"<br>"896x1152"<br>"1216x832"<br>"832x1216"<br>"1344x768"<br>"768x1344"<br>"1536x640"<br>"640x1536" | O tamanho da imagem gerada. (padrão: "1024x1024") |
| `n` | INT | Sim | 1-6 | O número de imagens a serem geradas. (padrão: 1) |
| `seed` | INT | Sim | 0-18446744073709551615 | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente. (padrão: 0) |
| `recraft_style` | COMBO | Não | Múltiplas opções disponíveis | Seleção de estilo opcional para a geração de imagem. |
| `negative_prompt` | STRING | Não | - | Uma descrição de texto opcional de elementos indesejados em uma imagem. (padrão: "") |
| `recraft_controls` | COMBO | Não | Múltiplas opções disponíveis | Controles adicionais opcionais sobre a geração via o nó Recraft Controls. |

**Nota:** O parâmetro `seed` controla apenas quando o nó é executado novamente, mas não torna a geração de imagem determinística. As imagens de saída reais variarão mesmo com o mesmo valor de semente.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | A(s) imagem(ns) gerada(s) como saída de tensor. |
