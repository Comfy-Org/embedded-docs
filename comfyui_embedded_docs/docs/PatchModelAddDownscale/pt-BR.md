# PatchModelAddDownscale (Kohya Deep Shrink)

O nó PatchModelAddDownscale implementa a funcionalidade Kohya Deep Shrink aplicando operações de redução e aumento de escala a blocos específicos de um modelo. Ele reduz a resolução das características intermediárias durante o processamento e depois as restaura ao tamanho original, o que pode melhorar o desempenho mantendo a qualidade. O nó permite controle preciso sobre quando e como essas operações de escalonamento ocorrem durante a execução do modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo no qual aplicar o patch de redução de escala | MODEL | Sim | - |
| `block_number` | O número do bloco específico em que a redução de escala será aplicada (padrão: 3) | INT | Não | 1-32 |
| `downscale_factor` | O fator pelo qual as características são reduzidas em escala (padrão: 2.0) | FLOAT | Não | 0.1-9.0 |
| `start_percent` | O ponto inicial no processo de remoção de ruído em que a redução de escala começa (padrão: 0.0) | FLOAT | Não | 0.0-1.0 |
| `end_percent` | O ponto final no processo de remoção de ruído em que a redução de escala para (padrão: 0.35) | FLOAT | Não | 0.0-1.0 |
| `downscale_after_skip` | Se a redução de escala deve ser aplicada após conexões de salto (padrão: True) | BOOLEAN | Não | - |
| `downscale_method` | O método de interpolação usado para operações de redução de escala | COMBO | Não | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `upscale_method` | O método de interpolação usado para operações de aumento de escala | COMBO | Não | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com o patch de redução de escala aplicado | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/pt-BR.md)

---
**Source fingerprint (SHA-256):** `aa9434a521ab585b290a3bd8db804469bd3bb02103a0d830b6be6eb8e8c26a5e`
