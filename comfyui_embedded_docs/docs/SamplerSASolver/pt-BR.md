# SamplerSASolver

O nó SamplerSASolver implementa um algoritmo de amostragem personalizado para modelos de difusão. Ele usa uma abordagem preditor-corretor com configurações de ordem ajustáveis e parâmetros de equação diferencial estocástica (SDE) para gerar amostras a partir do modelo de entrada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de difusão a ser usado para amostragem | MODEL | Sim | - |
| `eta` | Controla o fator de escala do tamanho do passo (padrão: 1.0) | FLOAT | Não | 0.0 - 10.0 |
| `sde_start_percent` | A porcentagem inicial do processo de remoção de ruído onde a amostragem SDE começa, convertida em um valor sigma usando o agendamento de amostragem do modelo (padrão: 0.2) | FLOAT | Não | 0.0 - 1.0 |
| `sde_end_percent` | A porcentagem final do processo de remoção de ruído onde a amostragem SDE para, convertida em um valor sigma usando o agendamento de amostragem do modelo (padrão: 0.8) | FLOAT | Não | 0.0 - 1.0 |
| `s_noise` | Controla a quantidade de ruído adicionada durante a amostragem (padrão: 1.0) | FLOAT | Não | 0.0 - 100.0 |
| `predictor_order` | A ordem do componente preditor no solucionador (padrão: 3) | INT | Não | 1 - 6 |
| `corrector_order` | A ordem do componente corretor no solucionador (padrão: 4) | INT | Não | 0 - 6 |
| `use_pece` | Ativa ou desativa o método PECE (Predict-Evaluate-Correct-Evaluate) | BOOLEAN | Não | - |
| `simple_order_2` | Ativa ou desativa cálculos simplificados de segunda ordem | BOOLEAN | Não | - |

Nota: Todas as entradas, exceto `model`, são parâmetros avançados, ocultos por padrão na interface do nó.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `sampler` | Um objeto de amostrador configurado que pode ser usado com modelos de difusão | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/pt-BR.md)

---
**Source fingerprint (SHA-256):** `31da2d436665bf533c28b32248f632edab8f6d92372402904702ae954230f98d`
