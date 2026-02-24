> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/pt-BR.md)

Este nó aplica o Reajuste de Pontuação Temporal (Temporal Score Rescaling - TSR) a um modelo de difusão. Ele modifica o comportamento de amostragem do modelo reajustando o ruído ou a pontuação prevista durante o processo de remoção de ruído, o que pode direcionar a diversidade da saída gerada. Isso é implementado como uma função pós-CFG (Orientação Livre de Classificador).

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo de difusão a ser modificado com a função TSR. |
| `tsr_k` | FLOAT | Não | 0.01 - 100.0 | Controla a intensidade do reajuste. Um k mais baixo produz resultados mais detalhados; um k mais alto produz resultados mais suaves na geração de imagens. Definir k = 1 desativa o reajuste. (padrão: 0.95) |
| `tsr_sigma` | FLOAT | Não | 0.01 - 100.0 | Controla quão cedo o reajuste entra em vigor. Valores maiores entram em vigor mais cedo. (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `patched_model` | MODEL | O modelo de entrada, agora modificado com a função de Reajuste de Pontuação Temporal aplicada ao seu processo de amostragem. |
