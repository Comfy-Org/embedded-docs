> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4TextToImageNode/pt-BR.md)

Este nó gera imagens a partir de descrições de texto usando os modelos de IA Recraft V4 ou V4 Pro. Ele envia seu prompt para uma API externa e retorna as imagens geradas. Você pode controlar a saída especificando o modelo, o tamanho da imagem e o número de imagens a serem criadas.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | N/A | Prompt para a geração da imagem. Máximo de 10.000 caracteres. |
| `negative_prompt` | STRING | Não | N/A | Uma descrição de texto opcional de elementos indesejados em uma imagem. |
| `model` | COMBO | Sim | `"recraftv4"`<br>`"recraftv4_pro"` | O modelo a ser usado para a geração. A seleção de um modelo determina os tamanhos de imagem disponíveis. |
| `size` | COMBO | Sim | Varia por modelo | O tamanho da imagem gerada. As opções disponíveis dependem do modelo selecionado. Para `recraftv4`, o padrão é "1024x1024". Para `recraftv4_pro`, o padrão é "2048x2048". |
| `n` | INT | Sim | 1 a 6 | O número de imagens a serem geradas (padrão: 1). |
| `seed` | INT | Sim | 0 a 18446744073709551615 | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0). |
| `recraft_controls` | CUSTOM | Não | N/A | Controles adicionais opcionais sobre a geração via o nó Recraft Controls. |

**Observação:** O parâmetro `size` é uma entrada dinâmica cujas opções disponíveis mudam com base no `model` selecionado. O valor da `seed` não garante saídas de imagem reproduzíveis.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | IMAGE | A imagem gerada ou o lote de imagens. |
