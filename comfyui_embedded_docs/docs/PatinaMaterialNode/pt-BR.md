# Patina Material

Gera um material PBR completo e com tiling perfeito a partir de uma descrição textual: uma textura base mais até cinco mapas de material, com upscaling opcional via SeedVR dos mapas. Uma imagem de entrada pode conduzir o resultado como uma passada de image-to-image, e uma imagem de entrada com máscara transforma o processo em uma passada de inpaint. Use-o para produzir superfícies prontas para jogos ou para 3D sem digitalizar um material real.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrição do material ou da textura a ser gerada. | STRING | Sim | Texto multilinha |
| `image_size` | Tamanho da textura de saída. `"custom"` revela as entradas `width` e `height`. Padrão: `"1:1 (1024x1024)"`. | DYNAMIC_COMBO | Sim | `"1:1 (1024x1024)"`<br>`"1:1 (512x512)"`<br>`"4:3 (1024x768)"`<br>`"3:4 (768x1024)"`<br>`"16:9 (1024x576)"`<br>`"9:16 (576x1024)"`<br>`"custom"` |
| `basecolor` | Gera o mapa de cor base (albedo). Padrão: True. | BOOLEAN | Sim | true<br>false |
| `normal` | Gera o mapa de normais. Padrão: True. | BOOLEAN | Sim | true<br>false |
| `roughness` | Gera o mapa de rugosidade. Padrão: False. | BOOLEAN | Sim | true<br>false |
| `metalness` | Gera o mapa de metalicidade. Padrão: False. | BOOLEAN | Sim | true<br>false |
| `height` | Gera o mapa de altura (deslocamento). Padrão: False. | BOOLEAN | Sim | true<br>false |
| `upscale_factor` | Upscaling SeedVR sem emendas dos mapas PBR. A textura base não passa por upscaling, e 4x transforma um mapa de 2048 pixels em um de 8K. Padrão: 0 (desativado). | INT | Sim | 0 a 4 (passo 2) |
| `seed` | Semente para geração reproduzível. Padrão: 42. | INT | Sim | 0 a 2147483646 |
| `tiling_mode` | Direção do tiling: omnidirecional, horizontal ou vertical. Configuração avançada. Padrão: `"both"`. | COMBO | Sim | `"both"`<br>`"horizontal"`<br>`"vertical"` |
| `num_inference_steps` | Etapas de denoising para geração de textura. Configuração avançada. Padrão: 8. | INT | Sim | 1 a 8 |
| `tile_size` | Tamanho do tile no espaço latente, em que 64 significa 512 pixels e 128 significa 1024 pixels. Configuração avançada. Padrão: 128. | INT | Sim | 32 a 256 (passo 2) |
| `tile_stride` | Stride do tile no espaço latente. Configuração avançada. Padrão: 64. | INT | Sim | 16 a 128 (passo 2) |
| `image` | Imagem de origem opcional. Sozinha, executa image-to-image; junto com uma máscara, executa uma passada de inpaint. | IMAGE | Não | - |
| `mask` | Máscara de inpaint opcional; requer uma imagem de entrada. Áreas brancas são regeneradas e áreas pretas são mantidas. | MASK | Não | - |
| `strength` | Quanto transformar a imagem de entrada. Usado apenas quando uma imagem está conectada. Configuração avançada. Padrão: 0.6. | FLOAT | Sim | 0.01 a 1.0 (passo 0.01) |
| `prompt_expansion` | Expande o prompt com um modelo de linguagem para obter mais detalhes na textura. Desativado por padrão, porque a expansão reformula o prompt como uma fotografia e tende a esmaecer o mapa de metalicidade. Configuração avançada. | BOOLEAN | Sim | true<br>false |
| `safety_checker` | Executa a verificação de segurança de conteúdo do provedor na solicitação. Configuração avançada. Padrão: False. | BOOLEAN | Sim | true<br>false |

### Entradas de tamanho de imagem personalizado

Estas entradas aparecem quando `image_size` está definido como `"custom"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image_size.width` | Largura da textura em pixels. Padrão: 1024. | INT | Sim | 512 a 2048 (passo 16) |
| `image_size.height` | Altura da textura em pixels. Padrão: 1024. | INT | Sim | 512 a 2048 (passo 16) |

**Restrições e comportamento:**

* É permitido não habilitar nenhum mapa de material: nesse caso, o nó retorna apenas a textura base, e cada saída de mapa permanece como um placeholder 1x1.
* Uma máscara requer uma imagem de entrada; uma máscara sozinha gera um erro.
* Um resultado 8K vem do upscaling 4x dos mapas de uma renderização de 2048 pixels, não de uma única geração 8K.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `texture` | A textura base do material, sem nenhum mapa aplicado. | IMAGE |
| `basecolor` | O mapa de cor base (albedo), ou um placeholder 1x1 quando esse mapa está desativado. | IMAGE |
| `normal` | O mapa de normais, ou um placeholder 1x1 quando esse mapa está desativado. | IMAGE |
| `roughness` | O mapa de rugosidade, ou um placeholder 1x1 quando esse mapa está desativado. | IMAGE |
| `metalness` | O mapa de metalicidade, ou um placeholder 1x1 quando esse mapa está desativado. | IMAGE |
| `height` | O mapa de altura (deslocamento), ou um placeholder 1x1 quando esse mapa está desativado. | IMAGE |
| `expanded_prompt` | O prompt que o provedor realmente usou, que difere da entrada apenas quando `prompt_expansion` está habilitado. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaMaterialNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4e8305fa56a29dce72c54de12ae05207e8de39a1fea1f4753906c26e8af60383`
