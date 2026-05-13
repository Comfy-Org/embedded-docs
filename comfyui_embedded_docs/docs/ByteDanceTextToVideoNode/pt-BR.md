> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/pt-BR.md)

O nó ByteDance Text to Video gera vídeos usando modelos ByteDance por meio de uma API baseada em prompts de texto. Ele recebe uma descrição textual e várias configurações de vídeo como entrada e, em seguida, cria um vídeo que corresponde às especificações fornecidas. O nó gerencia a comunicação com a API e retorna o vídeo gerado como saída.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | STRING | Sim | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-t2v-250428"`<br>`"seedance-1-0-pro-fast-251015"` | O modelo ByteDance a ser usado para geração (padrão: `"seedance-1-0-pro-fast-251015"`). |
| `prompt` | STRING | Sim | - | O prompt de texto usado para gerar o vídeo. |
| `resolution` | STRING | Sim | `"480p"`<br>`"720p"`<br>`"1080p"` | A resolução do vídeo de saída. |
| `aspect_ratio` | STRING | Sim | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` | A proporção de aspecto do vídeo de saída. |
| `duration` | INT | Sim | 3 a 12 | A duração do vídeo de saída em segundos (padrão: 5). |
| `seed` | INT | Não | 0 a 2147483647 | Semente a ser usada para geração (padrão: 0). |
| `camera_fixed` | BOOLEAN | Não | - | Especifica se a câmera deve ser fixada. A plataforma anexa uma instrução para fixar a câmera ao seu prompt, mas não garante o efeito real (padrão: Falso). |
| `watermark` | BOOLEAN | Não | - | Se deve adicionar uma marca d'água "gerado por IA" ao vídeo (padrão: Falso). |
| `generate_audio` | BOOLEAN | Não | - | Este parâmetro é ignorado para todos os modelos, exceto `seedance-1-5-pro-251215` (padrão: Falso). |

**Restrições dos Parâmetros:**

- O parâmetro `prompt` deve conter pelo menos 1 caractere após a remoção de espaços em branco.
- O parâmetro `prompt` não pode conter os seguintes parâmetros de texto: "resolution", "ratio", "duration", "seed", "camerafixed", "watermark".
- O parâmetro `duration` é limitado a valores entre 3 e 12 segundos. Para o modelo `seedance-1-5-pro-251215`, a duração mínima suportada é de 4 segundos.
- O parâmetro `seed` aceita valores de 0 a 2.147.483.647.
- O parâmetro `generate_audio` só tem efeito quando o `model` está definido como `seedance-1-5-pro-251215`; ele é ignorado para todos os outros modelos.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O arquivo de vídeo gerado |

---
**Source fingerprint (SHA-256):** `44ea3e40b99b337340cc39be1c5b6c903680591f1de49b1f2e82f398979355c5`
