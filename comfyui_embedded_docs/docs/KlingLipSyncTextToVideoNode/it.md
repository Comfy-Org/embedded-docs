# Kling Lip Sync Video con Testo

Il nodo Kling Lip Sync Text to Video sincronizza i movimenti della bocca in un file video per adattarli a un prompt testuale. Prende in input un video e genera un nuovo video in cui i movimenti labiali del personaggio sono allineati al testo fornito. Il nodo utilizza la sintesi vocale per creare una sincronizzazione del parlato dall'aspetto naturale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | File video di input per la sincronizzazione labiale. Il video deve avere altezza/larghezza compresa tra 720px e 1920px, durata compresa tra 2s e 10s e dimensione non superiore a 100MB. | VIDEO | Sì | - |
| `text` | Contenuto testuale per la generazione video con lip-sync. Obbligatorio quando la modalità è text2video. La lunghezza massima è di 120 caratteri. | STRING | Sì | - |
| `voice` | Selezione della voce per l'audio lip-sync (predefinito: "Melody"). Include opzioni vocali sia in inglese sia in cinese. | COMBO | No | "Melody"<br>"Sunny"<br>"Sage"<br>"Ace"<br>"Blossom"<br>"Peppy"<br>"Dove"<br>"Shine"<br>"Anchor"<br>"Lyric"<br>"Tender"<br>"Siren"<br>"Zippy"<br>"Bud"<br>"Sprite"<br>"Candy"<br>"Beacon"<br>"Rock"<br>"Titan"<br>"Grace"<br>"Helen"<br>"Lore"<br>"Crag"<br>"Prattle"<br>"Hearth"<br>"The Reader"<br>"Commercial Lady"<br>"阳光少年"<br>"懂事小弟"<br>"运动少年"<br>"青春少女"<br>"温柔小妹"<br>"元气少女"<br>"阳光男生"<br>"幽默小哥"<br>"文艺小哥"<br>"甜美邻家"<br>"温柔姐姐"<br>"职场女青"<br>"活泼男童"<br>"俏皮女童"<br>"稳重老爸"<br>"温柔妈妈"<br>"严肃上司"<br>"优雅贵妇"<br>"慈祥爷爷"<br>"唠叨爷爷"<br>"唠叨奶奶"<br>"和蔼奶奶"<br>"东北老铁"<br>"重庆小伙"<br>"四川妹子"<br>"潮汕大叔"<br>"台湾男生"<br>"西安掌柜"<br>"天津姐姐"<br>"新闻播报男"<br>"译制片男"<br>"撒娇女友"<br>"刀片烟嗓"<br>"乖巧正太" |
| `voice_speed` | Velocità del parlato. Intervallo valido: 0.8~2.0, con precisione fino a una cifra decimale. (predefinito: 1) | FLOAT | No | 0.8-2.0 |

**Requisiti del video:**

- Il file video non deve essere più grande di 100MB
- L'altezza/larghezza deve essere compresa tra 720px e 1920px
- La durata deve essere compresa tra 2s e 10s

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | Video generato con audio sincronizzato labialmente | VIDEO |
| `video_id` | Identificatore univoco per il video generato | STRING |
| `duration` | Informazioni sulla durata del video generato | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `28a7be92d7e8a57efeb7e2913124e4373dfc75fbdba6ff7036fafb3a8ae43a60`
