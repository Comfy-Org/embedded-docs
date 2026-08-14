# Kling 3.0 Primeiro-Último-Frame para Vídeo

Este nó usa o modelo Kling 3.0 para gerar um vídeo. Ele cria o vídeo com base em um prompt de texto, uma duração especificada e duas imagens fornecidas: um quadro inicial e um quadro final. O nó também pode gerar áudio de acompanhamento para o vídeo.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo e configurações de geração. Selecionar esta opção revela um parâmetro `resolution` aninhado. | COMBO | Não | `"kling-v3"` |
| `prompt` | A descrição em texto que orienta a geração do vídeo. Deve ter entre 1 e 2500 caracteres. | STRING | Sim | N/A |
| `duration` | A duração do vídeo em segundos (padrão: 5). | INT | Não | 3 a 15 |
| `first_frame` | A imagem inicial do vídeo. Deve ter pelo menos 300x300 pixels e uma proporção de aspecto entre 1:2.5 e 2.5:1. | IMAGE | Sim | N/A |
| `end_frame` | A imagem final do vídeo. Deve ter pelo menos 300x300 pixels e uma proporção de aspecto entre 1:2.5 e 2.5:1. | IMAGE | Sim | N/A |
| `generate_audio` | Controla se o áudio deve ser gerado para o vídeo (padrão: True). | BOOLEAN | Não | N/A |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados não são determinísticos independentemente da semente (padrão: 0). | INT | Não | 0 a 2147483647 |

### Entradas do Kling V3

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `resolution` | A resolução do vídeo gerado (padrão: `"1080p"`). | COMBO | Não | `"4k"`<br>`"1080p"`<br>`"720p"` |

**Nota:** As imagens `first_frame` e `end_frame` devem ter pelo menos 300x300 pixels e uma proporção de aspecto entre 1:2.5 e 2.5:1 para que o nó funcione corretamente. O `prompt` deve ter entre 1 e 2500 caracteres. A opção `resolution` corresponde a um modo de geração Kling: `"4k"`, `"1080p"` (pro) e `"720p"` (padrão).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingFirstLastFrameNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b71119c3267e2a74d2180e5182463c78828e892bfcf1eeb7c33a0f4d7019997f`
