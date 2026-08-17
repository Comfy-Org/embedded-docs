# Criar Lista

O nó Create List combina várias entradas em uma única lista sequencial. Ele aceita qualquer número de entradas do mesmo tipo de dados e as concatena na ordem em que são conectadas. Este nó é útil para preparar lotes de dados, como imagens ou textos, para serem processados por outros nós em um fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `inputs` | Um conjunto expansível de slots de entrada. Adicione mais slots clicando no ícone de adição (+), ou conecte itens e novos slots serão criados automaticamente. Cada slot aceita um ou mais itens, e todos os slots devem compartilhar o mesmo tipo de dados (por exemplo, todos IMAGE ou todos STRING). | Varia (corresponde ao tipo de dados conectado) | Sim | Qualquer número de slots; cada slot aceita um ou mais itens |

**Observação:** O nó cria automaticamente novos slots de entrada conforme você conecta itens. Todas as entradas conectadas devem compartilhar o mesmo tipo de dados para que o nó funcione corretamente, e a lista de saída assume esse mesmo tipo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `list` | Uma única lista contendo todos os itens dos slots de entrada conectados, concatenados na ordem em que os slots estão conectados. O tipo de dados de saída corresponde ao tipo de dados de entrada. | Varia (corresponde ao tipo de dados de entrada) |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateList/pt-BR.md)

---
**Source fingerprint (SHA-256):** `457d17da815ef9cee000d9e8dc8768f19ddfe247feae4b2ff4ce3c6cc0fd564e`
