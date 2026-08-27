# LTXV Modality Guidance (acoplamento A/V)

Este nó aplica orientação entre modalidades (áudio-vídeo) a um modelo LTXV-AV. Durante a amostragem, ele executa uma passagem direta extra por etapa com as conexões de atenção cruzada de áudio para vídeo e de vídeo para áudio desativadas. Em seguida, desloca o resultado em direção à previsão acoplada para reforçar a sincronização audiovisual, como a sincronização labial. O padrão de referência para `modality_scale` é 3.0; defini-lo como 1.0 desativa a passagem extra, e essa orientação pode ser combinada com o orientador dual-CFG e o STG.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo base ao qual a orientação de modalidade será aplicada. Ele é clonado internamente, deixando o modelo original inalterado. | MODEL | Sim | - |
| `modality_scale` | Intensidade da orientação de acoplamento áudio-vídeo. O padrão é 3.0. Defina como 1.0 para desativar a passagem direta extra. | FLOAT | Sim | 1.0 a 100.0 (padrão: 3.0) |
| `start_percent` | O ponto no processo de amostragem, como uma proporção de 0.0 a 1.0, em que a orientação de modalidade começa. Este é um parâmetro avançado. O padrão é 0.0. | FLOAT | Sim | 0.0 a 1.0 (padrão: 0.0) |
| `end_percent` | O ponto no processo de amostragem, como uma proporção de 0.0 a 1.0, em que a orientação de modalidade termina. Este é um parâmetro avançado. O padrão é 1.0. | FLOAT | Sim | 0.0 a 1.0 (padrão: 1.0) |

A orientação é aplicada somente nas etapas de amostragem cujos valores de sigma estejam dentro do intervalo definido por `start_percent` e `end_percent`. Fora desse intervalo, o nó retorna o resultado limpo inalterado. Um `modality_scale` de 1.0 também desativa completamente a passagem direta extra.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model` | O modelo clonado com uma função de orientação pós-CFG anexada. Este modelo modificado aplica a orientação de modalidade durante a amostragem. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVModalityGuidance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `038be607c42e626a8a8f5fe336ee466d0847d43835edb71e20ff38f668069cfb`
