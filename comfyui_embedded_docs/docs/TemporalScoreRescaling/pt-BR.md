# TSR - Redimensionamento Temporal de Pontuação

Este nó aplica o Reescalonamento Temporal de Score (TSR) a um modelo de difusão. Ele modifica o comportamento de amostragem do modelo ao reescalonar o ruído ou score previsto durante o processo de denoising, o que pode direcionar a diversidade da saída gerada. Isso é implementado como uma função pós-CFG (Classifier-Free Guidance).

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão a ser modificado com a função TSR. | MODEL | Sim | - |
| `tsr_k` | Controla a força do reescalonamento. Valores menores de k produzem resultados mais detalhados; valores maiores produzem resultados mais suaves na geração de imagens. Definir k = 1 desativa o reescalonamento. (padrão: 0,95) | FLOAT | Não | 0.01 - 100.0 |
| `tsr_sigma` | Controla o quão cedo o reescalonamento entra em vigor. Valores maiores entram em vigor mais cedo. (padrão: 1,0) | FLOAT | Não | 0.01 - 100.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `patched_model` | O modelo de entrada, agora modificado com a função de Reescalonamento Temporal de Score aplicada ao seu processo de amostragem. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4d4e3c64fb6e3a3fe4725ea944a361b46d871943a10e65d72d70e0e6d757dfca`
