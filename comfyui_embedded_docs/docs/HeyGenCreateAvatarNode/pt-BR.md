# HeyGenCreateAvatarNode

Crie um avatar HeyGen reutilizável a partir de uma foto de uma pessoa ou de um prompt de texto que descreva um personagem a ser gerado. O ID do avatar resultante pode ser usado com o nó HeyGen Avatar Video para criar vídeos com este avatar.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `source` | Gere um novo personagem a partir de um prompt de texto ou crie o avatar a partir de uma foto conectada de uma pessoa. | COMBO | Sim | `"prompt"`<br>`"photo"` |

Quando `source` estiver definido como `"prompt"`, os seguintes parâmetros adicionais ficam disponíveis:

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrição do avatar a ser gerado (até 1000 caracteres). | STRING | Sim | 1 a 1000 caracteres |
| `reference_images` | Até 3 imagens de referência para orientar a aparência gerada. | IMAGE | Não | 0 a 3 imagens |

Quando `source` estiver definido como `"photo"`, o seguinte parâmetro adicional fica disponível:

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `identity_photo` | Foto da pessoa a ser transformada em avatar. Redimensionada automaticamente se for maior que 2K. | IMAGE | Sim | Imagem única |

**Observação:** O parâmetro `source` alterna entre dois modos. No modo `"prompt"`, você fornece uma descrição em texto e, opcionalmente, até 3 imagens de referência. No modo `"photo"`, você fornece uma única foto de uma pessoa. Esses modos são mutuamente exclusivos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `avatar_id` | ID da aparência do avatar. Passe-o para o campo `custom_avatar_id` do nó HeyGen Avatar Video; salve-o para reutilizar o avatar posteriormente. | STRING |
| `preview` | Imagem de pré-visualização do avatar gerado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenCreateAvatarNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c60e9cdb0d91fb5ec6ea83b503b9aa10c978ce065a16c751a52e90c12e70a5e2`
