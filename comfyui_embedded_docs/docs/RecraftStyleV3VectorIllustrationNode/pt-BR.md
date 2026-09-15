# RecraftStyleV3VectorIllustrationNode

Este nó seleciona um estilo para a API Recraft, especificamente a categoria de estilo de ilustração vetorial. Opcionalmente, você pode escolher um subestilo mais específico dentro dessa categoria. O nó gera um objeto de configuração de estilo que pode ser passado para outros nós Recraft.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `substyle` | Um subestilo mais específico dentro da categoria de ilustração vetorial. As opções disponíveis são os subestilos definidos para o estilo `vector_illustration` pela API Recraft. Se nenhum subestilo for escolhido, o estilo base `vector_illustration` será usado. | COMBO | Sim | Várias opções disponíveis (lista de subestilos carregada dinamicamente para o estilo `vector_illustration`) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `recraft_style` | Um objeto de configuração de estilo Recraft contendo o estilo de ilustração vetorial selecionado e o subestilo opcional. Pode ser conectado a outros nós Recraft. | STYLEV3 |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3VectorIllustrationNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e88e7ea35b18acb55ec59814981cb36451d922d3287d23dcdb504289ea9f541b`
