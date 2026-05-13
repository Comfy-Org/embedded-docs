> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode/pt-BR.md)

Gera imagens de forma síncrona com base em um prompt de texto e proporção de aspecto. Este nó cria imagens usando descrições textuais e permite controlar as dimensões e o estilo da imagem por meio de várias entradas de referência, incluindo imagens de personagem e estilo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | - | Prompt para a geração da imagem (padrão: string vazia). Deve ter pelo menos 3 caracteres. |
| `model` | COMBO | Sim | `photon-flash-1`<br>`photon-1`<br>`photon` | Seleção do modelo para geração de imagem. Modelos diferentes têm custos diferentes. |
| `aspect_ratio` | COMBO | Sim | `16:9`<br>`1:1`<br>`4:3`<br>`3:2`<br>`21:9`<br>`9:16`<br>`3:4`<br>`2:3`<br>`9:21` | Proporção de aspecto para a imagem gerada (padrão: `16:9`) |
| `seed` | INT | Sim | 0 a 18446744073709551615 | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0) |
| `style_image_weight` | FLOAT | Não | 0.0 a 1.0 | Peso da imagem de estilo. Ignorado se nenhum `style_image` for fornecido (padrão: 1.0) |
| `image_luma_ref` | LUMA_REF | Não | - | Conexão do nó de Referência Luma para influenciar a geração com imagens de entrada; até 4 imagens podem ser consideradas. |
| `style_image` | IMAGE | Não | - | Imagem de referência de estilo; apenas 1 imagem será usada. |
| `character_image` | IMAGE | Não | - | Imagens de referência de personagem; pode ser um lote de múltiplas, até 4 imagens podem ser consideradas. |

**Restrições dos Parâmetros:**

- O `prompt` deve ter pelo menos 3 caracteres após a remoção de espaços em branco.
- O parâmetro `image_luma_ref` pode aceitar até 4 imagens de referência.
- O parâmetro `character_image` pode aceitar até 4 imagens de referência de personagem.
- O parâmetro `style_image` aceita apenas 1 imagem de referência de estilo.
- O parâmetro `style_image_weight` é usado apenas quando `style_image` é fornecido.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `output` | IMAGE | A imagem gerada com base nos parâmetros de entrada. |

---
**Source fingerprint (SHA-256):** `f7878cd4df62c2f364e4e404215b18bf2f5745fb071ae2cd931d5e34b84eab46`
