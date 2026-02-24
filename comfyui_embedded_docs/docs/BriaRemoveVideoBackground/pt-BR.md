> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/pt-BR.md)

Este nó remove o fundo de um vídeo usando o serviço Bria AI. Ele processa o vídeo de entrada e substitui o fundo original por uma cor sólida de sua escolha. A operação é realizada por meio de uma API externa, e o resultado é retornado como um novo arquivo de vídeo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Sim | N/A | O arquivo de vídeo de entrada do qual o fundo será removido. |
| `background_color` | STRING | Sim | `"Black"`<br>`"White"`<br>`"Gray"`<br>`"Red"`<br>`"Green"`<br>`"Blue"`<br>`"Yellow"`<br>`"Cyan"`<br>`"Magenta"`<br>`"Orange"` | A cor sólida a ser usada como o novo fundo para o vídeo de saída. |
| `seed` | INT | Não | 0 a 2147483647 | Um valor de semente que controla se o nó deve ser executado novamente. Os resultados são não determinísticos, independentemente do valor da semente. (padrão: 0) |

**Observação:** O vídeo de entrada deve ter uma duração de 60 segundos ou menos.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo processado com o fundo removido e substituído pela cor selecionada. |