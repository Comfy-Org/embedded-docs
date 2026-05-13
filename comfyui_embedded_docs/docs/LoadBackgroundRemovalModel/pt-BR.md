> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/pt-BR.md)

## Visão Geral

Carrega um modelo de remoção de fundo a partir de um arquivo. Este nó prepara o modelo para ser utilizado na remoção de fundos de imagens.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `bg_removal_name` | STRING | Sim | Lista de arquivos de modelo disponíveis | O modelo usado para remover fundos de imagens. Selecione na lista de arquivos de modelo de remoção de fundo disponíveis. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `bg_model` | BACKGROUND_REMOVAL | O modelo de remoção de fundo carregado, pronto para ser usado por outros nós no processamento de imagens. |

---
**Source fingerprint (SHA-256):** `63a1ffb37ea8581e3ba29f7dc4f871612d7ec458e6d36f5e2244201941d48f9d`
