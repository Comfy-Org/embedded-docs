> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Morphology/pt-BR.md)

O nó Morphology aplica várias operações morfológicas a imagens, que são operações matemáticas usadas para processar e analisar formas em imagens. Ele pode executar operações como erosão, dilatação, abertura, fechamento e mais, usando um tamanho de kernel personalizável para controlar a intensidade do efeito.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser processada |
| `operation` | STRING | Sim | `"erode"`<br>`"dilate"`<br>`"open"`<br>`"close"`<br>`"gradient"`<br>`"bottom_hat"`<br>`"top_hat"` | A operação morfológica a ser aplicada |
| `kernel_size` | INT | Não | 3-999 | O tamanho do kernel do elemento estruturante (padrão: 3) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem processada após a aplicação da operação morfológica |
