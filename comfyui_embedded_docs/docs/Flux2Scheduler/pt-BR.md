# Flux2Scheduler

O Flux2Scheduler gera uma sequência de níveis de ruído (sigmas) para o processo de remoção de ruído (denoising), especificamente adaptada para o modelo Flux. Ele calcula um agendamento com base no número de etapas de remoção de ruído e nas dimensões da imagem alvo, o que influencia a progressão da remoção de ruído durante a geração da imagem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `etapas` | O número de etapas de remoção de ruído a serem executadas. Um valor maior geralmente leva a resultados mais detalhados, mas demora mais para processar (padrão: 20). | INT | Sim | 1 a 4096 |
| `largura` | A largura da imagem a ser gerada, em pixels. Este valor influencia o cálculo do agendamento de ruído (padrão: 1024). | INT | Sim | 16 a 16384 |
| `altura` | A altura da imagem a ser gerada, em pixels. Este valor influencia o cálculo do agendamento de ruído (padrão: 1024). | INT | Sim | 16 a 16384 |

Nota: O agendamento é calculado a partir do comprimento da sequência de imagem, que é derivado de `width` e `height` como `(width * height) / 256`, refletindo o downsampling latente de 16x do modelo. Imagens maiores produzem sequências mais longas, o que desloca o agendamento de ruído de forma correspondente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sigmas` | Uma sequência de valores de níveis de ruído (sigmas) que definem o agendamento de remoção de ruído para o amostrador. | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9606177f37f7bc03aef524623f03b7f24bcdc3d9327dcdf74863fe2befeb2b65`
