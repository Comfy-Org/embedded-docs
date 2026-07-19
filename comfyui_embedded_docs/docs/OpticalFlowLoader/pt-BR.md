# Carregar Modelo de Optical Flow

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/en.md)

## Visão Geral

Carrega um modelo de fluxo óptico da pasta `models/optical_flow/`. Atualmente, apenas o formato RAFT-large do torchvision é suportado, que é o modelo usado pelo nó VOIDWarpedNoise. O ComfyUI não baixa pesos de fluxo óptico automaticamente; você deve colocar o arquivo de checkpoint manualmente no diretório `models/optical_flow/`.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model_name` | Modelo de fluxo óptico a ser carregado. Os arquivos devem ser colocados na pasta `optical_flow`. Atualmente, apenas o `raft_large.pth` do torchvision é suportado. | STRING | Sim | Lista de arquivos na pasta `models/optical_flow/` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `OPTICAL_FLOW` | O modelo de fluxo óptico carregado, encapsulado em um ModelPatcher para uso com outros nós. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `94bab0bb7e2b9d9b3f343337799eccc744f79275b72a6fad9681b408b4a0820b`
