# Escala de Ruído do Modelo

Este nó ajusta a escala de ruído usada durante a amostragem do modelo. Ele permite definir um valor específico de escala de ruído, que controla a quantidade de ruído aplicada ao processo de amostragem do modelo. O nó clona o modelo e atualiza sua configuração de amostragem com a nova escala de ruído, mantendo as configurações existentes de deslocamento (shift) e multiplicador.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo ao qual aplicar o ajuste de escala de ruído. | MODEL | Sim | - |
| `noise_scale` | Escala de ruído de treinamento absoluta. Por exemplo, HiDream-O1 base: 8.0, dev: 7.5. (padrão: 1.0) | FLOAT | Sim | 0.0 a 64.0 (passo: 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `MODEL` | O modelo modificado com a nova escala de ruído aplicada. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelNoiseScale/pt-BR.md)

---
**Source fingerprint (SHA-256):** `75b0b99323fc15ff3cafc23de05a9d6b52d059494fbc229e5fb685d2908dd5d3`
