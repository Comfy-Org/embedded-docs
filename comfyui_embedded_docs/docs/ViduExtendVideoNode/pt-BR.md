# Extensão de Vídeo Vidu

O ViduExtendVideoNode gera quadros adicionais para estender a duração de um vídeo existente. Ele usa um modelo de IA especificado para criar uma continuação perfeita com base no vídeo de origem e em um prompt de texto opcional.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a ser usado para extensão de vídeo. Selecionar um modelo revela suas configurações específicas de duração e resolução. | COMBO | Sim | `"viduq2-pro"`<br>`"viduq2-turbo"` |
| `video` | O vídeo de origem a ser estendido. | VIDEO | Sim | - |
| `prompt` | Um prompt de texto opcional para o vídeo estendido (máximo de 2000 caracteres, padrão: vazio). | STRING | Não | - |
| `seed` | Um valor de semente (seed) para controlar a aleatoriedade da geração (padrão: 1). | INT | Não | 0 a 2147483647 |
| `end_frame` | Uma imagem opcional para usar como quadro final de destino para a extensão. | IMAGE | Não | - |

### Entradas do viduq2-pro e do viduq2-turbo

Essas configurações são compartilhadas por ambos os modelos.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model.duration` | Duração do vídeo estendido em segundos (padrão: 4). Essa configuração aparece após selecionar um modelo. | INT | Sim | 1 a 7 |
| `model.resolution` | Resolução do vídeo de saída. Essa configuração aparece após selecionar um modelo. | COMBO | Sim | `"720p"`<br>`"1080p"` |

**Nota:** O vídeo de origem `video` deve ter duração entre 4 e 55 segundos. Se `end_frame` for fornecido, sua proporção de aspecto deve estar entre 1:4 e 4:1, e sua largura e altura devem ser de pelo menos 128 pixels cada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O arquivo de vídeo recém-gerado contendo a filmagem estendida. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduExtendVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bfa79dd1aee8a3e56d95fe7a899454b5c5f93679e098f59fc3bf58d93d290819`
