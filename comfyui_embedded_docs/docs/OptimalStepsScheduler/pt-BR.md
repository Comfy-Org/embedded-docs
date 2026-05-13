> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/pt-BR.md)

O nó OptimalStepsScheduler calcula os sigmas do cronograma de ruído para modelos de difusão com base no tipo de modelo selecionado e na configuração de etapas. Ele ajusta o número total de etapas de acordo com o parâmetro de remoção de ruído (`denoise`) e interpola os níveis de ruído para corresponder à quantidade solicitada de etapas. O nó retorna uma sequência de valores sigma que determinam os níveis de ruído utilizados durante o processo de amostragem por difusão.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `tipo_de_modelo` | COMBO | Sim | "FLUX"<br>"Wan"<br>"Chroma" | O tipo de modelo de difusão a ser usado para o cálculo do nível de ruído |
| `passos` | INT | Sim | 3-1000 | O número total de etapas de amostragem a serem calculadas (padrão: 20) |
| `reduzir_ruído` | FLOAT | Não | 0.0-1.0 | Controla a intensidade da remoção de ruído, que ajusta o número efetivo de etapas (padrão: 1.0) |

**Observação:** Quando `denoise` é definido como um valor menor que 1.0, o nó calcula as etapas efetivas como `steps * denoise`. Se `denoise` for definido como 0.0, o nó retorna um tensor vazio.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `sigmas` | SIGMAS | Uma sequência de valores sigma que representa o cronograma de ruído para a amostragem por difusão |

---
**Source fingerprint (SHA-256):** `4379171dc6d525a1ece514fdd11a95bfd92ed0c8b301f69ca718c1a3256b9590`
