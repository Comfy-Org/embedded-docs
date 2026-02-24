> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToVectorNode/pt-BR.md)

Gera SVG de forma síncrona com base no prompt e na resolução. Este nó cria ilustrações vetoriais enviando prompts de texto para a API do Recraft e retorna o conteúdo SVG gerado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Prompt para a geração da imagem. (padrão: "") |
| `substyle` | COMBO | Sim | Múltiplas opções disponíveis | O estilo de ilustração específico a ser usado para a geração. As opções são determinadas pelos subestilos de ilustração vetorial disponíveis no RecraftStyleV3. |
| `size` | COMBO | Sim | Múltiplas opções disponíveis | O tamanho da imagem gerada. (padrão: 1024x1024) |
| `n` | INT | Sim | 1-6 | O número de imagens a serem geradas. (padrão: 1, min: 1, max: 6) |
| `seed` | INT | Sim | 0-18446744073709551615 | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente. (padrão: 0, min: 0, max: 18446744073709551615) |
| `negative_prompt` | STRING | Não | - | Uma descrição textual opcional de elementos indesejados em uma imagem. (padrão: "") |
| `recraft_controls` | CONTROLS | Não | - | Controles adicionais opcionais sobre a geração via o nó Recraft Controls. |

**Nota:** O parâmetro `seed` controla apenas quando o nó é executado novamente, mas não torna os resultados da geração determinísticos.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `SVG` | SVG | A ilustração vetorial gerada no formato SVG |
