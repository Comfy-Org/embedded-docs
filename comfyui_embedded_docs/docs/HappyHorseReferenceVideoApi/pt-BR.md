# HappyHorse Referência para Vídeo

Este nó gera um vídeo apresentando uma pessoa ou objeto com base em imagens de referência usando o modelo HappyHorse. Ele suporta a criação de vídeos com um único personagem ou múltiplos personagens interagindo entre si.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo HappyHorse a ser usado para geração de vídeo. | COMBO | Sim | `"happyhorse-1.0-r2v"` |
| `prompt` | Uma descrição textual do vídeo que você deseja gerar. Use identificadores como 'character1' e 'character2' para se referir aos personagens de referência. | STRING | Sim | N/A |
| `resolution` | A resolução do vídeo gerado. | COMBO | Sim | `"720P"`<br>`"1080P"` |
| `ratio` | A proporção de aspecto do vídeo gerado. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | A duração do vídeo gerado em segundos (padrão: 5). | INT | Sim | 3 a 15 |
| `reference_images` | Uma ou mais imagens de referência da pessoa ou objeto a ser apresentado no vídeo. Você deve fornecer pelo menos uma imagem. | IMAGE | Sim | 1 a 9 |
| `seed` | Um valor de semente para geração reproduzível (padrão: 0). A semente pode ser configurada para alterar automaticamente após cada geração. | INT | Não | 0 a 2147483647 |
| `watermark` | Se deve adicionar uma marca d'água gerada por IA ao vídeo resultante (padrão: Falso). | BOOLEAN | Não | Verdadeiro ou Falso |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `VIDEO` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseReferenceVideoApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9162e150aef4cbafa42d59055bdff953e9c21b1e5fbf7c800629e570ee4cd0f9`
