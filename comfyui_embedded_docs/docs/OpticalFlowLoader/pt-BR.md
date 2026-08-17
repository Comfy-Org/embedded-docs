# Carregar Modelo de Optical Flow

## Visão Geral

Carrega um modelo de fluxo óptico da pasta `models/optical_flow/`. Atualmente, apenas o formato RAFT-large do torchvision é suportado, que é o modelo usado pelo nó VOIDWarpedNoise. O ComfyUI não baixa os pesos do fluxo óptico automaticamente; você deve colocar o arquivo de checkpoint manualmente no diretório `models/optical_flow/`.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model_name` | Modelo de fluxo óptico a ser carregado. Os arquivos devem ser colocados na pasta `optical_flow`. Atualmente, apenas o `raft_large.pth` do torchvision é suportado. | COMBO | Sim | Lista de arquivos na pasta `models/optical_flow/` |

O arquivo selecionado deve ser um checkpoint RAFT-large do torchvision. O nó verifica se o arquivo contém as chaves RAFT esperadas (`feature_encoder.*`, `context_encoder.*` e `update_block.*`) e gera um ValueError se o formato não for reconhecido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `OPTICAL_FLOW` | O modelo de fluxo óptico carregado, encapsulado em um ModelPatcher para uso com outros nós. | OPTICAL_FLOW |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5e79551545ad7ee2fd4856a47da29808a404342d1d5e57da0980058db6b11c3b`
