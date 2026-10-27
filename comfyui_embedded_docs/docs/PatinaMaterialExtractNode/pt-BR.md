# Patina Material Extract

Extrai um material PBR com repetição contínua e sem emendas de uma região de uma imagem de entrada, guiado por um prompt que nomeia o que deve ser extraído: uma parede, um piso, um tecido. Ele retorna a textura base extraída, além de até cinco mapas de material, com upscaling opcional dos mapas via SeedVR. Use-o para transformar a foto de uma superfície real em um material reutilizável e tileável.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem da qual extrair uma textura. | IMAGE | Sim | - |
| `prompt` | Descrição de qual textura extrair da imagem, por exemplo `"the wall"`. | STRING | Sim | Texto multilinha |
| `image_size` | Tamanho da textura de saída. `"custom"` revela as entradas `width` e `height`. Padrão: `"1:1 (1024x1024)"`. | DYNAMIC_COMBO | Sim | `"1:1 (1024x1024)"`<br>`"1:1 (512x512)"`<br>`"4:3 (1024x768)"`<br>`"3:4 (768x1024)"`<br>`"16:9 (1024x576)"`<br>`"9:16 (576x1024)"`<br>`"custom"` |
| `basecolor` | Gera o mapa basecolor (albedo). Padrão: True. | BOOLEAN | Sim | true<br>false |
| `normal` | Gera o mapa normal. Padrão: True. | BOOLEAN | Sim | true<br>false |
| `roughness` | Gera o mapa de rugosidade. Padrão: False. | BOOLEAN | Sim | true<br>false |
| `metalness` | Gera o mapa de metalicidade. Padrão: False. | BOOLEAN | Sim | true<br>false |
| `height` | Gera o mapa de altura (deslocamento). Padrão: False. | BOOLEAN | Sim | true<br>false |
| `upscale_factor` | Upscaling contínuo e sem emendas dos mapas PBR com SeedVR. A textura base não passa por upscaling, e 4x transforma um mapa de 2048 pixels em um de 8K. Padrão: 0 (desativado). | INT | Sim | 0 a 4 (passo 2) |
| `seed` | Semente para geração reproduzível. Padrão: 42. | INT | Sim | 0 a 2147483646 |
| `strength` | Quanto transformar a imagem de entrada. Configuração avançada. Padrão: 0.6. | FLOAT | Sim | 0.01 a 1.0 (passo 0.01) |
| `tiling_mode` | Direção do tiling: omnidirecional, horizontal ou vertical. Configuração avançada. Padrão: `"both"`. | COMBO | Sim | `"both"`<br>`"horizontal"`<br>`"vertical"` |
| `num_inference_steps` | Etapas de remoção de ruído para geração da textura. Configuração avançada. Padrão: 8. | INT | Sim | 1 a 8 |
| `tile_size` | Tamanho do tile no espaço latente, em que 64 significa 512 pixels e 128 significa 1024 pixels. Configuração avançada. Padrão: 128. | INT | Sim | 32 a 256 (passo 2) |
| `tile_stride` | Passo (stride) do tile no espaço latente. Configuração avançada. Padrão: 64. | INT | Sim | 16 a 128 (passo 2) |
| `prompt_expansion` | Expande o prompt com um modelo de linguagem para obter detalhes de textura mais ricos. Desativado por padrão, porque a expansão reformula o prompt como uma fotografia e tende a esmaecer o mapa de metalicidade. Configuração avançada. | BOOLEAN | Sim | true<br>false |
| `safety_checker` | Executa a verificação de segurança de conteúdo do provedor na solicitação. Configuração avançada. Padrão: False. | BOOLEAN | Sim | true<br>false |

### Entradas de tamanho de imagem personalizado

Estas entradas aparecem quando `image_size` é definido como `"custom"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image_size.width` | Largura da textura em pixels. Padrão: 1024. | INT | Sim | 512 a 2048 (passo 16) |
| `image_size.height` | Altura da textura em pixels. Padrão: 1024. | INT | Sim | 512 a 2048 (passo 16) |

**Restrições e comportamento:**

* Pelo menos um mapa de material deve estar habilitado; caso contrário, a execução falha.
* O prompt é obrigatório e não pode estar vazio; nomeie a região a ser extraída com a maior precisão possível.
* Um resultado em 8K vem do upscaling 4x dos mapas de uma renderização de 2048 pixels, e não de uma única geração em 8K.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `texture` | A textura base extraída, sem nenhum mapa aplicado. | IMAGE |
| `basecolor` | O mapa basecolor (albedo), ou um placeholder 1x1 quando esse mapa está desabilitado. | IMAGE |
| `normal` | O mapa normal, ou um placeholder 1x1 quando esse mapa está desabilitado. | IMAGE |
| `roughness` | O mapa de rugosidade, ou um placeholder 1x1 quando esse mapa está desabilitado. | IMAGE |
| `metalness` | O mapa de metalicidade, ou um placeholder 1x1 quando esse mapa está desabilitado. | IMAGE |
| `height` | O mapa de altura (deslocamento), ou um placeholder 1x1 quando esse mapa está desabilitado. | IMAGE |
| `expanded_prompt` | O prompt que o provedor realmente usou, que difere da entrada apenas quando `prompt_expansion` está habilitado. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PatinaMaterialExtractNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `484b8eaa57388541e352cd88c8998c63aa0b2a99d98cd8e602252625064f16ba`
