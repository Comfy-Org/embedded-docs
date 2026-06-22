# Anthropic Claude

Gere respostas de texto a partir de um modelo Anthropic Claude. Este nó envia um prompt de texto e imagens opcionais para um modelo Claude e retorna a resposta de texto gerada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Entrada de texto para o modelo. (padrão: string vazia) | STRING | Sim | N/A |
| `modelo` | O modelo Claude usado para gerar a resposta. | COMBO | Sim | `"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não-determinísticos independentemente da semente. (padrão: 0) | INT | Sim | 0 a 2147483647 |
| `imagens` | Imagem(ns) opcional(is) para usar como contexto para o modelo. Até 20 imagens. | IMAGE | Não | 0 a 20 imagens |
| `system_prompt` | Instruções fundamentais que determinam o comportamento do modelo. (padrão: string vazia) | STRING | Não | N/A |

### Restrições dos Parâmetros

- **Limite de Imagens**: No máximo 20 imagens podem ser fornecidas por requisição.
- **Gerenciamento de Temperatura**: Quando o pensamento está habilitado ou ao usar o modelo "Opus 4.7", o parâmetro de temperatura é automaticamente desabilitado (padrão para 1.0) conforme exigido pela API Anthropic. Para outros modelos, a temperatura pode ser definida através da configuração do modelo.
- **Pensamento/Raciocínio**: A configuração do modelo inclui uma opção `reasoning_effort` que controla se o pensamento está habilitado. Quando habilitado, o nó configura automaticamente o modo de pensamento apropriado (adaptativo ou baseado em orçamento) dependendo do modelo selecionado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A resposta de texto gerada pelo modelo Claude. Retorna "Resposta vazia do modelo Claude." se nenhum texto for gerado. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e3bab004535d4d406582aa42f28bb64a2988f8331788d51ec1fa4e943d8d4382`
