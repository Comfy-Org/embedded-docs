> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/pt-BR.md)

O nó Flux2Scheduler gera uma sequência de níveis de ruído (sigmas) para o processo de remoção de ruído, especificamente adaptado para o modelo Flux. Ele calcula um cronograma com base no número de etapas de remoção de ruído e nas dimensões da imagem alvo, o que influencia a progressão da remoção de ruído durante a geração da imagem.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `steps` | INT | Sim | 1 a 4096 | O número de etapas de remoção de ruído a serem executadas. Um valor maior geralmente resulta em detalhes mais refinados, mas aumenta o tempo de processamento (padrão: 20). |
| `width` | INT | Sim | 16 a 16384 | A largura da imagem a ser gerada, em pixels. Este valor influencia o cálculo do cronograma de ruído (padrão: 1024). |
| `height` | INT | Sim | 16 a 16384 | A altura da imagem a ser gerada, em pixels. Este valor influencia o cálculo do cronograma de ruído (padrão: 1024). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Uma sequência de valores de nível de ruído (sigmas) que define o cronograma de remoção de ruído para o amostrador. |
