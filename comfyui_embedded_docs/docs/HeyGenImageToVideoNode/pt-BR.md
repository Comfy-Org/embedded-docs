# HeyGen Video 1.0 Imagem para Vídeo

Anime uma imagem em um vídeo com diálogo e som sincronizados usando o HeyGen Video 1.0. A imagem conectada é usada como primeiro quadro, e o vídeo gerado mantém sua proporção. Descreva no prompt o que deve acontecer, incluindo quaisquer falas. O nó envia a imagem, cria a tarefa de vídeo, aguarda sua conclusão e retorna o vídeo resultante.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Versão do modelo usada para geração. (padrão: `"heygen-video-1"`) | DYNAMIC_COMBO | Sim | `"heygen-video-1"` |
| `image` | Primeiro quadro do vídeo. Exatamente uma imagem é necessária; um lote é rejeitado. Recorte a imagem para alterar o formato do vídeo, pois a saída mantém a proporção desta imagem. | IMAGE | Sim | 1 imagem, proporção 1:4 a 4:1 |
| `prompt` | Descrição do que acontece no vídeo, incluindo qualquer diálogo. (padrão: string vazia) | STRING | Sim | 1 a 16000 caracteres |
| `duration` | Duração do vídeo de saída em segundos. Ignorada quando `auto_duration` é `"enabled"`. (padrão: 5) | INT | Sim | 5 a 30 |
| `resolution` | Resolução de saída. 1080p e 2k são renderizados apenas em 16:9 ou 9:16, então a imagem precisa ter esse formato; recorte-a primeiro. (padrão: `"768p"`) | COMBO | Sim | `"768p"`<br>`"480p"`<br>`"1080p"`<br>`"2k"` |
| `seed` | Semente para a geração. Os resultados ainda podem variar entre execuções com a mesma semente. (padrão: 42) | INT | Sim | 0 a 4294967295 |
| `auto_duration` | Quando habilitado, a duração do vídeo segue o diálogo entre aspas no prompt (8 a 30 segundos) e `duration` é ignorado. (padrão: `"disabled"`) | COMBO | Não | `"disabled"`<br>`"enabled"` |

### Restrições dos parâmetros

- **Imagem única:** `image` deve conter exatamente uma imagem. Conectar um lote gera um erro.
- **Proporção da imagem:** a imagem não pode ser mais larga que 4x a sua altura nem mais alta que 4x a sua largura (entre 1:4 e 4:1); caso contrário, a execução falha.
- **Prompt obrigatório:** o prompt deve conter pelo menos um caractere que não seja espaço em branco e no máximo 16000 caracteres.
- **Resoluções altas:** `resolution` `"1080p"` e `"2k"` exigem uma imagem 16:9 ou 9:16, porque o vídeo mantém a proporção da imagem. Recorte a imagem para outros formatos.
- **Semente:** a semente apenas decide se o nó será reexecutado; os resultados não são reproduzíveis com a mesma semente.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo gerado com diálogo e som sincronizados, na proporção da imagem de entrada. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenImageToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e711d1d84c6c73a2ee177903f982042086a57b3e1afff8390c6e5b3bcd09c914`
