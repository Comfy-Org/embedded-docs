# Geração de Vídeo de Imagem para Vídeo Vidu Q3

O nó Vidu Q3 Image-to-Video Generation cria uma sequência de vídeo a partir de uma imagem de entrada. Ele usa um modelo Vidu Q3 para animar a imagem, opcionalmente guiado por um prompt de texto, e gera um arquivo de vídeo.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Modelo a ser usado para a geração de vídeo. | DYNAMIC_COMBO | Sim | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `imagem` | Uma imagem a ser usada como quadro inicial do vídeo gerado. | IMAGE | Sim | - |
| `prompt` | Um prompt de texto opcional para a geração de vídeo (máximo de 2000 caracteres) (padrão: vazio). | STRING | Sim | - |
| `semente` | Um valor de semente para controlar a aleatoriedade da geração (padrão: 1). | INT | Não | 0 a 2147483647 |

### viduq3-pro Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `resolução` | Resolução do vídeo de saída. | COMBO | Sim | `"720p"`<br>`"1080p"`<br>`"2K"` |
| `duração` | Duração do vídeo de saída em segundos (padrão: 5). | INT | Sim | 1 a 16 |
| `áudio` | Quando ativado, gera vídeo com som (incluindo diálogo e efeitos sonoros) (padrão: False). | BOOLEAN | Sim | `True`<br>`False` |

### viduq3-turbo Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `resolução` | Resolução do vídeo de saída. | COMBO | Sim | `"720p"`<br>`"1080p"` |
| `duração` | Duração do vídeo de saída em segundos (padrão: 5). | INT | Sim | 1 a 16 |
| `áudio` | Quando ativado, gera vídeo com som (incluindo diálogo e efeitos sonoros) (padrão: False). | BOOLEAN | Sim | `True`<br>`False` |

**Observação:** A `image` deve ter uma proporção de aspecto entre 1:4 e 4:1 (retrato a paisagem). O `prompt` é opcional, mas não pode exceder 2000 caracteres. As opções de resolução dependem do modelo selecionado: `"viduq3-pro"` suporta `"720p"`, `"1080p"` e `"2K"`; `"viduq3-turbo"` suporta `"720p"` e `"1080p"`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3ImageToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `77500d1e19928128decc010540670e311cd8ec4fcad913412517f47f0e27e15f`
