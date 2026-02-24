> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanReferenceVideoApi/pt-BR.md)

O nó Wan Reference to Video utiliza a aparência visual e a voz de um ou mais vídeos de referência de entrada, juntamente com um prompt de texto, para gerar um novo vídeo. Ele mantém a consistência com os personagens do material de referência enquanto cria novo conteúdo baseado na sua descrição.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sim | `"wan2.6-r2v"` | O modelo de IA específico a ser usado para a geração de vídeo. |
| `prompt` | STRING | Sim | - | Uma descrição dos elementos e características visuais para o novo vídeo. Suporta inglês e chinês. Use identificadores como `character1` e `character2` para se referir aos personagens dos vídeos de referência. |
| `negative_prompt` | STRING | Não | - | Uma descrição de elementos ou características a serem evitadas no vídeo gerado. |
| `reference_videos` | AUTOGROW | Sim | - | Uma lista de entradas de vídeo usadas como referência para a aparência e voz dos personagens. Você deve fornecer pelo menos um vídeo. Cada vídeo pode receber um nome como `character1`, `character2` ou `character3`. |
| `size` | COMBO | Sim | `"720p: 1:1 (960x960)"`<br>`"720p: 16:9 (1280x720)"`<br>`"720p: 9:16 (720x1280)"`<br>`"720p: 4:3 (1088x832)"`<br>`"720p: 3:4 (832x1088)"`<br>`"1080p: 1:1 (1440x1440)"`<br>`"1080p: 16:9 (1920x1080)"`<br>`"1080p: 9:16 (1080x1920)"`<br>`"1080p: 4:3 (1632x1248)"`<br>`"1080p: 3:4 (1248x1632)"` | A resolução e proporção de tela para o vídeo de saída. |
| `duration` | INT | Sim | 5 a 10 | A duração do vídeo gerado em segundos. O valor deve ser um múltiplo de 5 (padrão: 5). |
| `seed` | INT | Não | 0 a 2147483647 | Um valor de seed aleatória para resultados reproduzíveis. Um valor de 0 gerará uma seed aleatória. |
| `shot_type` | COMBO | Sim | `"single"`<br>`"multi"` | Especifica se o vídeo gerado é uma tomada única contínua ou contém múltiplas tomadas com cortes. |
| `watermark` | BOOLEAN | Não | - | Quando habilitado, uma marca d'água gerada por IA é adicionada ao vídeo final (padrão: Falso). |

**Restrições:**

* Cada vídeo fornecido em `reference_videos` deve ter entre 2 e 30 segundos de duração.
* O parâmetro `duration` está limitado a valores específicos (5 ou 10 segundos).

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O novo arquivo de vídeo gerado. |
