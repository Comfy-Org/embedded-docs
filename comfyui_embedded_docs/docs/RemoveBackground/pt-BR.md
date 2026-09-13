# Remover Fundo

## Visão geral

O nó Remove Background gera uma máscara de primeiro plano que separa o assunto principal do fundo de uma imagem de entrada. Ele usa um modelo de remoção de fundo para analisar a imagem e produzir uma máscara que destaca os elementos do primeiro plano.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `bg_removal_model` | Modelo de remoção de fundo usado para gerar a máscara | BACKGROUND_REMOVAL_MODEL | Sim | N/A |
| `image` | Imagem de entrada da qual remover o fundo | IMAGE | Sim | N/A |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `mask` | Máscara de primeiro plano gerada | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemoveBackground/pt-BR.md)

---
**Source fingerprint (SHA-256):** `75b415acedaeaa1a694aeba2e4b0367524c6878e3e4a1f48b2a62898c68109f9`
