Este nó aplica o Reajuste Temporal de Score (TSR) a um modelo de difusão. Ele modifica o comportamento de amostragem do modelo ao reajustar o ruído ou score previsto durante o processo de remoção de ruído, o que pode direcionar a diversidade da saída gerada. Isso é implementado como uma função pós-CFG (Orientação Livre de Classificador).

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão a ser modificado com a função TSR. | MODEL | Sim | - |
| `tsr_k` | Controla a intensidade do reajuste. Valores menores de k produzem resultados mais detalhados; valores maiores produzem resultados mais suaves na geração de imagens. Definir k = 1 desativa o reajuste. (padrão: 0.95) | FLOAT | Não | 0.01 - 100.0 |
| `tsr_sigma` | Controla o quão cedo o reajuste entra em ação. Valores maiores entram em ação mais cedo. (padrão: 1.0) | FLOAT | Não | 0.01 - 100.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `patched_model` | O modelo de entrada, agora modificado com a função de Reajuste Temporal de Score aplicada ao seu processo de amostragem. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2931b42ac93cf50e2c395bacf3128bb43dcc043ab5c8f86d7aabe4d35a44d20a`
