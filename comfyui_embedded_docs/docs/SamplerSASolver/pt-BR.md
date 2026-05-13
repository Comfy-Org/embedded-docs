> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/pt-BR.md)

O nó SamplerSASolver implementa um algoritmo de amostragem personalizado para modelos de difusão. Ele utiliza uma abordagem preditor-corretor com configurações de ordem ajustáveis e parâmetros de equação diferencial estocástica (SDE) para gerar amostras a partir do modelo de entrada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo de difusão a ser usado para amostragem |
| `eta` | FLOAT | Não | 0,0 - 10,0 | Controla o fator de escala do tamanho do passo (padrão: 1,0) |
| `sde_start_percent` | FLOAT | Não | 0,0 - 1,0 | A porcentagem inicial para amostragem SDE (padrão: 0,2) |
| `sde_end_percent` | FLOAT | Não | 0,0 - 1,0 | A porcentagem final para amostragem SDE (padrão: 0,8) |
| `s_noise` | FLOAT | Não | 0,0 - 100,0 | Controla a quantidade de ruído adicionada durante a amostragem (padrão: 1,0) |
| `predictor_order` | INT | Não | 1 - 6 | A ordem do componente preditor no solucionador (padrão: 3) |
| `corrector_order` | INT | Não | 0 - 6 | A ordem do componente corretor no solucionador (padrão: 4) |
| `use_pece` | BOOLEAN | Não | - | Ativa ou desativa o método PECE (Predict-Evaluate-Correct-Evaluate) |
| `simple_order_2` | BOOLEAN | Não | - | Ativa ou desativa cálculos simplificados de segunda ordem |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Um objeto amostrador configurado que pode ser usado com modelos de difusão |

---
**Source fingerprint (SHA-256):** `3de8834281c09d0bd1435e29f0c9ae540a2ea42db142277d07cb655ccf814873`
