# Flux2Scheduler

O nó Flux2Scheduler gera uma sequência de níveis de ruído (sigmas) para o processo de remoção de ruído, especificamente adaptada para o modelo Flux2. Ele calcula um agendamento com base no número de etapas de remoção de ruído e nas dimensões da imagem alvo, o que influencia a progressão da remoção de ruído durante a geração de imagens.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `steps` | O número de etapas de remoção de ruído a serem executadas. Um valor maior normalmente leva a resultados mais detalhados, mas leva mais tempo para processar (padrão: 20). | INT | Sim | 1 a 4096 |
| `width` | A largura da imagem a ser gerada, em pixels. Esse valor influencia o cálculo do agendamento de ruído (padrão: 1024). | INT | Sim | 16 a 16384 (MAX_RESOLUTION) |
| `height` | A altura da imagem a ser gerada, em pixels. Esse valor influencia o cálculo do agendamento de ruído (padrão: 1024). | INT | Sim | 16 a 16384 (MAX_RESOLUTION) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sigmas` | Uma sequência de valores de níveis de ruído (sigmas) que define o agendamento de remoção de ruído para o amostrador. A saída contém um valor a mais do que o número de etapas (`steps + 1`). | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9606177f37f7bc03aef524623f03b7f24bcdc3d9327dcdf74863fe2befeb2b65`
