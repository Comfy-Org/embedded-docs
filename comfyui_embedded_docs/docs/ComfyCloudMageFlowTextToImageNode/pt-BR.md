# Comfy Cloud Mage Flow Texto para Imagem [BETA]

Este nó gera uma imagem a partir de um prompt de texto enviando a solicitação para o fluxo de trabalho text-to-image do Mage-Flow no Comfy Cloud. Ele executa a passagem completa de geração com 30 etapas em vez da passagem turbo destilada, mais rápida, e aceita um prompt negativo para que você possa descrever conteúdo que não deseja na imagem final. O prompt negativo é compatível com este modo de 30 etapas; de acordo com o resumo do nó, a variante turbo destilada não consegue fazer bom uso dele.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | A descrição textual da imagem a ser gerada. | STRING | Sim | Texto livre |
| `negative_prompt` | Texto que descreve conteúdo que não deve aparecer na imagem gerada. Esta entrada é usada durante a passagem de geração padrão de 30 etapas, mas a variante turbo destilada não utiliza bem os prompts negativos. | STRING | Não | Texto livre |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem gerada a partir do prompt de texto e do prompt negativo fornecidos. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTextToImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `80f4ecf1df3f2c46d94138f8ada817e12cc49e69e69a001630776ed644868367`
