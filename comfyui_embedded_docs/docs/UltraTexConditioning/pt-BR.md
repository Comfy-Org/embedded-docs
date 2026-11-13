# UltraTex Conditioning

Condiciona o FLUX.2 Klein 9B com o UltraTex LoRA para aplicar a aparência de uma imagem de referência a uma malha, como uma imagem por visualização. Renderize as visualizações com Render Mesh no modo `world normal`, a partir de um Create Camera Orbit com 4, mais topo e base, e faça o bake do resultado com Bake Texture From Views.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `conditioning` | Condicionamento de texto. O UltraTex foi treinado com um prompt vazio. | CONDITIONING | Sim | - |
| `vae` | VAE usado para codificar as normais, as visualizações e a referência. | VAE | Sim | - |
| `normals` | Imagens `world normal` do Render Mesh: as 6 visualizações canônicas ou as 4 visualizações laterais. | IMAGE | Sim | - |
| `masks` | Máscaras do Render Mesh das mesmas visualizações, uma por visualização. | MASK | Sim | - |
| `reference` | O objeto como ele deve parecer, visto do lado da câmera frontal. | IMAGE | Sim | - |
| `reference_mask` | Máscara do objeto da referência, branca para o objeto. Padrão: totalmente branco. | MASK | Não | - |
| `extra_views` | Mais referências: o objeto visto das outras visualizações, cada uma vinculada à sua visualização assim como a referência está vinculada à frontal. Padrão: `"off"`. | DYNAMIC_COMBO | Sim | `"off"`<br>`"on"` |

### Entradas de Visualizações Extras "on"

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `right` | O objeto visto da visualização direita. | IMAGE | Não | - |
| `back` | O objeto visto da visualização traseira. | IMAGE | Não | - |
| `left` | O objeto visto da visualização esquerda. | IMAGE | Não | - |
| `top` | O objeto visto da visualização superior. | IMAGE | Não | - |
| `bottom` | O objeto visto da visualização inferior. | IMAGE | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `conditioning` | Condicionamento que carrega a grade de visualizações, os latentes de referência e as máscaras de tokens de que o UltraTex precisa. | CONDITIONING |

Nota: `normals` deve conter as 6 visualizações canônicas (Create Camera Orbit com `count` 4 e `poles` topo e base) ou as 4 visualizações laterais, e `masks` deve corresponder à contagem de visualizações.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UltraTexConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5b05f5151d4c12394ef893db69538adaef86e9cbdbb118a37c20919758520b6f`
