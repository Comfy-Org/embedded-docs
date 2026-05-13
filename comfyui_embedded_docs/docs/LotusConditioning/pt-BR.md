> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/pt-BR.md)

Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/en.md)

O nó LotusConditioning fornece embeddings de condicionamento pré-computados para o modelo Lotus. Ele utiliza um codificador congelado com condicionamento nulo e retorna embeddings de prompt codificados manualmente para alcançar paridade com a implementação de referência, sem exigir inferência ou carregamento de grandes arquivos de tensor. Este nó gera um tensor de condicionamento fixo que pode ser usado diretamente no pipeline de geração.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|---------------|-------------|-----------|-----------|
| *Nenhuma entrada* | - | - | - | Este nó não aceita nenhum parâmetro de entrada. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `conditioning` | CONDITIONING | Os embeddings de condicionamento pré-computados para o modelo Lotus, contendo embeddings de prompt fixos e um dicionário vazio. |

---
**Source fingerprint (SHA-256):** `aa428f8c355e2840dadbf634fe27d20c7c323dbe8c21255b40f4dafa12e4a0d0`
