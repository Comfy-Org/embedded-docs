# Agendador de Passos Ótimos

O nó OptimalStepsScheduler calcula os sigmas do agendamento de ruído para modelos de difusão com base no tipo de modelo selecionado e na configuração de passos. Ele ajusta o número total de passos de acordo com o parâmetro `denoise` e interpola os níveis de ruído para corresponder à contagem de passos solicitada. O nó retorna uma sequência de valores sigma que determinam os níveis de ruído usados durante o processo de amostragem por difusão.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model_type` | O tipo de modelo de difusão a ser usado para o cálculo do nível de ruído | COMBO | Sim | "FLUX"<br>"Wan"<br>"Chroma" |
| `steps` | O número total de passos de amostragem a serem calculados (padrão: 20) | INT | Sim | 3-1000 |
| `denoise` | Controla a força de remoção de ruído, que ajusta o número efetivo de passos (padrão: 1.0) | FLOAT | Sim | 0.0-1.0 |

**Observação:** Quando `denoise` é definido como menor que 1.0, o nó calcula os passos efetivos como `steps * denoise`. Se `denoise` for definido como 0.0, o nó retorna um tensor vazio.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sigmas` | Uma sequência de valores sigma que representa o agendamento de ruído para a amostragem por difusão | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fd48c94ca16c8a3d8e6f0138018e7b13c15d100d6147807bcb23d838899045b7`
