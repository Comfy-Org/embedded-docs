# Criar Lista

O nó Create List combina várias entradas em uma única lista sequencial. Ele aceita qualquer número de slots de entrada que compartilhem o mesmo tipo de dados e concatena seus itens na ordem em que os slots são conectados. O resultado é uma lista contendo todos os itens conectados.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `entradas` | Um número variável de slots de entrada chamados `input`, `input_2`, `input_3` e assim por diante. Cada slot aceita uma lista de itens do mesmo tipo de dados (por exemplo, todos IMAGE ou todos STRING). Novos slots são criados automaticamente conforme necessário. O nó concatena as listas na ordem dos slots. | Any | Sim | Qualquer número de slots; cada slot aceita qualquer número de itens |

**Nota:** Todas as entradas conectadas devem compartilhar o mesmo tipo de dados. Cada slot conectado fornece uma lista de itens, e o nó combina as listas na ordem dos slots (`input`, depois `input_2`, depois `input_3`, ...). O nó também pode ser encontrado pelos nomes alternativos "Image Iterator", "Text Iterator" e "Iterator".

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `list` | Uma única lista contendo todos os itens das entradas conectadas, concatenados na ordem em que os slots foram fornecidos. O tipo de dados da saída corresponde ao tipo de dados da entrada. | Any |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateList/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4824fa6af46ab08cd3c10b033dbb3e43682b468e1dbd934fffb571349e025b96`
