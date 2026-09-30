# HeyGen Video 1.0 Image to Video

Anime uma imagem em um vídeo com diálogo e som sincronizados usando o HeyGen Video 1.0. A imagem conectada é usada como o primeiro quadro, e o vídeo gerado mantém a proporção da imagem conectada. Descreva o que deve acontecer, incluindo quaisquer falas, no prompt. O nó envia a imagem, cria a tarefa de vídeo, aguarda sua conclusão e retorna o vídeo resultante.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `model` | Versão do modelo usada para geração. (padrão: `"heygen-video-1"`) | DYNAMIC_COMBO | Sim | `"heygen-video-1"` |
| `image` | Primeiro quadro do vídeo. É necessária exatamente uma imagem; um lote é rejeitado. Recorte a imagem para alterar o formato do vídeo, pois a saída mantém a proporção desta imagem. | IMAGE | Sim | 1 imagem, proporção de 1:4 a 4:1 |
| `prompt` | Descrição do que acontece no vídeo, incluindo qualquer diálogo. (padrão: string vazia) | STRING | Sim | 1 a 32000 caracteres |
| `duration` | Duração do vídeo de saída em segundos. (padrão: 5) | INT | Sim | 5 a 15 |
| `resolution` | Resolução de saída. (padrão: `"768p"`) | COMBO | Sim | `"768p"`<br>`"480p"` |
| `seed` | Semente para a geração. Os resultados ainda podem variar entre execuções com a mesma seed. (padrão: 42) | INT | Sim | 0 a 4294967295 |

### Restrições dos parâmetros

- **Imagem única:** `image` deve conter exatamente uma imagem. Conectar um lote gera um erro.
- **Proporção da imagem:** a imagem não pode ser mais larga que 4x sua altura nem mais alta que 4x sua largura (entre 1:4 e 4:1); caso contrário, a execução falha.
- **Prompt obrigatório:** o prompt deve conter pelo menos um caractere que não seja espaço em branco e no máximo 32000 caracteres.
- **Seed:** a seed só decide se o nó será executado novamente; os resultados não são reproduzíveis com a mesma seed.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|---------------|-----------|---------------|
| `VIDEO` | O vídeo gerado com diálogo e som sincronizados, na proporção da imagem de entrada. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenImageToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1de530dcc98f2324f6ef4e2cfe309a717a12116382e9885aca14a8ae0be4de39`
