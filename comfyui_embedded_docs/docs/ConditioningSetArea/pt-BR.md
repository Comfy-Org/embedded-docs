Este nó foi projetado para modificar as informações de condicionamento, definindo áreas específicas dentro do contexto de condicionamento. Ele permite a manipulação espacial precisa dos elementos de condicionamento, possibilitando ajustes e aprimoramentos direcionados com base em dimensões e intensidade especificadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento a serem modificados. Servem como base para aplicar ajustes espaciais. | CONDITIONING |
| `largura` | Especifica a largura da área a ser definida dentro do contexto de condicionamento, influenciando o escopo horizontal do ajuste. | `INT` |
| `altura` | Determina a altura da área a ser definida, afetando a extensão vertical da modificação do condicionamento. | `INT` |
| `x` | O ponto de partida horizontal da área a ser definida, posicionando o ajuste dentro do contexto de condicionamento. | `INT` |
| `y` | O ponto de partida vertical para o ajuste da área, estabelecendo sua posição dentro do contexto de condicionamento. | `INT` |
| `força` | Define a intensidade da modificação do condicionamento dentro da área especificada, permitindo controle sutil sobre o impacto do ajuste. | `FLOAT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento modificados, refletindo as configurações e ajustes de área especificados. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetArea/pt-BR.md)
