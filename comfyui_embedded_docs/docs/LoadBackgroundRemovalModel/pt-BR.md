# Carregar Modelo de Remoção de Fundo

Carrega um modelo de remoção de fundo a partir de um arquivo e o deixa pronto para uso por outros nós na remoção de fundos de imagens. O arquivo do modelo é selecionado entre os arquivos disponíveis na pasta `background_removal`.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `bg_removal_name` | O modelo usado para remover fundos de imagens. | COMBO | Sim | Lista de arquivos de modelo disponíveis (lista ordenada de arquivos na pasta background_removal) |

**Nota:** O nó gera um erro se o arquivo selecionado não contiver um modelo de remoção de fundo válido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `bg_model` | O modelo de remoção de fundo carregado, pronto para ser usado por outros nós no processamento de imagens. | BACKGROUND_REMOVAL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/pt-BR.md)

---
**Source fingerprint (SHA-256):** `76f6536eae849a8b63f46f11c6afcf8c89774e4e89a5976e051253acc6108bcc`
