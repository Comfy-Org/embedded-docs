> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoLinearCFGGuidance/pt-BR.md)

O nó VideoLinearCFGGuidance aplica uma escala de orientação de condicionamento linear a um modelo de vídeo, ajustando a influência dos componentes condicionados e não condicionados em um intervalo especificado. Isso permite um controle dinâmico sobre o processo de geração, possibilitando o ajuste fino da saída do modelo com base no nível de condicionamento desejado.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `model`   | MODEL     | O parâmetro `model` representa o modelo de vídeo ao qual a orientação CFG linear será aplicada. É crucial para definir o modelo base que será modificado com a escala de orientação. |
| `min_cfg` | `FLOAT`     | O parâmetro `min_cfg` especifica a escala mínima de orientação de condicionamento a ser aplicada, servindo como ponto de partida para o ajuste da escala linear. Ele desempenha um papel fundamental na determinação do limite inferior da escala de orientação, influenciando a saída do modelo. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `model`   | MODEL     | A saída é uma versão modificada do modelo de entrada, com a escala de orientação CFG linear aplicada. Este modelo ajustado é capaz de gerar saídas com diferentes graus de condicionamento, com base na escala de orientação especificada. |
