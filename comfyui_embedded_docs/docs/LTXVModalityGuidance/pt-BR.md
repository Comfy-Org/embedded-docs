# LTXVModalityGuidance

Este nó aplica orientação cross-modal (áudio-vídeo) a um modelo LTXV-AV. Durante a amostragem, ele executa uma passagem direta extra por etapa com as conexões de atenção cruzada áudio-para-vídeo e vídeo-para-áudio desativadas e, em seguida, aproxima o resultado da predição acoplada. Isso fortalece a sincronização audiovisual, como a sincronização labial. O valor de referência padrão para `modality_scale` é 3.0; defini-lo como 1.0 desativa a passagem extra.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo base ao qual a orientação de modalidade será aplicada. Ele é clonado internamente, deixando o modelo original inalterado. | MODEL | Sim | - |
| `modality_scale` | Intensidade da orientação de acoplamento áudio-vídeo. O padrão é 3.0. Defina como 1.0 para desativar a passagem direta extra. | FLOAT | Sim | 1.0 a 100.0 (padrão: 3.0) |
| `start_percent` | O ponto do processo de amostragem, como porcentagem de 0.0 a 1.0, em que a orientação de modalidade começa. O padrão é 0.0. | FLOAT | Sim | 0.0 a 1.0 (padrão: 0.0) |
| `end_percent` | O ponto do processo de amostragem, como porcentagem de 0.0 a 1.0, em que a orientação de modalidade termina. O padrão é 1.0. | FLOAT | Sim | 0.0 a 1.0 (padrão: 1.0) |

A orientação é aplicada apenas às etapas de amostragem cujos valores de sigma estejam dentro da faixa definida por `start_percent` e `end_percent`. Fora dessa faixa, o nó retorna o resultado sem ruído inalterado. Um `modality_scale` de 1.0 também desativa completamente a passagem direta extra.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model` | O modelo clonado com uma função de orientação pós-CFG anexada. Este modelo modificado aplica a orientação de modalidade durante a amostragem. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVModalityGuidance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `038be607c42e626a8a8f5fe336ee466d0847d43835edb71e20ff38f668069cfb`
