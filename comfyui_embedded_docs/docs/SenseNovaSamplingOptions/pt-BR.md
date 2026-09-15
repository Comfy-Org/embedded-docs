# Opções de amostragem do SenseNova

O nó SenseNova Sampling Options define o deslocamento de fluxo (flow shift) do SenseNova em um modelo. Ele clona o modelo de entrada, associa uma configuração de amostragem do modelo SenseNova usando o valor de deslocamento de fluxo escolhido e retorna o modelo com patch para uso durante a amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo ao qual a configuração de amostragem de deslocamento de fluxo do SenseNova é aplicada. | MODEL | Sim | - |
| `shift` | O valor de deslocamento de fluxo (flow shift) a ser definido na amostragem do modelo SenseNova (padrão: 3.0; passo da UI: 0.01). | FLOAT | Sim | Nenhum mínimo ou máximo definido |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `MODEL` | Um clone do modelo de entrada com o deslocamento de fluxo (flow shift) do SenseNova aplicado à sua configuração de amostragem. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaSamplingOptions/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b0dea4a5c226bccb54bb1d70e8ea2791a645018853571429c556034351e9e75a`
