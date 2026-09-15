# ByteDance Primeiro-Último-Frame para Vídeo

Este nó gera um vídeo usando um prompt de texto junto com imagens do primeiro e do último quadro. Ele utiliza sua descrição e os dois quadros-chave para criar uma sequência de vídeo completa que faz a transição entre eles. O nó oferece várias opções para controlar a resolução, a proporção de aspecto, a duração e outros parâmetros de geração do vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo usado para geração de vídeo (padrão: `"seedance-1-5-pro-251215"`). | COMBO | Sim | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"` |
| `prompt` | O prompt de texto usado para gerar o vídeo. Não deve estar vazio e não deve conter palavras-chave de parâmetros reservadas (`resolution`, `ratio`, `duration`, `seed`, `camerafixed`, `watermark`). | STRING | Sim | - |
| `first_frame` | Primeiro quadro a ser usado para o vídeo. Deve ter entre 300x300 e 6000x6000 pixels, com uma proporção de aspecto entre 0,4 e 2,5. | IMAGE | Sim | - |
| `last_frame` | Último quadro a ser usado para o vídeo. Deve ter entre 300x300 e 6000x6000 pixels, com uma proporção de aspecto entre 0,4 e 2,5. | IMAGE | Sim | - |
| `resolution` | A resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | A proporção de aspecto do vídeo de saída. | COMBO | Sim | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duration` | A duração do vídeo de saída em segundos. Ao usar `seedance-1-5-pro-251215`, a duração mínima é de 4 segundos. (padrão: 5) | INT | Sim | 3 - 12 |
| `seed` | Semente a ser usada para geração. (padrão: 0) | INT | Não | 0 - 2147483647 |
| `camera_fixed` | Especifica se a câmera deve ser fixada. A plataforma acrescenta uma instrução para fixar a câmera ao seu prompt, mas não garante o efeito real. (padrão: False) | BOOLEAN | Não | - |
| `watermark` | Se deve adicionar uma marca d'água "AI generated" ao vídeo. (padrão: False) | BOOLEAN | Não | - |
| `generate_audio` | Este parâmetro é ignorado para qualquer modelo, exceto `seedance-1-5-pro-251215`. (padrão: False) | BOOLEAN | Não | - |

**Nota:** Para o modelo `seedance-1-5-pro-251215`, `duration` deve ser 4 segundos ou maior. Tanto `first_frame` quanto `last_frame` devem ter entre 300x300 e 6000x6000 pixels e ter uma proporção de aspecto entre 0,4 e 2,5. O `prompt` é verificado e rejeitado se contiver palavras-chave de parâmetros reservadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ae0f3a34a21baad7f04f6917e98d16dc64496479a050896869ec6693a9a9ebaf`
