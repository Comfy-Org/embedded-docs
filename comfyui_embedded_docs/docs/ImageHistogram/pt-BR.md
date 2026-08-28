# Histograma de Imagem

O nó ImageHistogram analisa a distribuição de cores de uma imagem de entrada. Ele calcula e gera vários histogramas, que são gráficos que mostram quantos pixels na imagem possuem cada valor de intensidade possível. Ele gera histogramas separados para os canais de cor vermelho, verde e azul, um histograma RGB composto e um histograma de luminância baseado em uma fórmula padrão de brilho. Cada histograma contém 256 compartimentos, cobrindo níveis de intensidade de 0 a 255.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `imagem` | A imagem de entrada para análise. O nó processa a primeira imagem do lote. | IMAGE | Sim | N/A |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `rgb` | Um histograma composto que representa a intensidade média dos pixels nos canais vermelho, verde e azul. | HISTOGRAM |
| `luminância` | Um histograma do brilho percebido da imagem, calculado usando a fórmula de luminância padrão ITU-R BT.709. | HISTOGRAM |
| `vermelho` | Um histograma mostrando a distribuição das intensidades dos pixels no canal de cor vermelho. | HISTOGRAM |
| `verde` | Um histograma mostrando a distribuição das intensidades dos pixels no canal de cor verde. | HISTOGRAM |
| `azul` | Um histograma mostrando a distribuição das intensidades dos pixels no canal de cor azul. | HISTOGRAM |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageHistogram/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5020f5cedd325250a207a00950011f4b6dc19ddfe4d172665ffca4982731dd5e`
