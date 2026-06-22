# CondicionamentoDefinirÁreaPercentualVídeo

O nó ConditioningSetAreaPercentageVideo modifica os dados de condicionamento definindo uma área específica e uma região temporal para a geração de vídeo. Ele permite definir a posição, o tamanho e a duração da área onde o condicionamento será aplicado, usando valores percentuais relativos às dimensões gerais. Isso é útil para focar a geração em partes específicas de uma sequência de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Tipo de Entrada | Padrão | Faixa |
| --- | --- | --- | --- | --- | --- |
| `condicionamento` | Os dados de condicionamento a serem modificados | CONDITIONING | Obrigatório | - | - |
| `largura` | A largura da área como uma porcentagem da largura total | FLOAT | Obrigatório | 1.0 | 0.0 - 1.0 |
| `altura` | A altura da área como uma porcentagem da altura total | FLOAT | Obrigatório | 1.0 | 0.0 - 1.0 |
| `temporal` | A duração temporal da área como uma porcentagem da duração total do vídeo | FLOAT | Obrigatório | 1.0 | 0.0 - 1.0 |
| `x` | A posição inicial horizontal da área como uma porcentagem | FLOAT | Obrigatório | 0.0 | 0.0 - 1.0 |
| `y` | A posição inicial vertical da área como uma porcentagem | FLOAT | Obrigatório | 0.0 | 0.0 - 1.0 |
| `z` | A posição inicial temporal da área como uma porcentagem da linha do tempo do vídeo | FLOAT | Obrigatório | 0.0 | 0.0 - 1.0 |
| `força` | O multiplicador de intensidade aplicado ao condicionamento dentro da área definida | FLOAT | Obrigatório | 1.0 | 0.0 - 10.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `condicionamento` | Os dados de condicionamento modificados com a área e as configurações de intensidade especificadas aplicadas | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `72d4bef4f8ddc4765cf69863f7ad03d34992f0ff30a963dbe2dc1b7d69815410`
