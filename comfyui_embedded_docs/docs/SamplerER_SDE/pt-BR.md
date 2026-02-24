> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/pt-BR.md)

O nó SamplerER_SDE fornece métodos de amostragem especializados para modelos de difusão, oferecendo diferentes tipos de solucionadores, incluindo abordagens ER-SDE, SDE de tempo reverso e ODE. Ele permite o controle sobre o comportamento estocástico e os estágios computacionais do processo de amostragem. O nó ajusta automaticamente os parâmetros com base no tipo de solucionador selecionado para garantir o funcionamento adequado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `solver_type` | COMBO | Sim | "ER-SDE"<br>"Reverse-time SDE"<br>"ODE" | O tipo de solucionador a ser usado para a amostragem. Determina a abordagem matemática para o processo de difusão. |
| `max_stage` | INT | Sim | 1-3 | O número máximo de estágios para o processo de amostragem (padrão: 3). Controla a complexidade computacional e a qualidade. |
| `eta` | FLOAT | Sim | 0.0-100.0 | Força estocástica do SDE de tempo reverso (padrão: 1.0). Quando eta=0, ele se reduz a um ODE determinístico. Esta configuração não se aplica ao tipo de solucionador ER-SDE. |
| `s_noise` | FLOAT | Sim | 0.0-100.0 | Fator de escala de ruído para o processo de amostragem (padrão: 1.0). Controla a quantidade de ruído aplicada durante a amostragem. |

**Restrições dos Parâmetros:**

- Quando `solver_type` está definido como "ODE" ou quando se usa "Reverse-time SDE" com `eta`=0, tanto `eta` quanto `s_noise` são automaticamente definidos como 0, independentemente dos valores inseridos pelo usuário.
- O parâmetro `eta` afeta apenas o tipo de solucionador "Reverse-time SDE" e não tem efeito no tipo de solucionador "ER-SDE".

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Um objeto amostrador configurado que pode ser usado no pipeline de amostragem com as configurações de solucionador especificadas. |
