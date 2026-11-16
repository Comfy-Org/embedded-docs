# Bria Remover Fundo da Imagem

Este nó remove o fundo de uma imagem usando o serviço Bria RMBG 2.0 ou RMBG 3.0. Ele envia a imagem para uma API externa para processamento e retorna o resultado com o fundo removido.

## Entradas

O seletor `moderation` revela opções adicionais de moderação quando definido como `"true"`.

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | A imagem de entrada da qual o fundo será removido. | IMAGE | Sim | - |
| `moderação` | Configurações de moderação. Quando definido como `"true"`, opções adicionais de moderação ficam disponíveis. | DYNAMIC_COMBO | Sim | `"false"`<br>`"true"` |
| `semente` | A seed controla se o nó deve ser executado novamente; a mesma imagem sempre dá o mesmo resultado independentemente da seed. Padrão: `0`. | INT | Sim | 0 a 2147483647 |
| `model` | Modelo de remoção de fundo. `"RMBG2"` é o padrão; `"RMBG3"` usa o modelo mais recente Bria RMBG 3.0. | COMBO | Não | `"RMBG2"`<br>`"RMBG3"` |

### Entradas de moderação "true"

Esses parâmetros aparecem somente quando `moderation` está definido como `"true"`. A opção `"false"` não adiciona entradas adicionais.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Habilita a moderação de conteúdo visual na imagem de entrada. Padrão: `False`. | BOOLEAN | Não | - |
| `visual_output_moderation` | Habilita a moderação de conteúdo visual na imagem de saída. Padrão: `True`. | BOOLEAN | Não | - |

**Nota:** Os parâmetros `visual_input_moderation` e `visual_output_moderation` dependem do parâmetro `moderation`. Eles só ficam ativos quando `moderation` está definido como `"true"`.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `image` | A imagem processada com o fundo removido. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/pt-BR.md)

---
**Source fingerprint (SHA-256):** `82f7ec2ac2d1579a3da009b464bce7c56fa2d7b1f599744d6158177ecd462cb2`
