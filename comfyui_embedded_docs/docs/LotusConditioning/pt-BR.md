> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LotusConditioning/pt-BR.md)

O nó LotusConditioning fornece embeddings de condicionamento pré-computados para o modelo Lotus. Ele utiliza um codificador congelado com condicionamento nulo e retorna embeddings de prompt fixos para alcançar paridade com a implementação de referência, sem exigir inferência ou carregamento de arquivos de tensor grandes. Este nó gera um tensor de condicionamento fixo que pode ser usado diretamente no pipeline de geração.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| *Sem entradas* | - | - | - | Este nó não aceita nenhum parâmetro de entrada. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | Os embeddings de condicionamento pré-computados para o modelo Lotus, contendo embeddings de prompt fixos e um dicionário vazio. |
