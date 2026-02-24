> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/pt-BR.md)

Este nó fornece um amostrador configurável para gerar imagens. Ele implementa o algoritmo SEEDS-2, que é um resolvedor de equações diferenciais estocásticas (SDE). Ao ajustar seus parâmetros, você pode configurá-lo para se comportar como vários amostradores específicos, incluindo `seeds_2`, `exp_heun_2_x0` e `exp_heun_2_x0_sde`.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `solver_type` | COMBO | Sim | `"phi_1"`<br>`"phi_2"` | Seleciona o algoritmo resolvedor subjacente para o amostrador. |
| `eta` | FLOAT | Não | 0.0 - 100.0 | Força estocástica (padrão: 1.0). |
| `s_noise` | FLOAT | Não | 0.0 - 100.0 | Multiplicador de ruído SDE (padrão: 1.0). |
| `r` | FLOAT | Não | 0.01 - 1.0 | Tamanho relativo do passo para o estágio intermediário (nó c2) (padrão: 0.5). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | Um objeto amostrador configurado que pode ser passado para outros nós de amostragem. |
