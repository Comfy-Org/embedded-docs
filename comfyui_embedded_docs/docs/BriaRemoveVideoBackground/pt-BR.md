Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/en.md)

Este nó remove o fundo de um vídeo usando o serviço de IA da Bria. Ele processa o vídeo de entrada e substitui o fundo original por uma cor sólida de sua escolha. A operação é realizada por meio de uma API externa, e o resultado é retornado como um novo arquivo de vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `vídeo` | O arquivo de vídeo de entrada do qual o fundo será removido. | VIDEO | Sim | N/A |
| `cor de fundo` | A cor sólida a ser usada como novo fundo para o vídeo de saída. | STRING | Sim | `"Black"`<br>`"White"`<br>`"Gray"`<br>`"Red"`<br>`"Green"`<br>`"Blue"`<br>`"Yellow"`<br>`"Cyan"`<br>`"Magenta"`<br>`"Orange"` |
| `semente` | Um valor de semente que controla se o nó deve ser executado novamente. Os resultados são não determinísticos, independentemente do valor da semente. (padrão: 0) | INT | Não | 0 a 2147483647 |

**Observação:** O vídeo de entrada deve ter duração de 60 segundos ou menos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O arquivo de vídeo processado com o fundo removido e substituído pela cor selecionada. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/pt-BR.md)

---
**Source fingerprint (SHA-256):** `51499fc006d3fd3fd45f8aad686d92537d399255b3a583fd54b77c5a0698a068`
