# LumaRay32ExtendVideoNode

Este nó estende uma geração de vídeo anterior do Luma Ray 3.2 adicionando novo conteúdo após ela (extensão para frente) ou antes dela (extensão para trás). Conecte a saída do ID de geração de um nó Luma Ray 3.2 anterior para criar uma extensão contínua de 5 segundos do seu vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|---------------|-------------|-------|
| `source_generation_id` | ID de geração do vídeo Ray 3.2 anterior a ser estendido. Conecte a saída generation_id de outro nó Luma Ray 3.2. | STRING | Sim | - |
| `direction` | "Forward" continua após o clipe anterior; "Backward" é anexado antes dele. Quando "Forward (continuar após)" é selecionado, você pode opcionalmente ativar o modo de loop. | COMBO | Sim | "Forward (continuar após)"<br>"Backward (introdução antes)" |
| `loop` | Faz um loop contínuo do vídeo estendido (apenas extensão para frente). | BOOLEAN | Não | Verdadeiro<br>Falso |
| `prompt` | Prompt de texto descrevendo o novo conteúdo a ser gerado. | STRING | Sim | - |
| `resolution` | Resolução de saída para o segmento de vídeo estendido. | COMBO | Sim | "540p"<br>"720p"<br>"1080p" |
| `seed` | Semente aleatória para resultados de geração reproduzíveis. | INT | Sim | - |

**Nota:** O parâmetro `loop` está disponível apenas quando `direction` está definido como "Forward (continuar após)". Ao usar "Backward (introdução antes)", a opção de loop não está disponível. O `prompt` deve ter entre 1 e 6000 caracteres.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `VIDEO` | O segmento de vídeo estendido gerado de 5 segundos. | VIDEO |
| `generation_id` | Identificador único para esta geração, que pode ser conectado a outro nó Luma Ray 3.2 Extend Video para extensões adicionais. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ExtendVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a67ca53d4bcb9f3fd82bc0482b579f5f7fe4bf866f8d83cb922e1082ad320057`
