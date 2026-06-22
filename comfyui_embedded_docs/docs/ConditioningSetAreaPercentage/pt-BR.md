# Condicionamento (Definir Área com Percentual)

O nó **ConditioningSetAreaPercentage** é especializado em ajustar a área de influência de elementos de condicionamento com base em valores percentuais. Ele permite especificar as dimensões e a posição da área como porcentagens do tamanho total da imagem, juntamente com um parâmetro de intensidade para modular a força do efeito de condicionamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Representa os elementos de condicionamento a serem modificados, servindo como base para aplicar ajustes de área e intensidade. | CONDITIONING |
| `largura` | Especifica a largura da área como uma porcentagem da largura total da imagem, influenciando quanto da imagem o condicionamento afeta horizontalmente. | `FLOAT` |
| `altura` | Determina a altura da área como uma porcentagem da altura total da imagem, afetando a extensão vertical da influência do condicionamento. | `FLOAT` |
| `x` | Indica o ponto inicial horizontal da área como uma porcentagem da largura total da imagem, posicionando o efeito de condicionamento. | `FLOAT` |
| `y` | Especifica o ponto inicial vertical da área como uma porcentagem da altura total da imagem, posicionando o efeito de condicionamento. | `FLOAT` |
| `força` | Controla a intensidade do efeito de condicionamento dentro da área especificada, permitindo ajustes finos em seu impacto. | `FLOAT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Retorna os elementos de condicionamento modificados com parâmetros de área e intensidade atualizados, prontos para processamento ou aplicação adicionais. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentage/pt-BR.md)
