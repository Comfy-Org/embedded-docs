# Kling Lip Sync Vídeo com Texto

O nó Kling Lip Sync Text to Video sincroniza os movimentos da boca em um arquivo de vídeo para corresponder a um prompt de texto. Ele recebe um vídeo de entrada e gera um novo vídeo no qual os movimentos labiais do personagem são alinhados ao texto fornecido. O nó utiliza síntese de voz para criar uma sincronização de fala com aparência natural.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `vídeo` | Arquivo de vídeo de entrada para sincronização labial. O vídeo deve ter altura/largura entre 720px e 1920px, duração entre 2s e 10s e não pode ser maior que 100MB. | VIDEO | Sim | - |
| `texto` | Conteúdo de texto para geração de vídeo com sincronização labial. Obrigatório quando o modo é text2video. Comprimento máximo de 120 caracteres. | STRING | Sim | - |
| `voz` | Seleção de voz para o áudio de sincronização labial (padrão: "Melody"). Inclui opções de voz em inglês e chinês. | COMBO | Não | "Melody"<br>"Sunny"<br>"Sage"<br>"Ace"<br>"Blossom"<br>"Peppy"<br>"Dove"<br>"Shine"<br>"Anchor"<br>"Lyric"<br>"Tender"<br>"Siren"<br>"Zippy"<br>"Bud"<br>"Sprite"<br>"Candy"<br>"Beacon"<br>"Rock"<br>"Titan"<br>"Grace"<br>"Helen"<br>"Lore"<br>"Crag"<br>"Prattle"<br>"Hearth"<br>"The Reader"<br>"Commercial Lady"<br>"阳光少年"<br>"懂事小弟"<br>"运动少年"<br>"青春少女"<br>"温柔小妹"<br>"元气少女"<br>"阳光男生"<br>"幽默小哥"<br>"文艺小哥"<br>"甜美邻家"<br>"温柔姐姐"<br>"职场女青"<br>"活泼男童"<br>"俏皮女童"<br>"稳重老爸"<br>"温柔妈妈"<br>"严肃上司"<br>"优雅贵妇"<br>"慈祥爷爷"<br>"唠叨爷爷"<br>"唠叨奶奶"<br>"和蔼奶奶"<br>"东北老铁"<br>"重庆小伙"<br>"四川妹子"<br>"潮汕大叔"<br>"台湾男生"<br>"西安掌柜"<br>"天津姐姐"<br>"新闻播报男"<br>"译制片男"<br>"撒娇女友"<br>"刀片烟嗓"<br>"乖巧正太" |
| `velocidade_da_voz` | Velocidade da fala. Intervalo válido: 0.8~2.0, com precisão de uma casa decimal. (padrão: 1) | FLOAT | Não | 0.8-2.0 |

**Requisitos do vídeo:**

- O arquivo de vídeo não deve ser maior que 100MB
- A altura/largura deve estar entre 720px e 1920px
- A duração deve estar entre 2s e 10s

## Saídas

| Nome da Saída | Descrição | Tipo de dados |
|---------------|-----------|---------------|
| `output` | Vídeo gerado com áudio sincronizado com os lábios | VIDEO |
| `video_id` | Identificador único para o vídeo gerado | STRING |
| `duration` | Informação de duração do vídeo gerado | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `28a7be92d7e8a57efeb7e2913124e4373dfc75fbdba6ff7036fafb3a8ae43a60`
