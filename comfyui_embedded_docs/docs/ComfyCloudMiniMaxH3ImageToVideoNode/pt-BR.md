# Comfy Cloud MiniMax H3 Imagem para Vídeo [BETA]

Executa o fluxo de trabalho de imagem para vídeo do MiniMax H3 em uma GPU do Comfy Cloud e retorna um vídeo com uma trilha sonora correspondente. A imagem estática se torna o primeiro quadro. Fornecer novamente o quadro final de um clipe como entrada continua a sequência, assim, encadear várias execuções monta uma tomada mais longa. Este é um nó beta e é cobrado por segundo de GPU.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `primeiro_quadro` | A imagem a partir da qual o vídeo começa. Ela é enviada com até 2048x2048 pixels antes da execução do fluxo de trabalho. | IMAGE | Sim | - |
| `prompt` | A descrição textual do movimento e dos sons que a tomada deve conter. Espaços em branco no início e no final são removidos antes do envio. | STRING | Sim | 1 a 4096 caracteres |
| `semente` | Semente aleatória que controla o resultado gerado (padrão: 42). | INT | Sim | 0 a 18446744073709551615 |
| `proporção_de_aspecto` | Proporção do vídeo gerado (padrão: `"1:1"`). | COMBO | Sim | `"1:1"`<br>`"3:4"`<br>`"2:3"`<br>`"3:2"`<br>`"4:3"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"` |
| `resolução` | Orçamento de tamanho do quadro (padrão: `"480p"`). 720p custa aproximadamente o dobro dos segundos de GPU de 480p. | COMBO | Sim | `"480p"`<br>`"720p"` |
| `duração_em_segundos` | Duração em segundos (padrão: 5). O pipeline quantiza em etapas de 17 quadros a 24 fps, de modo que o clipe fica dentro de aproximadamente dois terços de segundo desse valor. | INT | Sim | 5 a 15 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo gerado com sua trilha sonora. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxH3ImageToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d3657e266f2b9f789414a106ef66b6c64ec314d27c3b6a99c3a6a9b8584abf61`
