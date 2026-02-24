> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/pt-BR.md)

O nó ByteDance Text to Video gera vídeos usando modelos da ByteDance por meio de uma API baseada em prompts de texto. Ele recebe uma descrição textual e várias configurações de vídeo como entrada e, em seguida, cria um vídeo que corresponde às especificações fornecidas. O nó gerencia a comunicação com a API e retorna o vídeo gerado como saída.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | STRING | Combo | seedance_1_pro | Opções de Text2VideoModelName | Nome do modelo |
| `prompt` | STRING | String | - | - | O prompt de texto usado para gerar o vídeo. |
| `resolution` | STRING | Combo | - | ["480p", "720p", "1080p"] | A resolução do vídeo de saída. |
| `aspect_ratio` | STRING | Combo | - | ["16:9", "4:3", "1:1", "3:4", "9:16", "21:9"] | A proporção de aspecto do vídeo de saída. |
| `duration` | INT | Int | 5 | 3-12 | A duração do vídeo de saída em segundos. |
| `seed` | INT | Int | 0 | 0-2147483647 | Semente a ser usada para a geração. (Opcional) |
| `camera_fixed` | BOOLEAN | Boolean | False | - | Especifica se a câmera deve ser fixa. A plataforma anexa uma instrução para fixar a câmera ao seu prompt, mas não garante o efeito real. (Opcional) |
| `watermark` | BOOLEAN | Boolean | True | - | Se deve adicionar uma marca d'água "Gerado por IA" ao vídeo. (Opcional) |

**Restrições dos Parâmetros:**

- O parâmetro `prompt` deve conter pelo menos 1 caractere após a remoção de espaços em branco
- O parâmetro `prompt` não pode conter os seguintes parâmetros de texto: "resolution", "ratio", "duration", "seed", "camerafixed", "watermark"
- O parâmetro `duration` está limitado a valores entre 3 e 12 segundos
- O parâmetro `seed` aceita valores de 0 a 2.147.483.647

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado |
