# Comfy Cloud MiniMax H3 Primeiro-Último Quadro para Vídeo [BETA]

Executa o workflow de primeiro e último quadro do MiniMax H3 em uma GPU do Comfy Cloud e retorna o movimento entre dois quadros-chave com uma trilha sonora correspondente. Forneça os quadros de abertura e encerramento e o modelo preenche a cena entre eles. O último quadro é opcional: se for omitido, o movimento se afasta do primeiro quadro. Este é um nó beta e é cobrado por segundo de GPU.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `first_frame` | A imagem a partir da qual o vídeo começa. Ela é enviada com até 2048x2048 pixels antes da execução do workflow. | IMAGE | Sim | - |
| `último_quadro` | Quadro de encerramento opcional. Quando conectado, o movimento gerado termina nesta imagem; sem ele, o movimento se afasta de `first_frame`. | IMAGE | Não | - |
| `prompt` | A descrição textual do movimento e dos sons que a cena deve conter. Espaços em branco no início e no fim são removidos antes do envio. | STRING | Sim | 1 a 4096 caracteres |
| `seed` | Semente aleatória que controla o resultado gerado (padrão: 42). | INT | Sim | 0 a 18446744073709551615 |
| `aspect_ratio` | Proporção do vídeo gerado (padrão: `"1:1"`). | COMBO | Sim | `"1:1"`<br>`"3:4"`<br>`"2:3"`<br>`"3:2"`<br>`"4:3"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"` |
| `resolution` | Orçamento de tamanho do quadro (padrão: `"480p"`). O 720p custa aproximadamente o dobro dos segundos de GPU do 480p. | COMBO | Sim | `"480p"`<br>`"720p"` |
| `duration_seconds` | Duração em segundos (padrão: 5). O pipeline quantiza em etapas de 17 quadros a 24 fps, portanto o clipe resultante varia em até cerca de dois terços de segundo em relação a esse valor. | INT | Sim | 5 a 15 |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo gerado com sua trilha sonora. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxH3FirstLastFrameToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5b9d1a2155951fb953e94726f0c6ca7720a805ab5d3015adaa5cc496acaa0de3`
