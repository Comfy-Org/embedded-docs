> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSASolver/pt-BR.md)

O nó SamplerSASolver implementa um algoritmo de amostragem personalizado para modelos de difusão. Ele utiliza uma abordagem de preditor-corretor com configurações de ordem ajustáveis e parâmetros de equação diferencial estocástica (SDE) para gerar amostras a partir do modelo de entrada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo de difusão a ser utilizado para a amostragem |
| `eta` | FLOAT | Sim | 0.0 - 10.0 | Controla o fator de escala do tamanho do passo (padrão: 1.0) |
| `sde_start_percent` | FLOAT | Sim | 0.0 - 1.0 | A porcentagem inicial para a amostragem SDE (padrão: 0.2) |
| `sde_end_percent` | FLOAT | Sim | 0.0 - 1.0 | A porcentagem final para a amostragem SDE (padrão: 0.8) |
| `s_noise` | FLOAT | Sim | 0.0 - 100.0 | Controla a quantidade de ruído adicionada durante a amostragem (padrão: 1.0) |
| `predictor_order` | INT | Sim | 1 - 6 | A ordem do componente preditor no resolvedor (padrão: 3) |
| `corrector_order` | INT | Sim | 0 - 6 | A ordem do componente corretor no resolvedor (padrão: 4) |
| `use_pece` | BOOLEAN | Sim | - | Ativa ou desativa o método PECE (Predizer-Avaliar-Corrigir-Avaliar) |
| `simple_order_2` | BOOLEAN | Sim | - | Ativa ou desativa os cálculos simplificados de segunda ordem |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Um objeto amostrador configurado que pode ser usado com modelos de difusão |
