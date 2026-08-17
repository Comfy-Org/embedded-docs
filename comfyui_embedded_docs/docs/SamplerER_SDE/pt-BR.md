# SamplerER_SDE

O nó SamplerER_SDE fornece métodos de amostragem especializados para modelos de difusão, oferecendo três tipos de solver: ER-SDE, Reverse-time SDE e ODE. Ele permite controle sobre o comportamento estocástico e o número de estágios computacionais do processo de amostragem. O nó ajusta automaticamente as configurações de ruído quando o solver ODE ou uma configuração determinística (`eta`=0) é selecionada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `solver_type` | O tipo de solver a ser usado para amostragem. Determina o comportamento de escala de ruído do processo de difusão (padrão: "ER-SDE"). | COMBO | Sim | "ER-SDE"<br>"Reverse-time SDE"<br>"ODE" |
| `max_stage` | O número máximo de estágios para o processo de amostragem (padrão: 3). Controla a complexidade computacional e a qualidade. Parâmetro avançado. | INT | Sim | 1-3 |
| `eta` | Força estocástica das SDEs.<br>Quando eta=0, elas se reduzem a ODE determinística.<br>Valores grandes de eta podem causar saídas inválidas. Se isso ocorrer, tente diminuir esse valor. (padrão: 1.0). Parâmetro avançado. | FLOAT | Sim | 0.0-10.0 |
| `s_noise` | Fator de escala de ruído para o processo de amostragem (padrão: 1.0). Controla a quantidade de ruído aplicado durante a amostragem. Parâmetro avançado. | FLOAT | Sim | 0.0-100.0 |

**Restrições dos Parâmetros:**

- Quando `solver_type` é "ODE" ou `eta` é 0, o nó força `s_noise` para 0.0 e alterna o solver para "ODE".
- `eta` afeta os tipos de solver "ER-SDE" e "Reverse-time SDE". Valores grandes podem causar saídas inválidas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `sampler` | Um objeto sampler configurado que pode ser usado no pipeline de amostragem com as configurações de solver especificadas. | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5299ae9b45444cdc7c36bcb3c5e5a0600f9f904e57ae614554033434afdffd30`
