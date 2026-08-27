# LotusConditioning

O nó LotusConditioning fornece embeddings de condicionamento pré-computados para o modelo Lotus. Ele usa um codificador congelado com condicionamento nulo e retorna embeddings de prompt fixos para alcançar paridade com a implementação de referência, sem exigir inferência ou carregar grandes arquivos de tensor. Este nó gera um tensor de condicionamento fixo que pode ser usado diretamente no pipeline de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| *Sem entradas* | Este nó não aceita nenhum parâmetro de entrada. | - | - | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `conditioning` | Os embeddings de condicionamento pré-computados para o modelo Lotus, contendo embeddings de prompt fixos e um dicionário vazio. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1fcb6530850341253c8acb47b2f26ee79d93f51eca84bef03a1fa5de33d6bc8d`
