> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreSca/pt-BR.md)

O nó FreSca aplica escalonamento dependente de frequência à orientação durante o processo de amostragem. Ele separa o sinal de orientação em componentes de baixa e alta frequência usando filtragem de Fourier, em seguida, aplica diferentes fatores de escalonamento para cada faixa de frequência antes de recombiná-los. Isso permite um controle mais sutil sobre como a orientação afeta diferentes aspectos da saída gerada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo ao qual aplicar o escalonamento de frequência |
| `scale_low` | FLOAT | Não | 0 - 10 | Fator de escalonamento para componentes de baixa frequência (padrão: 1.0) |
| `scale_high` | FLOAT | Não | 0 - 10 | Fator de escalonamento para componentes de alta frequência (padrão: 1.25) |
| `freq_cutoff` | INT | Não | 1 - 10000 | Número de índices de frequência ao redor do centro a serem considerados como baixa frequência (padrão: 20) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com escalonamento dependente de frequência aplicado à sua função de orientação |

---
**Source fingerprint (SHA-256):** `254a28847e082739f80c9637d9657ef618d40db1862b6856c1cda22436438ded`
