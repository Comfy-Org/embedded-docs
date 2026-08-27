# Agendador de Passos Ótimos

O nó `OptimalStepsScheduler` cria uma programação de ruído (uma sequência de valores sigma) para uso durante a amostragem por difusão. Ele seleciona os níveis de ruído base a partir do tipo de modelo escolhido, ajusta a programação quando a remoção de ruído é aplicada parcialmente e interpola os níveis para que os sigmas retornados correspondam à quantidade de passos solicitada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `tipo_de_modelo` | O tipo de modelo de difusão a ser usado para o cálculo do nível de ruído. | COMBO | Sim | "FLUX"<br>"Wan"<br>"Chroma" |
| `passos` | O número total de passos de amostragem a serem calculados (padrão: 20). | INT | Sim | 3 a 1000 |
| `reduzir_ruído` | Controla a intensidade da remoção de ruído, o que ajusta o número efetivo de passos (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |

**Observação:** Quando `denoise` é menor que 1.0, o nó usa `round(steps * denoise)` como o número total de passos efetivos. Se `denoise` for 0.0, o nó retorna um tensor vazio.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sigmas` | Uma sequência de valores sigma que representa a programação de ruído para a amostragem por difusão. | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fd48c94ca16c8a3d8e6f0138018e7b13c15d100d6147807bcb23d838899045b7`
