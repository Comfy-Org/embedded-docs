# SamplerSASolver

O nó SamplerSASolver implementa um algoritmo de amostragem personalizado para modelos de difusão. Ele utiliza uma abordagem preditor-corretor com configurações de ordem ajustáveis e parâmetros de equação diferencial estocástica (SDE) para gerar amostras a partir do modelo de entrada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de difusão a ser usado para amostragem | MODEL | Sim | - |
| `eta` | Controla o fator de escala do tamanho do passo (padrão: 1,0) | FLOAT | Não | 0,0 - 10,0 |
| `percentual_inicial_sde` | A porcentagem inicial para amostragem SDE (padrão: 0,2) | FLOAT | Não | 0,0 - 1,0 |
| `percentual_final_sde` | A porcentagem final para amostragem SDE (padrão: 0,8) | FLOAT | Não | 0,0 - 1,0 |
| `s_noise` | Controla a quantidade de ruído adicionada durante a amostragem (padrão: 1,0) | FLOAT | Não | 0,0 - 100,0 |
| `ordem_do_preditor` | A ordem do componente preditor no solucionador (padrão: 3) | INT | Não | 1 - 6 |
| `ordem_do_corretor` | A ordem do componente corretor no solucionador (padrão: 4) | INT | Não | 0 - 6 |
| `usar_pece` | Ativa ou desativa o método PECE (Predict-Evaluate-Correct-Evaluate) | BOOLEAN | Não | - |
| `ordem_simples_2` | Ativa ou desativa cálculos simplificados de segunda ordem | BOOLEAN | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sampler` | Um objeto amostrador configurado que pode ser usado com modelos de difusão | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3de8834281c09d0bd1435e29f0c9ae540a2ea42db142277d07cb655ccf814873`
