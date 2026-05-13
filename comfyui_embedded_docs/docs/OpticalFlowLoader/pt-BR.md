> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/en.md)

## Visão Geral

Carrega um modelo de fluxo óptico da pasta `models/optical_flow/`. Atualmente, apenas o formato RAFT-large do torchvision é suportado, que é o modelo usado pelo nó VOIDWarpedNoise. O ComfyUI não baixa pesos de fluxo óptico automaticamente; você deve colocar o arquivo de checkpoint manualmente no diretório `models/optical_flow/`.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model_name` | STRING | Sim | Lista de arquivos na pasta `models/optical_flow/` | Modelo de fluxo óptico a ser carregado. Os arquivos devem ser colocados na pasta `optical_flow`. Atualmente, apenas o `raft_large.pth` do torchvision é suportado. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `OPTICAL_FLOW` | MODEL | O modelo de fluxo óptico carregado, encapsulado em um ModelPatcher para uso com outros nós. |

---
**Source fingerprint (SHA-256):** `94bab0bb7e2b9d9b3f343337799eccc744f79275b72a6fad9681b408b4a0820b`
