# MinimaxHailuo03TextToVideoNode

Este nó gera um vídeo a partir de um prompt de texto usando o modelo MiniMax H3. Ele envia o texto juntamente com as configurações de vídeo, como resolução, duração e proporção de aspecto, para a API MiniMax, e retorna o vídeo resultante como sua saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a ser usado para geração de vídeo. (padrão: "MiniMax H3"). Esta seleção também inclui o prompt de texto, resolução, duração e configurações de proporção de aspecto do vídeo gerado. | COMBO | Sim | `"MiniMax H3"` |
| `seed` | Semente aleatória. A mesma solicitação com a mesma semente gera resultados semelhantes, mas não garantidamente idênticos. (padrão: 42) | INT | Sim | 0 a 4294967295 |
| `watermark` | Se deve adicionar uma marca d'água AIGC ao vídeo. (padrão: false) | BOOLEAN | Não | true<br>false |

Nota: O prompt de texto incluído na opção `model` deve conter pelo menos um caractere que não seja espaço em branco. O preço estimado exibido para este nó é calculado a partir da duração do vídeo selecionada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo gerado a partir do prompt de texto fornecido. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03TextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9478576dd02ed407a39c95c7227eb8e1482db8b77adc814691fbd807e4cc2893`
