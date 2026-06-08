O nó **Criar Lista** combina múltiplas entradas em uma única lista sequencial. Ele aceita qualquer número de entradas do mesmo tipo de dado e as concatena na ordem em que estão conectadas. Este nó é útil para preparar lotes de dados, como imagens ou textos, para serem processados por outros nós em um fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `input_*` | Um número variável de slots de entrada. Você pode adicionar mais entradas clicando no ícone de mais (+). Todas as entradas devem ser do mesmo tipo de dado (ex.: todas IMAGE ou todas STRING). | Variável | Sim | Qualquer |

**Observação:** O nó criará automaticamente novos slots de entrada conforme você conecta itens. Todas as entradas conectadas devem compartilhar o mesmo tipo de dado para que o nó funcione corretamente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `list` | Uma única lista contendo todos os itens das entradas conectadas, concatenados na ordem em que foram fornecidos. O tipo de dado da saída corresponde ao tipo de dado da entrada. | Variável |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateList/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d0e10c4d1186e694a72b18407c34cc1df74f77d02c989b507af75594c1a0794e`
