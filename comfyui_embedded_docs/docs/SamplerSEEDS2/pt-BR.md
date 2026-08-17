# SamplerSEEDS2

Este nó fornece um amostrador configurável para gerar imagens. Ele implementa o algoritmo SEEDS-2, que é um solucionador de equações diferenciais estocásticas (SDE). Ao ajustar seus parâmetros, você pode configurá-lo para se comportar como vários amostradores específicos, incluindo `seeds_2`, `exp_heun_2_x0` e `exp_heun_2_x0_sde`.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `solver_type` | Seleciona o algoritmo de solucionador subjacente para o amostrador. | COMBO | Sim | `"phi_1"`<br>`"phi_2"` |
| `eta` | Intensidade estocástica (padrão: 1.0). | FLOAT | Não | 0.0 - 100.0 |
| `s_noise` | Multiplicador de ruído SDE (padrão: 1.0). | FLOAT | Não | 0.0 - 100.0 |
| `r` | Tamanho relativo do passo para o estágio intermediário (nó c2) (padrão: 0.5). | FLOAT | Não | 0.01 - 1.0 |

Dependendo das configurações de parâmetros, este amostrador pode representar:

- `seeds_2` — configurações padrão
- `exp_heun_2_x0` — `solver_type`=`phi_2`, `r`=1.0, `eta`=0.0
- `exp_heun_2_x0_sde` — `solver_type`=`phi_2`, `r`=1.0, `eta`=1.0, `s_noise`=1.0

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sampler` | Um objeto de amostrador configurado que pode ser passado a outros nós de amostragem. | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f48744a706a49ef93d41845bf8c308af971853f6150afd00ded45f0317ffc4f9`
