# Bria FIBO 2.0 Image Generate

Gera uma nova imagem a partir de um prompt de texto, um prompt estruturado em JSON ou uma única imagem de referência usando o Bria FIBO 2.0. O nó envia a solicitação para a API da Bria, aguarda a conclusão da geração e retorna a imagem junto com um prompt estruturado que pode recriá-la ou refiná-la em uma execução posterior.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrição em linguagem natural da imagem a ser gerada (padrão: vazio). | STRING | Sim | Texto multilinha |
| `structured_prompt` | Prompt estruturado em JSON de um resultado anterior do Bria FIBO. Com o mesmo `seed`, recria essa imagem; altere o JSON ou adicione um prompt para refiná-la (padrão: vazio). | STRING | Sim | Texto multilinha |
| `aspect_ratio` | Proporção de aspecto da saída (padrão: `"1:1"`). As proporções a partir de `"16:10"` são tamanhos do FIBO 2.0 com requisitos extras, listados abaixo. | COMBO | Sim | `"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"16:10"`<br>`"10:16"`<br>`"2:1"`<br>`"1:2"`<br>`"21:9"`<br>`"9:21"`<br>`"3:1"`<br>`"1:3"`<br>`"4:1"`<br>`"1:4"`<br>`"5:1"`<br>`"1:5"` |
| `resolution` | Resolução da saída em megapixels (padrão: `"1MP"`). | COMBO | Sim | `"1MP"`<br>`"4MP"` |
| `seed` | Semente que inicializa a geração (padrão: 42). | INT | Sim | 1 a 2147483647 |
| `moderation` | Configurações de moderação. Selecionar `"true"` revela as entradas de moderação listadas abaixo. | DYNAMIC_COMBO | Sim | `"false"`<br>`"true"` |
| `image` | Imagem de referência opcional para servir de base. O resultado é uma nova imagem na proporção de aspecto selecionada, não uma edição desta imagem. | IMAGE | Não | - |

### Entradas de moderação

Quando `moderation` é definido como `"true"`, estas entradas adicionais ficam disponíveis:

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | Se o texto do prompt deve ser moderado; a solicitação falha quando a moderação o rejeita (padrão: false). | BOOLEAN | Não | `true`<br>`false` |
| `visual_input_moderation` | Se a imagem de referência deve ser moderada; a solicitação falha quando a moderação a rejeita (padrão: false). | BOOLEAN | Não | `true`<br>`false` |
| `visual_output_moderation` | Se a imagem gerada deve ser moderada; a solicitação falha quando a moderação a rejeita (padrão: false). | BOOLEAN | Não | `true`<br>`false` |

**Restrições importantes:**

- Forneça pelo menos um entre `prompt`, `structured_prompt` ou uma `image` de referência. Se todos os três estiverem vazios, o nó gera um erro.
- Uma imagem de referência não pode ser combinada com `structured_prompt`: use um ou outro.
- As proporções do FIBO 2.0 (`"16:10"`, `"10:16"`, `"2:1"`, `"1:2"`, `"21:9"`, `"9:21"`, `"3:1"`, `"1:3"`, `"4:1"`, `"1:4"`, `"5:1"`, `"1:5"`) exigem `resolution` `"1MP"` e exatamente um entre `prompt` ou `structured_prompt`.
- Este nó é um nó de API pago; o ComfyUI cobra aproximadamente 0,0572 USD por execução.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem gerada retornada pela API da Bria. | IMAGE |
| `structured_prompt` | Descrição estruturada da imagem gerada, para recriá-la ou refiná-la com este nó. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageGenerate/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4d53fe457e2e349ac41b5c8a0d3d5599eafa53cb653c470335853f1d4517688f`
