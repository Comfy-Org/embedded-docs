> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaConceptsNode/pt-BR.md)

Armazena um ou mais Conceitos de Câmera para uso com os nós Luma Text to Video e Luma Image to Video. Este nó permite selecionar até quatro conceitos de câmera e, opcionalmente, combiná-los com cadeias de conceitos existentes.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `concept1` | STRING | Sim | Múltiplas opções disponíveis<br>Inclui opção "None" | Primeira seleção de conceito de câmera a partir dos conceitos Luma disponíveis |
| `concept2` | STRING | Sim | Múltiplas opções disponíveis<br>Inclui opção "None" | Segunda seleção de conceito de câmera a partir dos conceitos Luma disponíveis |
| `concept3` | STRING | Sim | Múltiplas opções disponíveis<br>Inclui opção "None" | Terceira seleção de conceito de câmera a partir dos conceitos Luma disponíveis |
| `concept4` | STRING | Sim | Múltiplas opções disponíveis<br>Inclui opção "None" | Quarta seleção de conceito de câmera a partir dos conceitos Luma disponíveis |
| `luma_concepts` | LUMA_CONCEPTS | Não | N/A | Conceitos de Câmera opcionais para adicionar aos escolhidos aqui |

**Observação:** Todos os parâmetros de conceito (`concept1` a `concept4`) podem ser definidos como "None" se você não quiser usar todos os quatro espaços de conceito. O nó mesclará quaisquer `luma_concepts` fornecidos com os conceitos selecionados para criar uma cadeia de conceitos combinada.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `luma_concepts` | LUMA_CONCEPTS | Cadeia de conceitos de câmera combinada contendo todos os conceitos selecionados |
