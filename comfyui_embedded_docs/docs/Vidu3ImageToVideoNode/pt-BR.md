> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3ImageToVideoNode/pt-BR.md)

O nó de Geração de Vídeo a partir de Imagem Vidu Q3 cria uma sequência de vídeo a partir de uma imagem de entrada. Ele utiliza um modelo Vidu Q3 para animar a imagem, opcionalmente guiado por um prompt de texto, e gera um arquivo de vídeo como saída.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | COMBO | Sim | `"viduq3-pro"`<br>`"viduq3-turbo"` | Modelo a ser usado para a geração do vídeo. |
| `model.resolution` | COMBO | Sim | `"720p"`<br>`"1080p"`<br>`"2K"` (apenas viduq3-pro) | Resolução do vídeo de saída. As opções disponíveis dependem do modelo selecionado. |
| `model.duration` | INT | Sim | 1 a 16 | Duração do vídeo de saída em segundos (padrão: 5). |
| `model.audio` | BOOLEAN | Sim | `True` / `False` | Quando ativado, gera vídeo com som (incluindo diálogo e efeitos sonoros) (padrão: False). |
| `image` | IMAGE | Sim | - | Uma imagem a ser usada como quadro inicial do vídeo gerado. |
| `prompt` | STRING | Não | - | Um prompt de texto opcional para a geração do vídeo (máximo de 2000 caracteres) (padrão: vazio). |
| `seed` | INT | Não | 0 a 2147483647 | Um valor de semente para controlar a aleatoriedade da geração (padrão: 1). |

**Observação:** A `image` deve ter uma proporção de aspecto entre 1:4 e 4:1 (retrato para paisagem). O `prompt` é opcional, mas não pode exceder 2000 caracteres. As opções de `model.resolution` dependem do `model` selecionado: `"viduq3-pro"` suporta `"720p"`, `"1080p"` e `"2K"`; `"viduq3-turbo"` suporta `"720p"` e `"1080p"`.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O arquivo de vídeo gerado. |

---
**Source fingerprint (SHA-256):** `1dd3929860ee4a04b761014fd2cf7e9e32f9171d8b18fe1e93f27d0905ca04ee`
