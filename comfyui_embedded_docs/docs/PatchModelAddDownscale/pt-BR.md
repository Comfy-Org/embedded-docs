> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatchModelAddDownscale/pt-BR.md)

O nó PatchModelAddDownscale implementa a funcionalidade Kohya Deep Shrink ao aplicar operações de redução e ampliação de escala em blocos específicos de um modelo. Ele reduz a resolução de características intermediárias durante o processamento e, em seguida, as restaura ao tamanho original, o que pode melhorar o desempenho enquanto mantém a qualidade. O nó permite controle preciso sobre quando e como essas operações de escala ocorrem durante a execução do modelo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `modelo` | MODEL | Sim | - | O modelo no qual aplicar o patch de redução de escala |
| `número_do_bloco` | INT | Não | 1-32 | O número do bloco específico onde a redução de escala será aplicada (padrão: 3) |
| `fator_de_redução` | FLOAT | Não | 0.1-9.0 | O fator pelo qual reduzir a escala das características (padrão: 2.0) |
| `percentual_inicial` | FLOAT | Não | 0.0-1.0 | O ponto inicial no processo de remoção de ruído onde a redução de escala começa (padrão: 0.0) |
| `percentual_final` | FLOAT | Não | 0.0-1.0 | O ponto final no processo de remoção de ruído onde a redução de escala para (padrão: 0.35) |
| `reduzir_após_pular` | BOOLEAN | Não | - | Se deve aplicar a redução de escala após as conexões de atalho (padrão: True) |
| `método_de_redução` | COMBO | Não | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | O método de interpolação usado para operações de redução de escala |
| `método_de_ampliação` | COMBO | Não | "bicubic"<br>"nearest-exact"<br>"bilinear"<br>"area"<br>"bislerp" | O método de interpolação usado para operações de ampliação de escala |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `modelo` | MODEL | O modelo modificado com o patch de redução de escala aplicado |

---
**Source fingerprint (SHA-256):** `93ece77ad2dce3c1cdd554583ae1f2e6be51a43ab072d408869dddbcc7798c40`
