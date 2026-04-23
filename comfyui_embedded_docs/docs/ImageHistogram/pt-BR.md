> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageHistogram/pt-BR.md)

O nó ImageHistogram analisa a distribuição de cores de uma imagem de entrada. Ele calcula e gera vários histogramas, que são gráficos que mostram quantos pixels na imagem possuem cada valor de intensidade possível. Ele gera histogramas separados para os canais de cor vermelho, verde e azul, um histograma RGB composto e um histograma de luminância baseado em uma fórmula padrão de brilho.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `image` | IMAGE | Sim | N/A | A imagem de entrada para análise. O nó processa a primeira imagem do lote. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `rgb` | HISTOGRAM | Um histograma composto que representa a intensidade média dos pixels nos canais vermelho, verde e azul. |
| `luminance` | HISTOGRAM | Um histograma do brilho percebido da imagem, calculado usando a fórmula padrão de luminância ITU-R BT.709. |
| `red` | HISTOGRAM | Um histograma que mostra a distribuição das intensidades dos pixels no canal de cor vermelho. |
| `green` | HISTOGRAM | Um histograma que mostra a distribuição das intensidades dos pixels no canal de cor verde. |
| `blue` | HISTOGRAM | Um histograma que mostra a distribuição das intensidades dos pixels no canal de cor azul. |