# MultiGPU_Options

Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MultiGPU_Options/en.md)

## Visão Geral

Este nó permite especificar o desempenho relativo de cada GPU ao usar múltiplas placas gráficas com velocidades diferentes. Ele cria um grupo de opções de GPU que pode ser usado para distribuir o trabalho entre os dispositivos, embora a distribuição real de carga baseada em velocidade ainda não esteja implementada na versão atual.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `device_index` | O número do índice do dispositivo GPU a ser configurado (padrão: 0) | INT | Sim | 0 a 64 |
| `relative_speed` | A velocidade relativa desta GPU em comparação com outras, usada para distribuição de carga de trabalho (padrão: 1.0, incremento: 0.01) | FLOAT | Sim | 0.0 a ilimitado |
| `gpu_options` | Um grupo de opções de GPU existente para adicionar as opções deste dispositivo. Se não for fornecido, um novo grupo é criado | GPU_OPTIONS | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `GPU_OPTIONS` | Um grupo de opções de GPU contendo as configurações do dispositivo configurado, que pode ser passado para outros nós para operações com múltiplas GPUs | GPU_OPTIONS |

**Observação:** O parâmetro `relative_speed` está definido, mas ainda não é utilizado pelo agendador interno para distribuir o trabalho entre as GPUs. Na implementação atual, o trabalho é distribuído uniformemente entre todos os dispositivos, independentemente de suas velocidades relativas.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MultiGPU_Options/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8010460560a69c57d4ee0d8c3728a7a5d999e56ef5316b557fba0c660c9f38b0`
