# TSR - Redimensionamento Temporal de Pontuação

Este nó aplica Temporal Score Rescaling (TSR) a um modelo de difusão. Ele aplica patch ao modelo para que, durante a amostragem, o score previsto ou o ruído seja reescalonado para direcionar a diversidade dos resultados gerados. Isso é implementado como uma função pós-CFG (Classifier-Free Guidance).

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão que receberá o patch da função TSR. | MODEL | Sim | - |
| `tsr_k` | Controla a força do reescalonamento. Um k menor produz resultados mais detalhados; um k maior produz resultados mais suaves na geração de imagens. Definir k = 1 desativa o reescalonamento. (padrão: 0.95) | FLOAT | Sim | 0.01 - 100.0 |
| `tsr_sigma` | Controla quão cedo o reescalonamento entra em vigor. Valores maiores entram em vigor mais cedo. (padrão: 1.0) | FLOAT | Sim | 0.01 - 100.0 |

Observação: O reescalonamento é ignorado quando `tsr_k` é definido como 1, quando o valor de sigma é 0 ou quando a relação sinal-ruído é 0.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `patched_model` | O modelo de entrada, agora com patch da função Temporal Score Rescaling aplicado ao seu processo de amostragem. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4d4e3c64fb6e3a3fe4725ea944a361b46d871943a10e65d72d70e0e6d757dfca`
