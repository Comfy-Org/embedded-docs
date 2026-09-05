# SenseNovaSamplingOptions

SenseNova Sampling Options define o flow shift SenseNova em um modelo. Ele clona o modelo de entrada, anexa uma configuração de amostragem do modelo SenseNova usando o valor de flow shift escolhido e retorna o modelo ajustado para uso durante a amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo ao qual a configuração de amostragem com flow shift SenseNova é aplicada. | MODEL | Sim | - |
| `shift` | O valor de flow shift a definir na amostragem do modelo SenseNova (padrão: 3.0; passo da interface: 0.01). | FLOAT | Sim | Nenhum mínimo ou máximo definido |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `MODEL` | Um clone do modelo de entrada com o flow shift SenseNova aplicado à sua configuração de amostragem. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaSamplingOptions/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b0dea4a5c226bccb54bb1d70e8ea2791a645018853571429c556034351e9e75a`
