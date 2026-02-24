> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/pt-BR.md)

O nó PatchModelAddDownscale implementa a funcionalidade Kohya Deep Shrink aplicando operações de redução e aumento de escala a blocos específicos de um modelo. Ele reduz a resolução dos recursos intermediários durante o processamento e depois os restaura ao tamanho original, o que pode melhorar o desempenho mantendo a qualidade. O nó permite um controle preciso sobre quando e como essas operações de escala ocorrem durante a execução do modelo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo ao qual o patch de redução de escala será aplicado |
| `block_number` | INT | Não | 1-32 | O número específico do bloco onde a redução de escala será aplicada (padrão: 3) |
| `downscale_factor` | FLOAT | Não | 0.1-9.0 | O fator pelo qual os recursos serão reduzidos em escala (padrão: 2.0) |
| `start_percent` | FLOAT | Não | 0.0-1.0 | O ponto de partida no processo de remoção de ruído onde a redução de escala começa (padrão: 0.0) |
| `end_percent` | FLOAT | Não | 0.0-1.0 | O ponto final no processo de remoção de ruído onde a redução de escala para (padrão: 0.35) |
| `downscale_after_skip` | BOOLEAN | Não | - | Se deve aplicar a redução de escala após as conexões de salto (padrão: Verdadeiro) |
| `downscale_method` | COMBO | Não | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | O método de interpolação usado para as operações de redução de escala |
| `upscale_method` | COMBO | Não | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | O método de interpolação usado para as operações de aumento de escala |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo modificado com o patch de redução de escala aplicado |
