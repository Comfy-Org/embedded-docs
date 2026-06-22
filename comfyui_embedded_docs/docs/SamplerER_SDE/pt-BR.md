# SamplerER_SDE

O nó SamplerER_SDE fornece métodos de amostragem especializados para modelos de difusão, oferecendo diferentes tipos de solucionadores, incluindo ER-SDE, SDE de tempo reverso e abordagens ODE. Ele permite controle sobre o comportamento estocástico e os estágios computacionais do processo de amostragem. O nó ajusta automaticamente os parâmetros com base no tipo de solucionador selecionado para garantir o funcionamento adequado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `solver_type` | O tipo de solucionador a ser usado para amostragem. Determina a abordagem matemática para o processo de difusão. | COMBO | Sim | "ER-SDE"<br>"SDE de tempo reverso"<br>"ODE" |
| `max_stage` | O número máximo de estágios para o processo de amostragem (padrão: 3). Controla a complexidade computacional e a qualidade. | INT | Não | 1-3 |
| `eta` | Força estocástica do SDE de tempo reverso (padrão: 1,0). Quando eta=0, reduz-se a ODE determinística. Esta configuração não se aplica ao tipo de solucionador ER-SDE. | FLOAT | Não | 0,0-100,0 |
| `s_noise` | Fator de escala de ruído para o processo de amostragem (padrão: 1,0). Controla a quantidade de ruído aplicada durante a amostragem. | FLOAT | Não | 0,0-100,0 |

**Restrições dos Parâmetros:**

- Quando `solver_type` está definido como "ODE" ou ao usar "SDE de tempo reverso" com `eta`=0, tanto `eta` quanto `s_noise` são automaticamente definidos como 0, independentemente dos valores inseridos pelo usuário.
- O parâmetro `eta` afeta apenas o tipo de solucionador "SDE de tempo reverso" e não tem efeito sobre o tipo de solucionador "ER-SDE".

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sampler` | Um objeto de amostragem configurado que pode ser usado no pipeline de amostragem com as configurações de solucionador especificadas. | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bc24ec3c5dc645aebf55ef3392c5f4a40dcf0461b4b77731e8fe7ff397dcfadf`
