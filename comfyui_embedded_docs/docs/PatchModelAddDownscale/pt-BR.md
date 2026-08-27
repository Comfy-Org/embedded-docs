# PatchModelAddDownscale (Kohya Deep Shrink)

PatchModelAddDownscale (Kohya Deep Shrink) implementa a técnica Kohya Deep Shrink aplicando operações de redução e aumento de escala em blocos específicos de um modelo. Ela reduz a resolução das características intermediárias durante o processamento e depois as restaura ao tamanho original, o que pode melhorar o desempenho mantendo a qualidade. O nó permite controle preciso sobre quando e como essas operações de escala ocorrem durante a execução do modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo ao qual o patch de redução de escala será aplicado | MODEL | Sim | - |
| `número_do_bloco` | O número específico do bloco onde a redução de escala será aplicada (padrão: 3) | INT | Sim | 1-32 |
| `fator_de_redução` | O fator pelo qual as características serão reduzidas em escala (padrão: 2.0) | FLOAT | Sim | 0.1-9.0 |
| `percentual_inicial` | O ponto inicial no processo de denoising onde a redução de escala começa (padrão: 0.0) | FLOAT | Sim | 0.0-1.0 |
| `percentual_final` | O ponto final no processo de denoising onde a redução de escala termina (padrão: 0.35) | FLOAT | Sim | 0.0-1.0 |
| `reduzir_após_pular` | Se deve aplicar a redução de escala após as conexões de skip (padrão: True) | BOOLEAN | Sim | - |
| `método_de_redução` | O método de interpolação usado para operações de redução de escala | COMBO | Sim | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `método_de_ampliação` | O método de interpolação usado para operações de aumento de escala | COMBO | Sim | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

O patch de redução de escala é aplicado apenas quando a etapa atual de denoising está dentro do intervalo definido por `start_percent` e `end_percent`, e somente no bloco selecionado por `block_number`. Quando `downscale_after_skip` está habilitado, o patch é aplicado após a conexão de skip; quando desabilitado, é aplicado antes da conexão de skip.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com o patch de redução de escala aplicado | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/pt-BR.md)

---
**Source fingerprint (SHA-256):** `aa9434a521ab585b290a3bd8db804469bd3bb02103a0d830b6be6eb8e8c26a5e`
