# Tencent HY

Este nó gera respostas de texto com o modelo Hy4 da Tencent. Ele envia um prompt de texto e, opcionalmente, uma ou mais imagens como contexto, e retorna a resposta do modelo como texto.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo usado para gerar a resposta. Selecioná-lo revela suas entradas abaixo. Padrão: `"Hy4"`. | DYNAMIC_COMBO | Sim | `"Hy4"` |

### Entradas do Hy4

Estas entradas aparecem quando `model` está definido como `"Hy4"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | A mensagem a ser enviada ao modelo. Não deve estar vazia. Padrão: "" (string vazia). | STRING | Sim | Pelo menos 1 caractere |
| `images` | Até 20 imagens. Cada imagem em um lote conta. Padrão: nenhuma imagem. | AUTOGROW | Não | 0 a 20 imagens |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |
| `system_prompt` | Instruções fundamentais que ditam o comportamento do modelo. Padrão: "" (string vazia). | STRING | Não | - |
| `reasoning` | O modelo pensa antes de responder. As respostas demoram mais e usam mais tokens, e tarefas muito difíceis podem atingir o tempo limite. Padrão: False. | BOOLEAN | Sim | true<br>false |
| `temperature` | Controla a aleatoriedade. Os resultados ainda variam em 0. Padrão: 1.0. | FLOAT | Sim | 0.0 a 1.4 (passo: 0.01) |
| `max_tokens` | Número máximo de tokens a gerar, incluindo tokens de raciocínio quando `reasoning` está ativado. Respostas muito longas podem atingir o tempo limite. Padrão: 32000. | INT | Sim | 1 a 64000 |

**Restrições:**

* No máximo 20 imagens são aceitas por solicitação, contando cada imagem de um lote.
* O filtro de conteúdo da Tencent pode bloquear uma solicitação, o que gera um erro.
* Se `max_tokens` se esgotar antes de a resposta terminar, o nó gera um erro: aumente `max_tokens` ou desative `reasoning`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `STRING` | A resposta de texto do modelo Hy4. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TencentHyNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c7c1d2908d2fba8172fa279b7d273f5f3f96cf10b531f81650824fc8e0176f21`
