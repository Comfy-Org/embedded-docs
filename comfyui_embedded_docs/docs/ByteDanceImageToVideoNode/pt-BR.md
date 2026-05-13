> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/pt-BR.md)

O nó ByteDance Image to Video gera vídeos usando modelos ByteDance por meio de uma API com base em uma imagem de entrada e um prompt de texto. Ele recebe um quadro de imagem inicial e cria uma sequência de vídeo que segue a descrição fornecida. O nó oferece várias opções de personalização para resolução do vídeo, proporção de aspecto, duração e outros parâmetros de geração.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | STRING | Sim | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-i2v-250428"`<br>`"seedance-1-0-pro-fast-251015"` | O modelo ByteDance a ser usado para geração de vídeo (padrão: `"seedance-1-0-pro-fast-251015"`). |
| `prompt` | STRING | Sim | - | O prompt de texto usado para gerar o vídeo. Deve ter pelo menos 1 caractere após remover espaços em branco. |
| `imagem` | IMAGE | Sim | - | Primeiro quadro a ser usado para o vídeo. Deve ter entre 300x300 e 6000x6000 pixels, com proporção de aspecto entre 0,4 e 2,5. |
| `resolução` | STRING | Sim | `"480p"`<br>`"720p"`<br>`"1080p"` | A resolução do vídeo de saída. |
| `proporção` | STRING | Sim | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` | A proporção de aspecto do vídeo de saída. |
| `duração` | INT | Sim | 3 - 12 | A duração do vídeo de saída em segundos (padrão: 5). Para o modelo `seedance-1-5-pro-251215`, a duração mínima suportada é de 4 segundos. |
| `semente` | INT | Não | 0 - 2147483647 | Semente a ser usada para geração (padrão: 0). |
| `câmera fixa` | BOOLEAN | Não | - | Especifica se a câmera deve ser fixada. A plataforma adiciona uma instrução para fixar a câmera ao seu prompt, mas não garante o efeito real (padrão: Falso). |
| `marca d'água` | BOOLEAN | Não | - | Se deve adicionar uma marca d'água "gerado por IA" ao vídeo (padrão: Falso). |
| `generate_audio` | BOOLEAN | Não | - | Este parâmetro é ignorado para qualquer modelo, exceto `seedance-1-5-pro-251215` (padrão: Falso). |

**Observação:** O prompt não deve conter as seguintes palavras (sem distinção entre maiúsculas e minúsculas): `resolution`, `ratio`, `duration`, `seed`, `camerafixed`, `watermark`. Esses parâmetros são definidos por meio de suas entradas dedicadas.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O arquivo de vídeo gerado com base na imagem de entrada e nos parâmetros do prompt. |

---
**Source fingerprint (SHA-256):** `e47e14c69f4bdf4921a5a5eaec20fb775473483e80cdd9dd6700d2c7f9219e65`
