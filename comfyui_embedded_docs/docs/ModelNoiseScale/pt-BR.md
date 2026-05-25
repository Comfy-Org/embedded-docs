> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelNoiseScale/pt-BR.md)

Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelNoiseScale/en.md)

## Visão Geral

Este nó ajusta a escala de ruído usada durante a amostragem do modelo. Ele permite definir um valor específico para a escala de ruído, que controla a quantidade de ruído aplicada ao processo de amostragem do modelo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | MODEL | Sim | - | O modelo ao qual será aplicado o ajuste da escala de ruído. |
| `escala_de_ruído` | FLOAT | Sim | 0.0 a 64.0 (passo: 0.01) | Escala de ruído absoluta do treinamento. Por exemplo, HiDream-O1 base: 8.0, dev: 7.5. (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `MODEL` | MODEL | O modelo modificado com a nova escala de ruído aplicada. |

---
**Source fingerprint (SHA-256):** `37b77a5d65fb872f45be8ffa4efb65037bc7459bb001babaaf6b526a9a735190`
