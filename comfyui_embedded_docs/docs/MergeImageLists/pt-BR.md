O nó **Merge Image Lists** combina múltiplas listas separadas de imagens em uma única lista contínua. Ele funciona pegando todas as imagens de cada entrada conectada e anexando-as na ordem em que são recebidas. Isso é útil para organizar ou agrupar imagens de diferentes fontes para processamento posterior.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `imagens` | Uma lista de imagens a serem mescladas. Esta entrada pode aceitar múltiplas conexões, e cada lista conectada será concatenada na saída final. | IMAGE | Sim | - |

**Nota:** Este nó foi projetado para receber múltiplas entradas. Você pode conectar várias listas de imagens ao único soquete de entrada `images`. O nó concatenará automaticamente todas as imagens de todas as listas conectadas em uma única lista de saída.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagens` | A única lista mesclada contendo todas as imagens de cada lista de entrada conectada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeImageLists/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8fc53091b817a5036aae022aa841ba11fae0ed3242a969f5ae9072f48e061366`
