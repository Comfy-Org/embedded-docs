# SamplerER_SDE

O nó SamplerER_SDE fornece métodos de amostragem especializados para modelos de difusão, oferecendo diferentes tipos de solvers: ER-SDE, Reverse-time SDE e ODE. Ele permite controlar o comportamento estocástico e o número de estágios computacionais do processo de amostragem. O nó ajusta automaticamente as configurações com base no tipo de solver escolhido para manter o sampler funcionando corretamente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `solver_type` | O tipo de solver a ser usado na amostragem. Determina a abordagem matemática para o processo de difusão (padrão: "ER-SDE"). | COMBO | Sim | "ER-SDE"<br>"Reverse-time SDE"<br>"ODE" |
| `max_stage` | O número máximo de estágios para o processo de amostragem (padrão: 3). Controla a complexidade computacional e a qualidade. | INT | Sim | 1-3 |
| `eta` | Intensidade estocástica das SDEs.<br>Quando eta=0, elas se reduzem à ODE determinística.<br>Valores grandes de eta podem causar saídas inválidas. Se isso ocorrer, tente diminuir esse valor. (padrão: 1.0) | FLOAT | Sim | 0.0-10.0 (passo: 0.01) |
| `s_noise` | Fator de escalonamento de ruído para o processo de amostragem (padrão: 1.0). Controla a quantidade de ruído aplicada durante a amostragem. | FLOAT | Sim | 0.0-100.0 (passo: 0.01) |

**Restrições dos Parâmetros:**

- Quando `solver_type` está definido como "ODE" ou quando `eta` é 0, o nó muda para o modo ODE e define `s_noise` como 0.0, independentemente do valor inserido para `s_noise`.
- O parâmetro `eta` controla a intensidade estocástica dos tipos de solver "ER-SDE" e "Reverse-time SDE". Ele não tem efeito quando o solver opera no modo ODE.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sampler` | Um objeto sampler configurado que pode ser usado no pipeline de amostragem com as configurações de solver especificadas. | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5299ae9b45444cdc7c36bcb3c5e5a0600f9f904e57ae614554033434afdffd30`
