# Synchronisation labiale Kling vidéo avec texte

Le nœud Kling Lip Sync Text to Video synchronise les mouvements de la bouche dans un fichier vidéo afin qu'ils correspondent à une invite textuelle. Il prend une vidéo d'entrée et génère une nouvelle vidéo dans laquelle les mouvements labiaux du personnage sont alignés sur le texte fourni. Le nœud utilise la synthèse vocale pour créer une synchronisation de parole d'aspect naturel.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | Fichier vidéo d'entrée pour la synchronisation labiale. La vidéo doit avoir une hauteur/largeur comprise entre 720 px et 1920 px, une durée comprise entre 2 s et 10 s, et ne pas dépasser 100 Mo. | VIDEO | Oui | - |
| `text` | Contenu textuel pour la génération de vidéo avec synchronisation labiale. Requis lorsque le mode est text2video. Longueur maximale : 120 caractères. | STRING | Oui | - |
| `voice` | Sélection de la voix pour l'audio de synchronisation labiale (par défaut : « Melody »). Comprend des options de voix en anglais et en chinois. | COMBO | Non | "Melody"<br>"Sunny"<br>"Sage"<br>"Ace"<br>"Blossom"<br>"Peppy"<br>"Dove"<br>"Shine"<br>"Anchor"<br>"Lyric"<br>"Tender"<br>"Siren"<br>"Zippy"<br>"Bud"<br>"Sprite"<br>"Candy"<br>"Beacon"<br>"Rock"<br>"Titan"<br>"Grace"<br>"Helen"<br>"Lore"<br>"Crag"<br>"Prattle"<br>"Hearth"<br>"The Reader"<br>"Commercial Lady"<br>"阳光少年"<br>"懂事小弟"<br>"运动少年"<br>"青春少女"<br>"温柔小妹"<br>"元气少女"<br>"阳光男生"<br>"幽默小哥"<br>"文艺小哥"<br>"甜美邻家"<br>"温柔姐姐"<br>"职场女青"<br>"活泼男童"<br>"俏皮女童"<br>"稳重老爸"<br>"温柔妈妈"<br>"严肃上司"<br>"优雅贵妇"<br>"慈祥爷爷"<br>"唠叨爷爷"<br>"唠叨奶奶"<br>"和蔼奶奶"<br>"东北老铁"<br>"重庆小伙"<br>"四川妹子"<br>"潮汕大叔"<br>"台湾男生"<br>"西安掌柜"<br>"天津姐姐"<br>"新闻播报男"<br>"译制片男"<br>"撒娇女友"<br>"刀片烟嗓"<br>"乖巧正太" |
| `voice_speed` | Débit de parole. Plage valide : 0,8~2,0, précis à une décimale. (par défaut : 1) | FLOAT | Non | 0.8-2.0 |

**Exigences relatives à la vidéo :**

- Le fichier vidéo ne doit pas dépasser 100 Mo
- La hauteur/largeur doit être comprise entre 720 px et 1920 px
- La durée doit être comprise entre 2 s et 10 s

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Vidéo générée avec audio synchronisé sur les lèvres | VIDEO |
| `video_id` | Identifiant unique de la vidéo générée | STRING |
| `duration` | Informations sur la durée de la vidéo générée | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `28a7be92d7e8a57efeb7e2913124e4373dfc75fbdba6ff7036fafb3a8ae43a60`
