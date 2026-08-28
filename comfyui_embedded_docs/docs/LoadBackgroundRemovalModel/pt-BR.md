# Carregar Modelo de Remoção de Fundo

Carrega um modelo de remoção de fundo de um arquivo. Este nó prepara o modelo para uso na remoção de fundos de imagens.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `nome_remoção_fundo` | O modelo usado para remover fundos de imagens. Selecione na lista de arquivos de modelo de remoção de fundo disponíveis. | COMBO | Sim | Lista de arquivos de modelo disponíveis (ordenados alfabeticamente) |

Observação: se o arquivo selecionado não contiver um modelo de remoção de fundo válido, o nó gera um RuntimeError.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo_fundo` | O modelo de remoção de fundo carregado, pronto para ser usado por outros nós no processamento de imagens. | BACKGROUND_REMOVAL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/pt-BR.md)

---
**Source fingerprint (SHA-256):** `76f6536eae849a8b63f46f11c6afcf8c89774e4e89a5976e051253acc6108bcc`
