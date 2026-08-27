# Criar Lista

O nó Create List combina múltiplas entradas em uma única lista sequencial. Ele aceita qualquer número de entradas do mesmo tipo de dados e as concatena na ordem em que são conectadas. Este nó é útil para preparar lotes de dados, como imagens ou textos, para serem processados por outros nós em um fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `entradas` | Um número variável de slots de entrada nomeados `input`, `input_2`, `input_3` e assim por diante. Cada slot aceita uma lista de itens do mesmo tipo de dados. Você pode adicionar mais slots clicando no ícone de adição (+). Todos os slots devem usar o mesmo tipo de dados (por exemplo, todos IMAGE ou todos STRING). | Varia | Sim | Qualquer número de slots; cada slot aceita qualquer número de itens |

**Observação:** O nó cria automaticamente novos slots de entrada conforme você conecta itens. Todas as entradas conectadas devem compartilhar o mesmo tipo de dados para que o nó funcione corretamente. Cada slot conectado fornece uma lista de itens, e o nó combina as listas na ordem dos slots (`input`, depois `input_2`, depois `input_3`, ...). O nó também pode ser encontrado pelos sinônimos "Image Iterator", "Text Iterator" e "Iterator".

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `lista` | Uma única lista contendo todos os itens das entradas conectadas, concatenados na ordem em que foram fornecidos. O tipo de dados da saída corresponde ao tipo de dados da entrada. | Varia |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateList/pt-BR.md)

---
**Source fingerprint (SHA-256):** `457d17da815ef9cee000d9e8dc8768f19ddfe247feae4b2ff4ce3c6cc0fd564e`
