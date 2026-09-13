# SamplerSASolver

O nó SamplerSASolver cria e configura um amostrador personalizado para modelos de difusão. Ele usa o algoritmo de amostragem "sa_solver" com um esquema preditor-corretor configurável e configurações de equação diferencial estocástica (SDE), retornando um objeto amostrador que pode ser conectado a um nó de amostragem. Os valores `sde_start_percent` e `sde_end_percent` são convertidos em valores sigma usando o cronograma de amostragem do modelo conectado para definir o intervalo no qual o componente estocástico é aplicado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão cujo cronograma de amostragem é usado para construir o amostrador | MODEL | Sim | - |
| `eta` | Controla o fator de escala do tamanho do passo do solucionador SDE (padrão: 1.0) | FLOAT | Não | 0.0 - 10.0 |
| `sde_start_percent` | Percentual inicial do processo de amostragem em que o componente estocástico (SDE) começa; convertido em um valor sigma usando o cronograma do modelo (padrão: 0.2) | FLOAT | Não | 0.0 - 1.0 |
| `sde_end_percent` | Percentual final do processo de amostragem em que o componente estocástico (SDE) para; convertido em um valor sigma usando o cronograma do modelo (padrão: 0.8) | FLOAT | Não | 0.0 - 1.0 |
| `s_noise` | Controla a quantidade de ruído adicionada durante a amostragem (padrão: 1.0) | FLOAT | Não | 0.0 - 100.0 |
| `predictor_order` | A ordem do componente preditor no solucionador (padrão: 3) | INT | Não | 1 - 6 |
| `corrector_order` | A ordem do componente corretor no solucionador (padrão: 4) | INT | Não | 0 - 6 |
| `use_pece` | Habilita o método PECE (Predict-Evaluate-Correct-Evaluate) (padrão: desabilitado) | BOOLEAN | Não | - |
| `simple_order_2` | Habilita cálculos simplificados de segunda ordem (padrão: desabilitado) | BOOLEAN | Não | - |

Todas as entradas opcionais estão marcadas como avançadas na interface.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sampler` | Um objeto amostrador configurado (usando o algoritmo `sa_solver`) que pode ser usado por nós de amostragem | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/pt-BR.md)

---
**Source fingerprint (SHA-256):** `31da2d436665bf533c28b32248f632edab8f6d92372402904702ae954230f98d`
