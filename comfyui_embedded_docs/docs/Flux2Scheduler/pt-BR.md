# Flux2Scheduler

O nó Flux2Scheduler gera uma sequência de níveis de ruído (sigmas) para o processo de remoção de ruído, especificamente adaptada para o modelo Flux. Ele calcula um cronograma com base no número de etapas de remoção de ruído e nas dimensões da imagem alvo, o que influencia a progressão da remoção de ruído durante a geração de imagens.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `etapas` | O número de etapas de remoção de ruído a serem executadas. Um valor maior geralmente resulta em resultados mais detalhados, mas leva mais tempo para processar (padrão: 20). | INT | Sim | 1 a 4096 |
| `largura` | A largura da imagem a ser gerada, em pixels. Este valor influencia o cálculo do cronograma de ruído (padrão: 1024). | INT | Sim | 16 a 16384 |
| `altura` | A altura da imagem a ser gerada, em pixels. Este valor influencia o cálculo do cronograma de ruído (padrão: 1024). | INT | Sim | 16 a 16384 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sigmas` | Uma sequência de valores de nível de ruído (sigmas) que definem o cronograma de remoção de ruído para o amostrador. | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dbe44a6eb454dd61ab22df5770ad5ac559e03b20fd36d17d33730cdb835f7ede`
