# EasyCache

O nó EasyCache adiciona um sistema de cache nativo a um modelo de difusão que acelera a amostragem ao reutilizar resultados de etapas calculadas anteriormente em vez de recalcular cada etapa. Ele é ativado apenas entre um ponto inicial e final configurável do processo de amostragem, e pula etapas quando a mudança estimada na saída permanece abaixo de um limite definido pelo usuário. Este é um nó experimental destinado ao uso avançado de depuração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo ao qual adicionar EasyCache. | MODEL | Sim | - |
| `limite_de_reutilização` | O limiar para reutilizar etapas em cache (padrão: 0.2). | FLOAT | Sim | 0.0 - 3.0 |
| `percentual_inicial` | A etapa relativa de amostragem para iniciar o uso do EasyCache (padrão: 0.15). | FLOAT | Sim | 0.0 - 1.0 |
| `percentual_final` | A etapa relativa de amostragem para encerrar o uso do EasyCache (padrão: 0.95). | FLOAT | Sim | 0.0 - 1.0 |
| `detalhado` | Se deve registrar informações detalhadas (padrão: False). | BOOLEAN | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo com a funcionalidade EasyCache adicionada. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3e10ac65f8df58ce8649fdf599e62bfb86f2d4166840bed5622c0aa2c419cd38`
