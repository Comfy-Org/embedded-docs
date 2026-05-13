> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/pt-BR.md)

O nó ConditioningSetAreaPercentageVideo modifica os dados de condicionamento definindo uma área específica e uma região temporal para a geração de vídeo. Ele permite definir a posição, o tamanho e a duração da área onde o condicionamento será aplicado, usando valores percentuais relativos às dimensões gerais. Isso é útil para focar a geração em partes específicas de uma sequência de vídeo.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Faixa | Descrição |
|-----------|---------------|-----------------|--------|-------|-------------|
| `condicionamento` | CONDITIONING | Obrigatório | - | - | Os dados de condicionamento a serem modificados |
| `largura` | FLOAT | Obrigatório | 1.0 | 0.0 - 1.0 | A largura da área como uma porcentagem da largura total |
| `altura` | FLOAT | Obrigatório | 1.0 | 0.0 - 1.0 | A altura da área como uma porcentagem da altura total |
| `temporal` | FLOAT | Obrigatório | 1.0 | 0.0 - 1.0 | A duração temporal da área como uma porcentagem da duração total do vídeo |
| `x` | FLOAT | Obrigatório | 0.0 | 0.0 - 1.0 | A posição inicial horizontal da área como uma porcentagem |
| `y` | FLOAT | Obrigatório | 0.0 | 0.0 - 1.0 | A posição inicial vertical da área como uma porcentagem |
| `z` | FLOAT | Obrigatório | 0.0 | 0.0 - 1.0 | A posição inicial temporal da área como uma porcentagem da linha do tempo do vídeo |
| `força` | FLOAT | Obrigatório | 1.0 | 0.0 - 10.0 | O multiplicador de intensidade aplicado ao condicionamento dentro da área definida |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `condicionamento` | CONDITIONING | Os dados de condicionamento modificados com a área e as configurações de intensidade especificadas aplicadas |

---
**Source fingerprint (SHA-256):** `72d4bef4f8ddc4765cf69863f7ad03d34992f0ff30a963dbe2dc1b7d69815410`
