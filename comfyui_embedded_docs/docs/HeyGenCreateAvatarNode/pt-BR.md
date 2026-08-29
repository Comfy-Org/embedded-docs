# Criar Avatar HeyGen

Crie um avatar HeyGen reutilizável a partir de uma foto de uma pessoa ou de um prompt de texto que descreva um personagem a ser gerado. O `avatar_id` resultante pode ser usado com o nó HeyGen Avatar Video e deve ser salvo para reutilizar o avatar em fluxos de trabalho futuros.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `origem` | Gere um novo personagem a partir de um prompt de texto ou crie o avatar a partir de uma foto conectada de uma pessoa. | DYNAMIC_COMBO | Sim | `"prompt"`<br>`"photo"` |

### Entradas de prompt

Disponíveis quando `source` está definido como `"prompt"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrição do avatar a ser gerado (até 1000 caracteres). Deve conter pelo menos 1 caractere que não seja espaço em branco. Padrão: string vazia. | STRING | Sim | 1 a 1000 caracteres |

### Entradas de foto

Disponíveis quando `source` está definido como `"photo"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `identity_photo` | Foto da pessoa que será transformada em avatar. Redimensionada automaticamente se for maior que 2K. | IMAGE | Sim | Imagem única |

### Entradas de referência

Disponíveis quando `source` está definido como `"prompt"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slot expansível: conecte até 3 imagens (`ref_image_1`...`ref_image_3`) que orientam a aparência gerada. As imagens são redimensionadas automaticamente se forem maiores que 2K. | IMAGE | Não | 0 a 3 imagens |

**Nota:** O parâmetro `source` alterna entre dois modos mutuamente exclusivos. No modo `"prompt"`, `prompt` é obrigatório e até 3 imagens de referência podem ser conectadas opcionalmente. No modo `"photo"`, `identity_photo` é obrigatório. Fotos e imagens de referência são redimensionadas automaticamente quando maiores que 2K; mais de 3 imagens de referência não são aceitas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `avatar_id` | ID da aparência do avatar. Passe-o para `custom_avatar_id` do HeyGen Avatar Video; salve-o para reutilizar o avatar posteriormente. | STRING |
| `prévia` | Imagem de pré-visualização do avatar gerado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenCreateAvatarNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3669686fc6d089909bd5d2d75292ceef05702ed3cc7b14e561bcb444c30a4e63`
