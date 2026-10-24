# Comfy Cloud MiniMax H3 Texto para Vídeo [BETA]

Executa o fluxo de trabalho de texto para vídeo MiniMax H3 em uma GPU do Comfy Cloud e retorna um vídeo com trilha sonora correspondente. Imagem e áudio saem da mesma passagem, em vez de serem dublados posteriormente. Este é um nó beta e é cobrado por segundo de GPU.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | A descrição textual do vídeo, incluindo os sons que a cena deve conter. Espaços em branco no início e no final são removidos antes do envio. | STRING | Sim | 1 a 4096 caracteres |
| `semente` | Semente aleatória que controla o resultado gerado (padrão: 42). | INT | Sim | 0 a 18446744073709551615 |
| `proporção_de_aspecto` | Proporção de aspecto do vídeo gerado (padrão: `"16:9"`). | COMBO | Sim | `"1:1"`<br>`"3:4"`<br>`"2:3"`<br>`"3:2"`<br>`"4:3"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"` |
| `resolução` | Orçamento de tamanho de quadro (padrão: `"480p"`). 720p custa aproximadamente o dobro dos segundos de GPU de 480p. | COMBO | Sim | `"480p"`<br>`"720p"` |
| `duração_em_segundos` | Duração em segundos (padrão: 5). O pipeline quantiza em etapas de 17 quadros a 24 fps, então o clipe fica dentro de cerca de dois terços de segundo desse valor. | INT | Sim | 5 a 15 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo gerado com sua trilha sonora. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMiniMaxH3TextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bd1cbc80baa3b77ba48b529119495052252570b949676742b4c77cfe86b70ee2`
