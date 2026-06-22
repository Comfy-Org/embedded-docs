# FreSca

O nó FreSca aplica escalonamento dependente de frequência à orientação durante o processo de amostragem. Ele separa o sinal de orientação em componentes de baixa e alta frequência usando filtragem de Fourier, em seguida, aplica diferentes fatores de escalonamento para cada faixa de frequência antes de recombiná-los. Isso permite um controle mais sutil sobre como a orientação afeta diferentes aspectos da saída gerada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo ao qual aplicar o escalonamento de frequência | MODEL | Sim | - |
| `scale_low` | Fator de escalonamento para componentes de baixa frequência (padrão: 1.0) | FLOAT | Não | 0 - 10 |
| `scale_high` | Fator de escalonamento para componentes de alta frequência (padrão: 1.25) | FLOAT | Não | 0 - 10 |
| `freq_cutoff` | Número de índices de frequência ao redor do centro a serem considerados como baixa frequência (padrão: 20) | INT | Não | 1 - 10000 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo modificado com escalonamento dependente de frequência aplicado à sua função de orientação | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreSca/pt-BR.md)

---
**Source fingerprint (SHA-256):** `254a28847e082739f80c9637d9657ef618d40db1862b6856c1cda22436438ded`
