# PatchModelAddDownscale (Kohya Deep Shrink)

PatchModelAddDownscale (Kohya Deep Shrink) aplica a técnica Kohya Deep Shrink a um modelo, reduzindo as features intermediárias em um bloco escolhido e depois redimensionando-as de volta ao tamanho original. A redução ocorre apenas durante uma parte selecionada do processo de denoising, o que pode reduzir o custo de processamento mantendo o resultado final próximo do original.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo ao qual aplicar o patch de redução | MODEL | Sim | - |
| `número_do_bloco` | O número específico do bloco onde a redução será aplicada (padrão: 3) | INT | Sim | 1-32 |
| `fator_de_redução` | O fator pelo qual as features serão reduzidas (padrão: 2.0) | FLOAT | Sim | 0.1-9.0 |
| `percentual_inicial` | O ponto inicial do processo de denoising onde a redução começa (padrão: 0.0) | FLOAT | Sim | 0.0-1.0 |
| `percentual_final` | O ponto final do processo de denoising onde a redução para (padrão: 0.35) | FLOAT | Sim | 0.0-1.0 |
| `reduzir_após_pular` | Se a redução deve ser aplicada após as skip connections (padrão: True) | BOOLEAN | Sim | - |
| `método_de_redução` | O método de interpolação usado nas operações de redução (padrão: "bicubic") | COMBO | Sim | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |
| `método_de_ampliação` | O método de interpolação usado nas operações de ampliação (padrão: "bicubic") | COMBO | Sim | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" |

O patch de redução é aplicado somente quando o passo atual de denoising está dentro do intervalo definido por `start_percent` e `end_percent`, e apenas no bloco selecionado por `block_number`. Quando `downscale_after_skip` está habilitado, o patch é aplicado após a skip connection; quando desabilitado, é aplicado antes da skip connection. As features são redimensionadas de volta ao tamanho original em seguida, mas apenas quando o tamanho atual das features não corresponde mais ao tamanho registrado antes da redução.

Os parâmetros `block_number`, `start_percent`, `end_percent` e `downscale_after_skip` estão marcados como opções avançadas na interface do nó.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com o patch de redução aplicado | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/pt-BR.md)

---
**Source fingerprint (SHA-256):** `aa9434a521ab585b290a3bd8db804469bd3bb02103a0d830b6be6eb8e8c26a5e`
