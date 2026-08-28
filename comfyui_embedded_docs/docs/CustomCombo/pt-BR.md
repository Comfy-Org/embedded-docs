# Combo Personalizado

O nó Custom Combo permite criar um menu suspenso personalizado com sua própria lista de opções de texto. É um nó focado no frontend que inclui uma representação no backend para manter seu fluxo de trabalho compatível. Quando você seleciona uma opção no menu suspenso, o nó emite esse texto como uma string e sua posição de índice.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `escolha` | A opção de texto selecionada no menu suspenso personalizado. A lista de opções disponíveis é definida pelo usuário na interface frontend do nó. | COMBO | Sim | Definido pelo usuário |
| `index` | Um valor inteiro que pode ser usado para especificar um índice. Padrão: 0. | INT | Não | Qualquer inteiro (padrão: 0) |

**Nota:** A validação das entradas deste nó está intencionalmente desativada. Isso permite que você escreva quaisquer opções de texto personalizadas no frontend sem que o backend verifique se sua seleção corresponde a uma lista predefinida. Widgets além do menu suspenso de combinação são totalmente definidos no frontend. Este nó está marcado como experimental.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `STRING` | A string de texto da opção selecionada na caixa de combinação personalizada. | STRING |
| `ÍNDICE` | A posição do índice da opção selecionada na lista suspensa. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CustomCombo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `143eafcf32de7ebaf72b5387537154b5deee7d3e3a520a0b2c12ac4fb67890f8`
