# Kling Lip-Sync-Video mit Text

Der Kling Lip Sync Text to Video Node synchronisiert Lippenbewegungen in einer Videodatei mit einem Text-Prompt. Er nimmt ein Eingabevideo entgegen und generiert ein neues Video, bei dem die Lippenbewegungen der Figur mit dem bereitgestellten Text abgeglichen werden. Der Node verwendet Stimmsynthese, um eine natürlich wirkende Sprachsynchronisation zu erzeugen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `video` | Eingabe-Videodatei für die Lippensynchronisation. Das Video muss in Höhe/Breite zwischen 720px und 1920px liegen, eine Dauer zwischen 2s und 10s haben und darf nicht größer als 100MB sein. | VIDEO | Ja | - |
| `text` | Textinhalt für die Lip-Sync-Videogenerierung. Erforderlich, wenn der Modus text2video ist. Maximale Länge beträgt 120 Zeichen. | STRING | Ja | - |
| `voice` | Stimmauswahl für das Lip-Sync-Audio (Standard: "Melody"). Enthält sowohl englische als auch chinesische Stimmoptionen. | COMBO | Nein | "Melody"<br>"Sunny"<br>"Sage"<br>"Ace"<br>"Blossom"<br>"Peppy"<br>"Dove"<br>"Shine"<br>"Anchor"<br>"Lyric"<br>"Tender"<br>"Siren"<br>"Zippy"<br>"Bud"<br>"Sprite"<br>"Candy"<br>"Beacon"<br>"Rock"<br>"Titan"<br>"Grace"<br>"Helen"<br>"Lore"<br>"Crag"<br>"Prattle"<br>"Hearth"<br>"The Reader"<br>"Commercial Lady"<br>"阳光少年"<br>"懂事小弟"<br>"运动少年"<br>"青春少女"<br>"温柔小妹"<br>"元气少女"<br>"阳光男生"<br>"幽默小哥"<br>"文艺小哥"<br>"甜美邻家"<br>"温柔姐姐"<br>"职场女青"<br>"活泼男童"<br>"俏皮女童"<br>"稳重老爸"<br>"温柔妈妈"<br>"严肃上司"<br>"优雅贵妇"<br>"慈祥爷爷"<br>"唠叨爷爷"<br>"唠叨奶奶"<br>"和蔼奶奶"<br>"东北老铁"<br>"重庆小伙"<br>"四川妹子"<br>"潮汕大叔"<br>"台湾男生"<br>"西安掌柜"<br>"天津姐姐"<br>"新闻播报男"<br>"译制片男"<br>"撒娇女友"<br>"刀片烟嗓"<br>"乖巧正太" |
| `voice_speed` | Sprechgeschwindigkeit. Gültiger Bereich: 0.8~2.0, auf eine Dezimalstelle genau. (Standard: 1) | FLOAT | Nein | 0.8-2.0 |

**Videoanforderungen:**

- Die Videodatei darf nicht größer als 100MB sein
- Höhe/Breite sollte zwischen 720px und 1920px liegen
- Dauer sollte zwischen 2s und 10s liegen

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `output` | Generiertes Video mit lippensynchronisiertem Audio | VIDEO |
| `video_id` | Eindeutiger Bezeichner für das generierte Video | STRING |
| `duration` | Dauerinformationen für das generierte Video | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/de.md)

---
**Source fingerprint (SHA-256):** `28a7be92d7e8a57efeb7e2913124e4373dfc75fbdba6ff7036fafb3a8ae43a60`
