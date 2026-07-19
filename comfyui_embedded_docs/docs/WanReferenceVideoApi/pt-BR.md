# Wan Referência para Vídeo

Esta documentação foi gerada por IA. Caso encontre erros ou tenha sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanReferenceVideoApi/en.md)

O nó Wan Reference to Video utiliza a aparência visual e a voz de um ou mais vídeos de referência de entrada, juntamente com um prompt de texto, para gerar um novo vídeo. Ele mantém a consistência com os personagens do material de referência enquanto cria novos conteúdos com base na sua descrição.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de IA específico a ser usado para a geração de vídeo. | COMBO | Sim | `"wan2.6-r2v"` |
| `prompt` | Uma descrição dos elementos e características visuais para o novo vídeo. Suporta inglês e chinês. Use identificadores como `character1` e `character2` para se referir aos personagens dos vídeos de referência. | STRING | Sim | - |
| `prompt negativo` | Uma descrição de elementos ou características a serem evitados no vídeo gerado. | STRING | Não | - |
| `vídeos de referência` | Uma lista de entradas de vídeo usadas como referências para a aparência e voz dos personagens. Você deve fornecer pelo menos um vídeo. Cada vídeo pode receber um nome como `character1`, `character2` ou `character3`. | AUTOGROW | Sim | - |
| `tamanho` | A resolução e a proporção de aspecto para o vídeo de saída. | COMBO | Sim | `"720p: 1:1 (960x960)"`<br>`"720p: 16:9 (1280x720)"`<br>`"720p: 9:16 (720x1280)"`<br>`"720p: 4:3 (1088x832)"`<br>`"720p: 3:4 (832x1088)"`<br>`"1080p: 1:1 (1440x1440)"`<br>`"1080p: 16:9 (1920x1080)"`<br>`"1080p: 9:16 (1080x1920)"`<br>`"1080p: 4:3 (1632x1248)"`<br>`"1080p: 3:4 (1248x1632)"` |
| `duração` | A duração do vídeo gerado em segundos. O valor deve ser múltiplo de 5 (padrão: 5). | INT | Sim | 5 a 10 |
| `semente` | Um valor de semente aleatório para resultados reproduzíveis. Um valor de 0 gerará uma semente aleatória. | INT | Não | 0 a 2147483647 |
| `tipo de tomada` | Especifica se o vídeo gerado é uma única tomada contínua ou contém múltiplas tomadas com cortes. | COMBO | Sim | `"single"`<br>`"multi"` |
| `marca d'água` | Quando ativado, uma marca d'água gerada por IA é adicionada ao vídeo final (padrão: False). | BOOLEAN | Não | - |

**Restrições:**

* Cada vídeo fornecido em `reference_videos` deve ter entre 2 e 30 segundos de duração.
* O parâmetro `duration` é limitado a valores específicos (5 ou 10 segundos).

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O arquivo de vídeo recém-gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanReferenceVideoApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ed29f0bd3a1b30a81c94896976c4f9ff7bf5d0bcafaba66d70be61fce1418962`
