# Geração de Vídeo Quadro Inicial/Final Vidu Q3

Este nó gera um vídeo interpolando entre um quadro inicial e um quadro final fornecidos, guiado por um prompt de texto. Ele usa o modelo Vidu Q3 para criar uma transição perfeita entre as duas imagens, produzindo um vídeo com duração e resolução especificadas.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo a ser usado para geração de vídeo. Selecionar uma opção revela parâmetros de configuração adicionais para `resolution`, `duration` e `audio`. | DYNAMIC_COMBO | Sim | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `quadro inicial` | A imagem inicial para a sequência de vídeo. | IMAGE | Sim | - |
| `quadro final` | A imagem final para a sequência de vídeo. | IMAGE | Sim | - |
| `prompt` | Descrição do prompt (máximo 2000 caracteres). | STRING | Sim | - |
| `semente` | Um valor de semente para controlar a aleatoriedade da geração (padrão: 1). | INT | Não | 0 a 2147483647 |

### Entradas de viduq3-pro e viduq3-turbo

Os seguintes parâmetros são compartilhados por ambas as opções de modelo (`viduq3-pro` e `viduq3-turbo`). Eles são revelados após a seleção de um modelo.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `resolução` | Resolução do vídeo de saída. Este parâmetro é revelado após selecionar um `model`. | COMBO | Sim | `"720p"`<br>`"1080p"` |
| `duração` | Duração do vídeo de saída em segundos (padrão: 5). Este parâmetro é revelado após selecionar um `model`. | INT | Sim | 1 a 16 |
| `áudio` | Quando ativado, gera vídeo com som (incluindo diálogo e efeitos sonoros) (padrão: False). Este parâmetro é revelado após selecionar um `model`. | BOOLEAN | Sim | `True`<br>`False` |

**Nota:** As imagens `first_frame` e `end_frame` devem ter proporções de aspecto semelhantes para obter melhores resultados. A proporção de aspecto das duas imagens deve estar entre 80% e 125% uma da outra (uma proximidade relativa entre 0,8 e 1,25).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c917867c5a7b68a1286f445025070f9a55d8d10091d9562960e0428cbedf25e4`
