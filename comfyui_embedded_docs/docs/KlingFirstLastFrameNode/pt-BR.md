> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingFirstLastFrameNode/pt-BR.md)

Este nó utiliza o modelo Kling 3.0 para gerar um vídeo. Ele cria o vídeo com base em um prompt de texto, uma duração especificada e duas imagens fornecidas: um quadro inicial e um quadro final. O nó também pode gerar áudio de acompanhamento para o vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | N/A | A descrição textual que orienta a geração do vídeo. Deve ter entre 1 e 2500 caracteres. |
| `duration` | INT | Não | 3 a 15 | A duração do vídeo em segundos (padrão: 5). |
| `first_frame` | IMAGE | Sim | N/A | A imagem inicial do vídeo. Deve ter pelo menos 300x300 pixels e uma proporção de aspecto entre 1:2,5 e 2,5:1. |
| `end_frame` | IMAGE | Sim | N/A | A imagem final do vídeo. Deve ter pelo menos 300x300 pixels e uma proporção de aspecto entre 1:2,5 e 2,5:1. |
| `generate_audio` | BOOLEAN | Não | N/A | Controla se o áudio será gerado para o vídeo (padrão: Verdadeiro). |
| `model` | COMBO | Não | `"kling-v3"` | Configurações do modelo e de geração. Selecionar esta opção revela um parâmetro `resolution` aninhado. |
| `model.resolution` | COMBO | Não | `"4k"`<br>`"1080p"`<br>`"720p"` | A resolução do vídeo gerado. Este parâmetro só está disponível quando o `model` está definido como `"kling-v3"` (padrão: `"1080p"`). |
| `seed` | INT | Não | 0 a 2147483647 | Um número usado para controlar se o nó deve ser executado novamente. Os resultados são não determinísticos, independentemente do valor da semente (padrão: 0). |

**Observação:** As imagens `first_frame` e `end_frame` devem atender aos requisitos mínimos de tamanho e proporção de aspecto para que o nó funcione corretamente.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O arquivo de vídeo gerado. |

---
**Source fingerprint (SHA-256):** `5c904fec35b2bb41cf521263b1b06fd36ba227400b4cec24e79a4e80618e4bae`
