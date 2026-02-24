> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/pt-BR.md)

O nó LTXVConditioning adiciona informações de taxa de quadros (frame rate) tanto ao condicionamento positivo quanto ao negativo para modelos de geração de vídeo. Ele recebe dados de condicionamento existentes e aplica o valor de taxa de quadros especificado a ambos os conjuntos de condicionamento, tornando-os adequados para o processamento de modelos de vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | A entrada de condicionamento positivo que receberá a informação de taxa de quadros |
| `negative` | CONDITIONING | Sim | - | A entrada de condicionamento negativo que receberá a informação de taxa de quadros |
| `frame_rate` | FLOAT | Não | 0.0 - 1000.0 | O valor da taxa de quadros a ser aplicado a ambos os conjuntos de condicionamento (padrão: 25.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | O condicionamento positivo com a informação de taxa de quadros aplicada |
| `negative` | CONDITIONING | O condicionamento negativo com a informação de taxa de quadros aplicada |
