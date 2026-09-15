# LotusConditioning

O nó LotusConditioning fornece embeddings de condicionamento fixos e pré-computados para o modelo Lotus. Como o Lotus usa um codificador congelado com condicionamento nulo, o nó incorpora diretamente os embeddings de prompt resultantes em vez de executar inferência ou carregar arquivos grandes de tensor, portanto sua saída nunca muda. O condicionamento retornado pode ser conectado diretamente a um pipeline de geração que espera condicionamento compatível com o Lotus.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| *Sem entradas* | Este nó não aceita nenhum parâmetro de entrada. | - | - | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `conditioning` | Os embeddings de condicionamento fixos e pré-computados para o modelo Lotus. Retornado como uma lista de condicionamento que contém os embeddings de prompt fixos junto com um dicionário vazio. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1fcb6530850341253c8acb47b2f26ee79d93f51eca84bef03a1fa5de33d6bc8d`
