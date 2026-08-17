# Combo Personalizado

O nó Custom Combo permite criar um menu suspenso personalizado com sua própria lista de opções de texto. É um nó focado no frontend que fornece uma representação no backend para garantir compatibilidade dentro do seu fluxo de trabalho. Quando você seleciona uma opção no menu suspenso, o nó gera esse texto como uma string e sua posição de índice.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `choice` | A opção de texto selecionada no menu suspenso personalizado. A lista de opções disponíveis é definida pelo usuário na interface frontend do nó. | COMBO | Sim | Definido pelo usuário |
| `index` | Um valor inteiro que pode ser usado para especificar um índice. Padrão: 0. | INT | Não | Qualquer inteiro |

**Observação:** A validação para a entrada deste nó está intencionalmente desabilitada. Isso permite que você defina quaisquer opções de texto personalizadas no frontend sem que o backend verifique se a sua seleção pertence a uma lista predefinida. Este nó é marcado como experimental.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `STRING` | A string de texto da opção selecionada na caixa de combinação personalizada. | STRING |
| `INDEX` | A posição do índice da opção selecionada na lista suspensa. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CustomCombo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `143eafcf32de7ebaf72b5387537154b5deee7d3e3a520a0b2c12ac4fb67890f8`
