Este nó utiliza o modelo Kling 3.0 para gerar um vídeo. Ele cria o vídeo com base em um prompt de texto, uma duração especificada e duas imagens fornecidas: um quadro inicial e um quadro final. O nó também pode gerar áudio de acompanhamento para o vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | A descrição textual que orienta a geração do vídeo. Deve ter entre 1 e 2500 caracteres. | STRING | Sim | N/A |
| `duração` | A duração do vídeo em segundos (padrão: 5). | INT | Não | 3 a 15 |
| `primeiro_frame` | A imagem inicial do vídeo. Deve ter pelo menos 300x300 pixels e uma proporção de aspecto entre 1:2,5 e 2,5:1. | IMAGE | Sim | N/A |
| `último_frame` | A imagem final do vídeo. Deve ter pelo menos 300x300 pixels e uma proporção de aspecto entre 1:2,5 e 2,5:1. | IMAGE | Sim | N/A |
| `gerar_áudio` | Controla se o áudio será gerado para o vídeo (padrão: Verdadeiro). | BOOLEAN | Não | N/A |
| `modelo` | Configurações do modelo e de geração. Selecionar esta opção revela um parâmetro `resolution` aninhado. | COMBO | Não | `"kling-v3"` |
| `model.resolution` | A resolução do vídeo gerado. Este parâmetro só está disponível quando o `modelo` está definido como `"kling-v3"` (padrão: `"1080p"`). | COMBO | Não | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `semente` | Um número usado para controlar se o nó deve ser executado novamente. Os resultados são não determinísticos, independentemente do valor da semente (padrão: 0). | INT | Não | 0 a 2147483647 |

**Observação:** As imagens `first_frame` e `end_frame` devem atender aos requisitos mínimos de tamanho e proporção de aspecto para que o nó funcione corretamente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingFirstLastFrameNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5c904fec35b2bb41cf521263b1b06fd36ba227400b4cec24e79a4e80618e4bae`
