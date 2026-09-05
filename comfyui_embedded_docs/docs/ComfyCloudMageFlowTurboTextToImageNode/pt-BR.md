# ComfyCloudMageFlowTurboTextToImageNode

Este nó Comfy Cloud gera uma imagem a partir de um prompt de texto usando o fluxo de trabalho Mage-Flow Turbo (`mage-flow-turbo/text-to-image`). Ele executa uma versão destilada do modelo Mage-Flow que gera a imagem em 4 etapas com valor de cfg de 1, consumindo cerca de um sétimo do tempo de GPU de uma passagem completa do Mage-Flow, o que o torna a variante destinada à iteração rápida.

## Entradas

A própria classe do nó não declara widgets de entrada no código-fonte disponível; seu esquema de entrada é herdado da classe base compartilhada `_ComfyCloudMageFlowNode`, cuja definição não está incluída no instantâneo do código-fonte. Com base no resumo do nó e no nome do fluxo de trabalho de texto para imagem, o nó recebe um prompt de texto descrevendo a imagem a ser gerada.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | O prompt de texto que descreve a imagem a ser gerada. O nome exato do parâmetro é definido pelo esquema base herdado `_ComfyCloudMageFlowNode` e pode diferir deste rótulo. | STRING | Sim | Texto livre |

Observação: Parâmetros de entrada adicionais podem existir na definição do nó base herdado, que não está disponível no código-fonte fornecido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem gerada a partir do prompt de texto. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTurboTextToImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8d867a0c906028597ef52c75f5c9a994fdc00211c7aae410ffca8204943f0c34`
