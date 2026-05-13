> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageHistogram/pt-BR.md)

O nó ImageHistogram analisa a distribuição de cores de uma imagem de entrada. Ele calcula e gera vários histogramas, que são gráficos que mostram quantos pixels na imagem possuem cada valor de intensidade possível. Ele gera histogramas separados para os canais de cores vermelho, verde e azul, um histograma RGB composto e um histograma de luminância baseado em uma fórmula de brilho padrão.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `image` | IMAGE | Sim | N/A | A imagem de entrada para análise. O nó processa a primeira imagem do lote. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `rgb` | HISTOGRAM | Um histograma composto representando a intensidade média dos pixels nos canais vermelho, verde e azul. |
| `luminance` | HISTOGRAM | Um histograma do brilho percebido da imagem, calculado usando a fórmula de luminância padrão ITU-R BT.709. |
| `red` | HISTOGRAM | Um histograma mostrando a distribuição das intensidades dos pixels no canal de cor vermelho. |
| `green` | HISTOGRAM | Um histograma mostrando a distribuição das intensidades dos pixels no canal de cor verde. |
| `blue` | HISTOGRAM | Um histograma mostrando a distribuição das intensidades dos pixels no canal de cor azul. |

---
**Source fingerprint (SHA-256):** `9bfcdb2907ab1e5cb2a9a736671fb9286b0e6ce6439fab95187f691b969ea53d`
