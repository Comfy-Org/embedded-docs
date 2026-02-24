> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetArea/pt-BR.md)

Este nó é projetado para modificar as informações de condicionamento definindo áreas específicas dentro do contexto de condicionamento. Ele permite a manipulação espacial precisa dos elementos de condicionamento, possibilitando ajustes e aprimoramentos direcionados com base em dimensões e intensidade especificadas.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Os dados de condicionamento a serem modificados. Servem como base para a aplicação dos ajustes espaciais. |
| `width`   | `INT`      | Especifica a largura da área a ser definida dentro do contexto de condicionamento, influenciando o escopo horizontal do ajuste. |
| `height`  | `INT`      | Determina a altura da área a ser definida, afetando a extensão vertical da modificação de condicionamento. |
| `x`       | `INT`      | O ponto de partida horizontal da área a ser definida, posicionando o ajuste dentro do contexto de condicionamento. |
| `y`       | `INT`      | O ponto de partida vertical para o ajuste da área, estabelecendo sua posição dentro do contexto de condicionamento. |
| `strength`| `FLOAT`    | Define a intensidade da modificação de condicionamento dentro da área especificada, permitindo um controle refinado sobre o impacto do ajuste. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | Os dados de condicionamento modificados, refletindo as configurações e ajustes da área especificada. |
