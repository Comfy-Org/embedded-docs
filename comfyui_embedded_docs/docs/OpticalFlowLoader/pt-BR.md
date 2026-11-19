# Carregar Modelo de Optical Flow

Carrega um modelo de fluxo óptico da pasta `models/optical_flow/`. Atualmente, apenas o formato RAFT-large do torchvision é suportado, que é o modelo usado pelo nó VOIDWarpedNoise. O ComfyUI não baixa os pesos do fluxo óptico automaticamente; você deve colocar o arquivo de checkpoint manualmente no diretório `models/optical_flow/`.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model_name` | Modelo de fluxo óptico a ser carregado. Os arquivos devem ser colocados na pasta `optical_flow`. Hoje, apenas o `raft_large.pth` do torchvision é suportado. | COMBO | Sim | Lista de arquivos na pasta `models/optical_flow/` |

Nota: O checkpoint selecionado deve ser um dicionário de estado do RAFT-large do torchvision contendo chaves prefixadas com `feature_encoder.`, `context_encoder.` e `update_block.`. Se o arquivo não corresponder a esse formato, o nó gerará um ValueError.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `OPTICAL_FLOW` | O modelo de fluxo óptico carregado, configurado para modo de avaliação, com precisão fp16 em dispositivos que a suportam e sem `--force-fp32` (float32 caso contrário), encapsulado em um ModelPatcher para uso com outros nós. | OPTICAL_FLOW |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `82e5d747679ede113ec4d72fd6eda4b8f20d098832612bebf26ef65de8b4b3dc`
