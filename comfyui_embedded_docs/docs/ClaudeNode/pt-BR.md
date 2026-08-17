# Anthropic Claude

Gera respostas de texto a partir de um modelo Claude da Anthropic. Este nó envia um prompt de texto e imagens opcionais para um modelo Claude e retorna a resposta de texto gerada.

## Entradas

O parâmetro `model` é um seletor dinâmico: quando você escolhe um modelo, configurações adicionais específicas do modelo, como limite de tokens, temperatura e esforço de raciocínio, aparecem abaixo dele.

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Texto de entrada para o modelo. Deve ser não vazio após remover espaços em branco. (padrão: string vazia) | STRING | Sim | N/A |
| `model` | O modelo Claude usado para gerar a resposta. | DYNAMIC_COMBO | Sim | `"Opus 5"`<br>`"Opus 4.8"`<br>`"Fable 5"`<br>`"Sonnet 5"`<br>`"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 0) | INT | Sim | 0 a 2147483647 |
| `images` | Imagem(ns) opcional(is) para usar como contexto para o modelo. Slot expansível: conecte de `image_1` a `image_20`; até 20 imagens. (padrão: nenhuma) | IMAGE | Não | 0 a 20 imagens |
| `system_prompt` | Instruções fundamentais que definem o comportamento do modelo. (padrão: string vazia) | STRING | Não | N/A |

### Entradas do Opus 5 e Fable 5

Compartilhadas por Opus 5 e Fable 5. Esses modelos sempre usam pensamento estendido e não expõem uma configuração de temperatura.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Número máximo de tokens a gerar (inclui tokens de raciocínio quando ativado). (padrão: 32768) | INT | Sim | 4096 a 64000 |
| `reasoning_effort` | Esforço de pensamento estendido. O raciocínio está sempre ativado para este modelo. (padrão: "high") | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"` |

### Entradas do Opus 4.8 e Sonnet 5

Compartilhadas por Opus 4.8 e Sonnet 5. Esses modelos não expõem uma configuração de temperatura.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Número máximo de tokens a gerar (inclui tokens de raciocínio quando ativado). (padrão: 32768) | INT | Sim | 4096 a 64000 |
| `reasoning_effort` | Esforço de pensamento estendido. "off" desativa o raciocínio. (padrão: "off") | COMBO | Sim | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Entradas do Opus 4.7, Opus 4.6, Sonnet 4.6 e Sonnet 4.5

Compartilhadas por Opus 4.7, Opus 4.6, Sonnet 4.6 e Sonnet 4.5. Para o Opus 4.7, o parâmetro de temperatura é exibido, mas é ignorado, e a API usa o valor padrão de 1.0.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Número máximo de tokens a gerar (inclui tokens de raciocínio quando ativado). (padrão: 32768) | INT | Sim | 4096 a 64000 |
| `temperature` | Controla a aleatoriedade. 0.0 é determinístico, 1.0 é o mais aleatório. Ignorado para Opus 4.7 e para qualquer modelo quando `reasoning_effort` estiver definido. (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo 0.01) |
| `reasoning_effort` | Esforço de pensamento estendido. "off" desativa o raciocínio. (padrão: "off") | COMBO | Sim | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Entradas do Haiku 4.5

Este modelo não suporta pensamento estendido, portanto nenhuma configuração de `reasoning_effort` está disponível.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Número máximo de tokens a gerar (inclui tokens de raciocínio quando ativado). (padrão: 32768) | INT | Sim | 4096 a 64000 |
| `temperature` | Controla a aleatoriedade. 0.0 é determinístico, 1.0 é o mais aleatório. (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo 0.01) |

### Restrições dos Parâmetros

- Até 20 imagens podem ser fornecidas por solicitação. A contagem total de pixels das imagens enviadas é limitada a 1568 × 1568 pixels.
- A temperatura não é configurável para Opus 5, Fable 5, Opus 4.8 e Sonnet 5. Quando um parâmetro de temperatura está disponível, ele é ignorado para Opus 4.7 e para qualquer modelo quando `reasoning_effort` estiver definido como algo diferente de "off".
- O raciocínio está sempre ativado para Opus 5 e Fable 5, portanto as opções de `reasoning_effort` para esses modelos não incluem "off". O modelo Haiku 4.5 não suporta pensamento estendido e, portanto, não possui configuração de `reasoning_effort`.
- Se o Claude se recusar a responder a uma solicitação por motivos de segurança, o nó lança um erro em vez de retornar texto.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A resposta de texto gerada pelo modelo Claude. Se nenhum texto visível for gerado, a saída será `"Empty response from Claude model."`. Blocos de pensamento ou raciocínio não são incluídos na saída. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b0381e7981e5886d66b6976c7ddcad3f142bdd803271a6ac8567293dcddaa98a`
