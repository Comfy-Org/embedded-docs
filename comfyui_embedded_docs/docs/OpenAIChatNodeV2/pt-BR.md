# OpenAI ChatGPT

Este nó gera respostas de texto com os modelos GPT da OpenAI. Ele envia um prompt de texto e, opcionalmente, imagens ou arquivos como contexto, e retorna a resposta como uma string. Cada configuração fica dentro do seletor `model`: ao escolher um modelo, são exibidos os níveis de `reasoning_effort`, o limite de tokens, a seed e o prompt de sistema daquele modelo, portanto, nenhum nó de configuração separado é necessário. Este nó substitui o nó OpenAI ChatGPT anterior, que o código-fonte agora marca como descontinuado.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo usado para gerar a resposta. Cada modelo expõe os níveis de `reasoning_effort` que suporta (padrão: `"gpt-6.2-sol"`). | DYNAMIC_COMBO | Sim | `"gpt-6.2-sol"`<br>`"gpt-6.2-astra"`<br>`"gpt-6-astra"`<br>`"gpt-6.1-sol"`<br>`"gpt-6.1-terra"`<br>`"gpt-6-sol"`<br>`"gpt-6-luna"`<br>`"gpt-5.6-sol"`<br>`"gpt-5.6-terra"`<br>`"gpt-5.6-luna"`<br>`"gpt-5.5-pro"`<br>`"gpt-5.5"` |
| `prompt` | Entrada de texto para o modelo (padrão: string vazia). | STRING | Sim | - |
| `images` | Slot expansível: conecte 1..16 itens (`image_1`, `image_2`, ...). Imagem(ns) opcional(is) usada(s) como contexto para o modelo. | IMAGE | Não | 0 a 16 imagens |
| `files` | Arquivo(s) opcional(is) usado(s) como contexto para o modelo. Aceita entradas do nó OpenAI ChatGPT Input Files. | OPENAI_INPUT_FILES | Não | - |
| `reasoning_effort` | Quanto o modelo raciocina antes de responder. Níveis mais altos usam mais tokens e levam mais tempo. Os níveis oferecidos dependem do modelo selecionado (padrão: `"medium"`, `"high"` para `gpt-5.5-pro`). | COMBO | Sim | Consulte a lista por modelo abaixo |
| `max_output_tokens` | Máximo de tokens a gerar, incluindo tokens de raciocínio. Um valor baixo junto com um `reasoning_effort` alto pode não deixar espaço para a resposta (padrão: 32768). | INT | Sim | 16 a 128000 |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed (padrão: 42). | INT | Sim | 0 a 2147483647 |
| `system_prompt` | Instruções fundamentais que ditam o comportamento do modelo (padrão: string vazia). | STRING | Não | - |

### Níveis de esforço de raciocínio por modelo

- `gpt-6.2-sol`, `gpt-6.2-astra`, `gpt-6-astra`, `gpt-6.1-sol`: `"low"`, `"medium"`, `"high"`, `"xhigh"`, `"max"`, padrão `"medium"`.
- `gpt-6.1-terra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`: `"none"`, `"low"`, `"medium"`, `"high"`, `"xhigh"`, `"max"`, padrão `"medium"`.
- `gpt-5.5-pro`: `"medium"`, `"high"`, `"xhigh"`, padrão `"high"`.
- `gpt-5.5`: `"none"`, `"low"`, `"medium"`, `"high"`, `"xhigh"`, padrão `"medium"`.

### Notas sobre o comportamento

- Apenas o texto da resposta é retornado. Mensagens que o modelo emite em sua fase de comentários enquanto pensa são ignoradas.
- Se o orçamento de tokens acabar antes de a resposta ser escrita, o nó gera um erro informando que você deve aumentar `max_output_tokens`.
- As imagens são enviadas na própria resolução, com o nível de detalhe automático da API, então imagens grandes usam mais tokens.
- Toda solicitação é armazenada do lado da OpenAI, e o texto retornado une as partes da resposta com quebras de linha.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `output` | A resposta de texto gerada pelo modelo OpenAI. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatNodeV2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `129c13a6c7b76d142c0a23234ab5e707a1dd39a99055974277d46a39593aa7ba`
