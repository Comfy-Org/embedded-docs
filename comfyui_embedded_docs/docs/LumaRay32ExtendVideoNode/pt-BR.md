# Luma Ray 3.2 Estender Vídeo

Luma Ray 3.2 Extend Video dá continuidade a uma geração de vídeo anterior do Luma Ray 3.2 ao criar um novo segmento de 5 segundos, seja após o clipe original (forward) ou antes dele (backward). Conecte a saída `generation_id` de um nó Luma Ray 3.2 anterior para usar esse clipe como quadro inicial (forward) ou quadro final (backward) da extensão.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `direction` | Forward continua após o clipe anterior; backward é adicionado antes dele. Forward usa o clipe de origem como quadro inicial; backward usa como quadro final. Selecionar "Forward (continue after)" adiciona a opção `loop`. | DYNAMIC_COMBO | Sim | "Forward (continue after)"<br>"Backward (lead-in before)" |
| `source_generation_id` | ID de geração do vídeo Ray 3.2 anterior a ser estendido. Conecte a saída `generation_id` de outro nó Luma Ray 3.2. Este valor é obrigatório e não deve estar vazio. | STRING | Sim | – |
| `prompt` | Prompt de texto para o novo conteúdo. Deve ter entre 1 e 6000 caracteres. | STRING | Sim | 1 a 6000 caracteres |
| `resolution` | Resolução de saída do segmento de vídeo estendido. Padrão: "720p". | COMBO | Sim | "540p"<br>"720p"<br>"1080p" |
| `seed` | Semente para determinar se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. Padrão: 0. | INT | Sim | 0 a 0xFFFFFFFFFFFFFFFF |

### Entradas de Forward (continue after)

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `loop` | Faz um loop contínuo do vídeo estendido (somente para extensão forward). Padrão: False. | BOOLEAN | Não | True<br>False |

### Entradas de Backward (lead-in before)

Esta direção não adiciona nenhum parâmetro adicional.

**Observação:** As extensões têm sempre 5 segundos. O parâmetro `loop` só está disponível quando `direction` for "Forward (continue after)"; ao usar "Backward (lead-in before)", a opção `loop` não está disponível. O `prompt` deve ter entre 1 e 6000 caracteres. O `source_generation_id` é obrigatório e deve ser conectado à saída `generation_id` de um nó Luma Ray 3.2 anterior.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O segmento de vídeo estendido de 5 segundos gerado. | VIDEO |
| `generation_id` | Identificador exclusivo para esta geração, que pode ser conectado a outro nó Luma Ray 3.2 Extend Video para extensões adicionais. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ExtendVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a67ca53d4bcb9f3fd82bc0482b579f5f7fe4bf866f8d83cb922e1082ad320057`
