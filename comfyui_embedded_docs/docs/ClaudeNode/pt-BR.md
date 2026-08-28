# Anthropic Claude

Gera respostas de texto dos modelos Claude da Anthropic. Forneça um prompt de texto e, opcionalmente, uma ou mais imagens para contexto multimodal, e o nó retorna a resposta de texto gerada pelo modelo.

## Entradas

As entradas são agrupadas em configurações comuns, configurações específicas do modelo, que aparecem quando um modelo é selecionado, e imagens de referência opcionais.

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo Claude usado para gerar a resposta. Selecionar um modelo revela as configurações específicas abaixo. | DYNAMIC_COMBO | Sim | `"Opus 5"`<br>`"Opus 4.8"`<br>`"Fable 5"`<br>`"Sonnet 5"`<br>`"Opus 4.7"`<br>`"Opus 4.6"`<br>`"Sonnet 4.6"`<br>`"Sonnet 4.5"`<br>`"Haiku 4.5"` |
| `prompt` | Entrada de texto para o modelo. (padrão: string vazia) | STRING | Sim | N/A |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 0) | INT | Sim | 0 a 2147483647 |
| `system_prompt` | Instruções fundamentais que determinam o comportamento do modelo. (padrão: string vazia) | STRING | Não | N/A |

### Entradas do Opus 5 e Fable 5

Esses dois modelos compartilham as mesmas configurações. Eles não expõem uma configuração de temperatura, e o raciocínio está sempre ativado.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Número máximo de tokens a gerar (inclui tokens de raciocínio quando ativado). (padrão: 32768) | INT | Sim | 4096 a 64000 |
| `reasoning_effort` | Esforço de pensamento estendido. O raciocínio está sempre ativado para este modelo. (padrão: "high") | COMBO | Sim | `"low"`<br>`"medium"`<br>`"high"` |

### Entradas do Opus 4.8 e Sonnet 5

Esses dois modelos compartilham as mesmas configurações. Eles não expõem uma configuração de temperatura.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Número máximo de tokens a gerar (inclui tokens de raciocínio quando ativado). (padrão: 32768) | INT | Sim | 4096 a 64000 |
| `reasoning_effort` | Esforço de pensamento estendido. `"off"` desativa o raciocínio. (padrão: "off") | COMBO | Sim | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Entradas do Opus 4.7, Opus 4.6, Sonnet 4.6 e Sonnet 4.5

Esses quatro modelos compartilham as mesmas configurações.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Número máximo de tokens a gerar (inclui tokens de raciocínio quando ativado). (padrão: 32768) | INT | Sim | 4096 a 64000 |
| `temperature` | Controla a aleatoriedade. 0.0 é determinístico, 1.0 é o mais aleatório. Ignorado para Opus 4.7 e para qualquer modelo quando `reasoning_effort` está definido. (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `reasoning_effort` | Esforço de pensamento estendido. `"off"` desativa o raciocínio. (padrão: "off") | COMBO | Sim | `"off"`<br>`"low"`<br>`"medium"`<br>`"high"` |

### Entradas do Haiku 4.5

Este modelo não expõe uma configuração de `reasoning_effort`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `max_tokens` | Número máximo de tokens a gerar (inclui tokens de raciocínio quando ativado). (padrão: 32768) | INT | Sim | 4096 a 64000 |
| `temperature` | Controla a aleatoriedade. 0.0 é determinístico, 1.0 é o mais aleatório. Ignorado para Opus 4.7 e para qualquer modelo quando `reasoning_effort` está definido. (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagens` | Imagem(ns) opcional(is) para usar como contexto do modelo. Até 20 imagens. Slot expansível: conecte de 1 a 20 itens (`image_1` ... `image_20`). | IMAGE | Não | 0 a 20 imagens |

### Restrições dos Parâmetros

- **Limite de imagens:** No máximo 20 imagens podem ser fornecidas por solicitação. Conectar mais de 20 imagens gera um erro.
- **Prompt obrigatório:** O prompt deve conter pelo menos um caractere que não seja espaço em branco. Um prompt vazio gera um erro de validação.
- **Tratamento da temperatura:** Quando o pensamento está ativado, a API da Anthropic exige que a temperatura não seja definida (ela assume o padrão 1.0). Opus 5, Opus 4.8, Fable 5 e Sonnet 5 não expõem uma configuração de temperatura. Opus 4.7 ignora `temperature`, e qualquer modelo com `reasoning_effort` definido como `"low"`, `"medium"` ou `"high"` também a ignora.
- **Comportamento de raciocínio/pensamento:** A configuração `reasoning_effort` controla se o pensamento está habilitado. Opus 5 e Fable 5 sempre têm o raciocínio habilitado. Haiku 4.5 não suporta raciocínio. Quando o pensamento está habilitado, o nó usa o modo de pensamento apropriado para o modelo selecionado, seja adaptativo ou baseado em orçamento. No modo de orçamento, o orçamento de tokens de raciocínio é limitado para deixar pelo menos 1024 tokens para a resposta real.
- **Recusa de segurança:** Se o Claude se recusar a responder à solicitação por motivos de segurança, o nó gera um erro pedindo que você reformule o prompt ou tente um modelo diferente.
- **Texto de saída:** Blocos de pensamento e raciocínio não são incluídos na saída; apenas o texto gerado é retornado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A resposta de texto gerada pelo modelo Claude. Blocos de pensamento/raciocínio não são incluídos. Se nenhum texto for gerado, retorna "Empty response from Claude model." | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b0381e7981e5886d66b6976c7ddcad3f142bdd803271a6ac8567293dcddaa98a`
