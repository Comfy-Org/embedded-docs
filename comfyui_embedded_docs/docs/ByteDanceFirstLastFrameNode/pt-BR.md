> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/pt-BR.md)

Este nó gera um vídeo usando um prompt de texto juntamente com imagens do primeiro e último quadro. Ele utiliza sua descrição e os dois quadros-chave para criar uma sequência de vídeo completa que faz a transição entre eles. O nó oferece várias opções para controlar a resolução, proporção de aspecto, duração e outros parâmetros de geração do vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | COMBO | Sim | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-i2v-250428"` | O modelo a ser usado para geração de vídeo (padrão: `"seedance-1-0-lite-i2v-250428"`). |
| `prompt` | STRING | Sim | - | O prompt de texto usado para gerar o vídeo. |
| `first_frame` | IMAGE | Sim | - | Primeiro quadro a ser usado no vídeo. Deve ter entre 300x300 e 6000x6000 pixels, com proporção de aspecto entre 0,4 e 2,5. |
| `last_frame` | IMAGE | Sim | - | Último quadro a ser usado no vídeo. Deve ter entre 300x300 e 6000x6000 pixels, com proporção de aspecto entre 0,4 e 2,5. |
| `resolution` | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"` | A resolução do vídeo de saída. |
| `aspect_ratio` | COMBO | Sim | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` | A proporção de aspecto do vídeo de saída (padrão: `"adaptive"`). |
| `duration` | INT | Sim | 3 - 12 | A duração do vídeo de saída em segundos (padrão: 5). Nota: Para o modelo `seedance-1-5-pro-251215`, a duração mínima suportada é de 4 segundos. |
| `seed` | INT | Não | 0 - 2147483647 | Semente a ser usada para geração (padrão: 0). |
| `camera_fixed` | BOOLEAN | Não | - | Especifica se a câmera deve ser fixada. A plataforma anexa uma instrução para fixar a câmera ao seu prompt, mas não garante o efeito real (padrão: False). |
| `watermark` | BOOLEAN | Não | - | Se deve adicionar uma marca d'água "Gerado por IA" ao vídeo (padrão: False). |
| `generate_audio` | BOOLEAN | Não | - | Este parâmetro é ignorado para qualquer modelo, exceto `seedance-1-5-pro-251215` (padrão: False). |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O arquivo de vídeo gerado |

---
**Source fingerprint (SHA-256):** `2da7b8ad2bc818a21988c028155ba2b466452a1655ac506fcef01c143dda7450`
