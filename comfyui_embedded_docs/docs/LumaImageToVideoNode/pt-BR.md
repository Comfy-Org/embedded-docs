> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageToVideoNode/pt-BR.md)

Gera vídeos de forma síncrona com base em um prompt de texto e imagens opcionais de início/fim. Este nó utiliza a API Luma para criar vídeos, permitindo definir o conteúdo do vídeo através de um prompt e, opcionalmente, especificar o primeiro e/ou último quadro para controlar a estrutura do vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Prompt para a geração do vídeo (padrão: "") |
| `model` | COMBO | Sim | Múltiplas opções disponíveis | Seleciona o modelo de geração de vídeo dentre os modelos Luma disponíveis |
| `resolution` | COMBO | Sim | `"540p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` | Resolução de saída do vídeo gerado (padrão: "540p"). Este parâmetro é ignorado ao usar o modelo `ray-1-6`. |
| `duration` | COMBO | Sim | `"5s"`<br>`"9s"` | Duração do vídeo gerado. Este parâmetro é ignorado ao usar o modelo `ray-1-6`. |
| `loop` | BOOLEAN | Sim | - | Se o vídeo gerado deve ser em loop (padrão: Falso) |
| `seed` | INT | Sim | 0 a 18446744073709551615 | Semente para determinar se o nó deve ser reexecutado; os resultados reais são não determinísticos independentemente da semente. (padrão: 0) |
| `first_image` | IMAGE | Não | - | Primeiro quadro do vídeo gerado. (opcional) |
| `last_image` | IMAGE | Não | - | Último quadro do vídeo gerado. (opcional) |
| `luma_concepts` | CUSTOM | Não | - | Conceitos de Câmera opcionais para ditar o movimento da câmera através do nó Luma Concepts. (opcional) |

**Nota:** Pelo menos um dos parâmetros `first_image` ou `last_image` deve ser fornecido. O nó lançará uma exceção se ambos estiverem ausentes. Os parâmetros `resolution` e `duration` são ignorados quando o `model` está definido como `ray-1-6`.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado |

---
**Source fingerprint (SHA-256):** `210286ad38cecc5b3b0689f470ff473e996abfd251f88a45bcac936751ae2674`
