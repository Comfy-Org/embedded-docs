# Geração de Vídeo Quadro Inicial/Final Vidu Q3

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/en.md)

Este nó gera um vídeo interpolando entre um quadro inicial fornecido e um quadro final, guiado por um prompt de texto. Ele usa o modelo Vidu Q3 para criar uma transição suave entre as duas imagens, produzindo um vídeo com duração e resolução especificadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo a ser usado para a geração de vídeo. Selecionar uma opção revela parâmetros de configuração adicionais para `resolution`, `duration` e `audio`. | COMBO | Sim | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `model.resolution` | Resolução do vídeo de saída. Este parâmetro é revelado após selecionar um `modelo`. | COMBO | Sim | `"720p"`<br>`"1080p"` |
| `model.duration` | Duração do vídeo de saída em segundos (padrão: 5). Este parâmetro é revelado após selecionar um `modelo`. | INT | Sim | 1 a 16 |
| `model.audio` | Quando ativado, gera vídeo com som (incluindo diálogo e efeitos sonoros) (padrão: False). Este parâmetro é revelado após selecionar um `modelo`. | BOOLEAN | Sim | `True` / `False` |
| `quadro inicial` | A imagem inicial para a sequência de vídeo. | IMAGE | Sim | - |
| `quadro final` | A imagem final para a sequência de vídeo. | IMAGE | Sim | - |
| `prompt` | Uma descrição em texto que guia a geração do vídeo (máximo de 2000 caracteres). | STRING | Sim | - |
| `semente` | Um valor de semente para controlar a aleatoriedade da geração (padrão: 1). | INT | Não | 0 a 2147483647 |

**Nota:** As imagens `first_frame` e `end_frame` devem ter proporções de aspecto semelhantes para obter melhores resultados. A proporção de aspecto das duas imagens deve estar entre 80% e 125% uma da outra (uma proximidade relativa entre 0,8 e 1,25).

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `video` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4a0a8d6657702d80278dc9239370683f408d7c051e91e8396939b7b81b87b4ed`
