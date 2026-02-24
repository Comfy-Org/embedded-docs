> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreSca/pt-BR.md)

O nó FreSca aplica um escalonamento dependente de frequência ao guiamento durante o processo de amostragem. Ele separa o sinal de guiamento em componentes de baixa frequência e alta frequência usando filtragem de Fourier, aplica fatores de escala diferentes a cada faixa de frequência e, em seguida, os recombina. Isso permite um controle mais refinado sobre como o guiamento afeta diferentes aspectos da saída gerada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo ao qual aplicar o escalonamento de frequência |
| `scale_low` | FLOAT | Não | 0-10 | Fator de escala para componentes de baixa frequência (padrão: 1.0) |
| `scale_high` | FLOAT | Não | 0-10 | Fator de escala para componentes de alta frequência (padrão: 1.25) |
| `freq_cutoff` | INT | Não | 1-10000 | Número de índices de frequência em torno do centro a serem considerados como baixa frequência (padrão: 20) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com o escalonamento dependente de frequência aplicado à sua função de guiamento |
