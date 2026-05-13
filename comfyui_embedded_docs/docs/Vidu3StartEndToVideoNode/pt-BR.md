> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/en.md)

Este nó gera um vídeo interpolando entre um quadro inicial fornecido e um quadro final, guiado por um prompt de texto. Ele usa o modelo Vidu Q3 para criar uma transição suave entre as duas imagens, produzindo um vídeo com duração e resolução especificadas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `modelo` | COMBO | Sim | `"viduq3-pro"`<br>`"viduq3-turbo"` | O modelo a ser usado para a geração de vídeo. Selecionar uma opção revela parâmetros de configuração adicionais para `resolution`, `duration` e `audio`. |
| `model.resolution` | COMBO | Sim | `"720p"`<br>`"1080p"` | Resolução do vídeo de saída. Este parâmetro é revelado após selecionar um `modelo`. |
| `model.duration` | INT | Sim | 1 a 16 | Duração do vídeo de saída em segundos (padrão: 5). Este parâmetro é revelado após selecionar um `modelo`. |
| `model.audio` | BOOLEAN | Sim | `True` / `False` | Quando ativado, gera vídeo com som (incluindo diálogo e efeitos sonoros) (padrão: False). Este parâmetro é revelado após selecionar um `modelo`. |
| `quadro inicial` | IMAGE | Sim | - | A imagem inicial para a sequência de vídeo. |
| `quadro final` | IMAGE | Sim | - | A imagem final para a sequência de vídeo. |
| `prompt` | STRING | Sim | - | Uma descrição em texto que guia a geração do vídeo (máximo de 2000 caracteres). |
| `semente` | INT | Não | 0 a 2147483647 | Um valor de semente para controlar a aleatoriedade da geração (padrão: 1). |

**Nota:** As imagens `first_frame` e `end_frame` devem ter proporções de aspecto semelhantes para obter melhores resultados. A proporção de aspecto das duas imagens deve estar entre 80% e 125% uma da outra (uma proximidade relativa entre 0,8 e 1,25).

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `video` | VIDEO | O arquivo de vídeo gerado. |

---
**Source fingerprint (SHA-256):** `4a0a8d6657702d80278dc9239370683f408d7c051e91e8396939b7b81b87b4ed`
