Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/en.md)

Este nó fornece um amostrador configurável para gerar imagens. Ele implementa o algoritmo SEEDS-2, que é um solucionador de equação diferencial estocástica (SDE). Ao ajustar seus parâmetros, você pode configurá-lo para se comportar como vários amostradores específicos, incluindo `seeds_2`, `exp_heun_2_x0` e `exp_heun_2_x0_sde`.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `solver_type` | Seleciona o algoritmo solucionador subjacente para o amostrador. | COMBO | Sim | `"phi_1"`<br>`"phi_2"` |
| `eta` | Força estocástica (padrão: 1.0). | FLOAT | Não | 0.0 - 100.0 |
| `s_noise` | Multiplicador de ruído SDE (padrão: 1.0). | FLOAT | Não | 0.0 - 100.0 |
| `r` | Tamanho relativo do passo para o estágio intermediário (nó c2) (padrão: 0.5). | FLOAT | Não | 0.01 - 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sampler` | Um objeto amostrador configurado que pode ser passado para outros nós de amostragem. | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `13cfc064dab8b77dbdfdc27238130bdf3dc6c1eca47110f4a7f7d6b8c2866b90`
