# CondicionamentoDefinirÁreaPercentualVídeo

O nó ConditioningSetAreaPercentageVideo modifica os dados de condicionamento ao definir uma área específica e uma região temporal para a geração de vídeo. Ele usa valores percentuais relativos às dimensões gerais para definir a posição, o tamanho e a duração da área onde o condicionamento é aplicado. Isso é útil para focar a geração em partes específicas de uma sequência de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `condicionamento` | Os dados de condicionamento a serem modificados | CONDITIONING | Sim | - |
| `largura` | A largura da área como porcentagem da largura total (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step 0.01) |
| `altura` | A altura da área como porcentagem da altura total (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step 0.01) |
| `temporal` | A duração temporal da área como porcentagem da duração total do vídeo (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step 0.01) |
| `x` | A posição inicial horizontal da área como porcentagem (padrão: 0.0) | FLOAT | Sim | 0.0 - 1.0 (step 0.01) |
| `y` | A posição inicial vertical da área como porcentagem (padrão: 0.0) | FLOAT | Sim | 0.0 - 1.0 (step 0.01) |
| `z` | A posição inicial temporal da área como porcentagem da linha do tempo do vídeo (padrão: 0.0) | FLOAT | Sim | 0.0 - 1.0 (step 0.01) |
| `força` | O multiplicador de intensidade aplicado ao condicionamento dentro da área definida (padrão: 1.0) | FLOAT | Sim | 0.0 - 10.0 (step 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `conditioning` | Os dados de condicionamento modificados com a área especificada e as configurações de intensidade aplicadas | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9c5ddae6a2b1da5907fb52ef625eefb12b0b228fd3bd52c3033b5c4226d76150`
