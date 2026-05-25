> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/pt-BR.md)

# Visão Geral

Gere respostas de texto a partir de um modelo Anthropic Claude. Este nó envia um prompt de texto e imagens opcionais para um modelo Claude e retorna a resposta de texto gerada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | N/A | Entrada de texto para o modelo. (padrão: string vazia) |
| `modelo` | COMBO | Sim | `"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` | O modelo Claude usado para gerar a resposta. |
| `seed` | INT | Sim | 0 a 2147483647 | A semente controla se o nó deve ser executado novamente; os resultados são não-determinísticos independentemente da semente. (padrão: 0) |
| `imagens` | IMAGE | Não | 0 a 20 imagens | Imagem(ns) opcional(is) para usar como contexto para o modelo. Até 20 imagens. |
| `system_prompt` | STRING | Não | N/A | Instruções fundamentais que determinam o comportamento do modelo. (padrão: string vazia) |

### Restrições dos Parâmetros

- **Limite de Imagens**: No máximo 20 imagens podem ser fornecidas por requisição.
- **Gerenciamento de Temperatura**: Quando o pensamento está habilitado ou ao usar o modelo "Opus 4.7", o parâmetro de temperatura é automaticamente desabilitado (padrão para 1.0) conforme exigido pela API Anthropic. Para outros modelos, a temperatura pode ser definida através da configuração do modelo.
- **Pensamento/Raciocínio**: A configuração do modelo inclui uma opção `reasoning_effort` que controla se o pensamento está habilitado. Quando habilitado, o nó configura automaticamente o modo de pensamento apropriado (adaptativo ou baseado em orçamento) dependendo do modelo selecionado.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | STRING | A resposta de texto gerada pelo modelo Claude. Retorna "Resposta vazia do modelo Claude." se nenhum texto for gerado. |

---
**Source fingerprint (SHA-256):** `e3bab004535d4d406582aa42f28bb64a2988f8331788d51ec1fa4e943d8d4382`
