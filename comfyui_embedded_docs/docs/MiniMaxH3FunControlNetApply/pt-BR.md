# MiniMaxH3FunControlNetApply

Este nó aplica um MiniMax H3 Fun ControlNet a um modelo de texto para vídeo como um patch de modelo. Ele pode usar um vídeo de controle opcional e uma máscara opcional para direcionar a geração e retorna uma cópia do modelo com o patch aplicado para amostragem posterior. Quando a força está definida como 0, ou quando nenhum vídeo de controle ou máscara é fornecido, o modelo de entrada é retornado inalterado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-------------|-------------|-----------|
| `model` | O modelo de difusão ao qual o patch MiniMax H3 Fun ControlNet é aplicado. | MODEL | Sim | N/A |
| `model_patch` | O patch MiniMax H3 Fun ControlNet cujos sinais de controle são injetados no modelo; ele deve ser compatível com o `model` fornecido. | MODEL_PATCH | Sim | N/A |
| `vae` | VAE usado para codificar os quadros do vídeo de controle e de origem no espaço latente esperado pelo modelo. | VAE | Sim | N/A |
| `strength` | Força geral do efeito ControlNet. Quando definida como 0, o nó não faz nada e retorna o modelo de entrada inalterado. (padrão: 1.0) | FLOAT | Sim | min 0.0, max 10.0, step 0.01 |
| `start_percent` | Início do intervalo de amostragem, expresso como uma porcentagem do cronograma de amostragem, durante o qual o ControlNet está ativo. Ele é convertido internamente para o valor sigma equivalente. (padrão: 0.0) | FLOAT | Sim | min 0.0, max 1.0, step 0.001 |
| `end_percent` | Fim do intervalo de amostragem, expresso como uma porcentagem do cronograma de amostragem, durante o qual o ControlNet está ativo. Ele é convertido internamente para o valor sigma equivalente. (padrão: 1.0) | FLOAT | Sim | min 0.0, max 1.0, step 0.001 |
| `control_video` | Quadros de vídeo opcionais usados como dica visual do ControlNet. Os quadros são redimensionados para corresponder ao vídeo gerado e codificados com o `vae`. | IMAGE | Não | N/A |
| `mask` | 1 marca as regiões a serem regeneradas. Valores de máscara acima de 0.5 são tratados como regiões marcadas. | MASK | Não | N/A |
| `source_video` | Vídeo atrás da máscara; somente lido quando uma máscara é fornecida. | IMAGE | Não | N/A |

Nota: Para que o patch tenha efeito, `strength` deve ser maior que 0 e pelo menos um de `control_video` ou `mask` deve ser fornecido. `source_video` é ignorado a menos que `mask` seja fornecida; se `mask` for fornecida sem `source_video`, o conteúdo atrás das regiões mascaradas é tratado como preto.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-------------|
| `model` | Um clone do modelo de entrada com o patch MiniMax H3 Fun ControlNet aplicado. Se `strength` for 0, ou se nenhum vídeo de controle ou máscara for fornecido, o modelo original é retornado inalterado. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3FunControlNetApply/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e907fb8e5ae60663d1d10b315985695ee5d49397fef6bd76b0e723637457a74a`
