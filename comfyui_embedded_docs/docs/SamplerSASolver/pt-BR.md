# SamplerSASolver

O nó SamplerSASolver implementa um algoritmo de amostragem personalizado para modelos de difusão. Ele usa uma abordagem preditor-corretor com configurações de ordem ajustáveis e parâmetros de equação diferencial estocástica (SDE) para gerar amostras a partir do modelo de entrada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de difusão a ser usado para amostragem | MODEL | Sim | - |
| `eta` | Controla o fator de escala do tamanho do passo (padrão: 1.0) | FLOAT | Não | 0.0 - 10.0 |
| `percentual_inicial_sde` | O percentual inicial para amostragem SDE (padrão: 0.2) | FLOAT | Não | 0.0 - 1.0 |
| `percentual_final_sde` | O percentual final para amostragem SDE (padrão: 0.8) | FLOAT | Não | 0.0 - 1.0 |
| `s_noise` | Controla a quantidade de ruído adicionada durante a amostragem (padrão: 1.0) | FLOAT | Não | 0.0 - 100.0 |
| `ordem_do_preditor` | A ordem do componente preditor no solucionador (padrão: 3) | INT | Não | 1 - 6 |
| `ordem_do_corretor` | A ordem do componente corretor no solucionador (padrão: 4) | INT | Não | 0 - 6 |
| `usar_pece` | Ativa ou desativa o método PECE (Predict-Evaluate-Correct-Evaluate) | BOOLEAN | Não | - |
| `ordem_simples_2` | Ativa ou desativa cálculos simplificados de segunda ordem | BOOLEAN | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sampler` | Um objeto de amostrador configurado que pode ser usado com modelos de difusão | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/pt-BR.md)

---
**Source fingerprint (SHA-256):** `31da2d436665bf533c28b32248f632edab8f6d92372402904702ae954230f98d`
