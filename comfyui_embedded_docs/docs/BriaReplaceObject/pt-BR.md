# BriaReplaceObject

Substitui um objeto em uma imagem por outro descrito em texto simples, usando a edição de imagem guiada por texto da Bria. A Bria renderiza novamente o quadro inteiro em cerca de 1 megapixel, portanto o resultado não fica alinhado pixel a pixel com a entrada.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | A imagem que contém o objeto a ser substituído. O canal alfa é descartado antes de a imagem ser enviada. | IMAGE | Sim | - |
| `instrução` | O que substituir e por o quê, como "Substitua a maçã vermelha por uma pera verde". Deve ter pelo menos 1 caractere. | STRING | Sim | Texto multilinha; padrão: "" (vazio) |
| `semente` | A Bria não usa seed aqui e recria a edição a cada chamada, portanto execuções repetidas podem diferir. O valor nunca é enviado: ele apenas altera a chave de cache deste nó, de modo que um grafo de outro modo idêntico execute a edição novamente em vez de retornar o resultado em cache. | INT | Sim | 0 a 2147483647, passo 1; padrão: 42; controle após gerar habilitado |

### Entradas de moderação

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `moderação` | Configurações de moderação. Selecionar `"true"` revela as subopções de moderação abaixo, que de outra forma não são exibidas. | DYNAMIC_COMBO | Sim | `"false"`<br>`"true"` |
| `visual_input_moderation` | Habilita a moderação da imagem de entrada. Disponível apenas quando `moderation` está definido como `"true"`. | BOOLEAN | Não | `true` / `false`; padrão: false |
| `visual_output_moderation` | Habilita a moderação da imagem de saída gerada. Disponível apenas quando `moderation` está definido como `"true"`. | BOOLEAN | Não | `true` / `false`; padrão: false |

Observação: `instruction` é validado antes de a solicitação ser enviada e deve conter pelo menos 1 caractere. O valor de `seed` não é transmitido à Bria; ele só afeta se o nó reexecuta a edição ou retorna um resultado em cache.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `image` | A imagem editada com a substituição de objeto descrita aplicada. | IMAGE |
| `structured_prompt` | Descrição estruturada da imagem editada, para uma edição posterior com Bria FIBO Image Edit. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReplaceObject/pt-BR.md)

---
**Source fingerprint (SHA-256):** `75a45d5c0d6cde96a1e961db627edc1a59c07cc37b974402745cefc62864cc26`
