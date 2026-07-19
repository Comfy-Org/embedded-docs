# HeyGenTalkingPhotoNode

Animez une image fixe d'une personne en une vidéo parlante synchronisée labialement grâce à la technologie Avatar IV de HeyGen. Vous pouvez piloter l'animation avec un script textuel que HeyGen convertit en parole, ou fournir votre propre audio pour que l'avatar effectue le lip-sync.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | Image d'une personne à animer. Réduite automatiquement si elle dépasse 2K. | IMAGE | Oui | - |
| `speech` | Piloter l'avatar avec un script textuel (synthèse vocale HeyGen) ou votre propre audio. | COMBO | Oui | `"script"`<br>`"audio"` |
| `text` | Texte que l'avatar doit prononcer (jusqu'à 5000 caractères). La parole générée doit durer au moins 1 seconde. | STRING | Oui (lorsque speech est "script") | - |
| `voice` | Voix pour le script (les voix les plus populaires de HeyGen). | COMBO | Oui (lorsque speech est "script") | Plusieurs options disponibles |
| `custom_voice_id` | Identifiant de voix HeyGen optionnel. Lorsqu'il est défini, il remplace la voix sélectionnée ci-dessus. N'importe quelle voix de la bibliothèque HeyGen (2000+) peut être utilisée. | STRING | Non | - |
| `voice_speed` | Multiplicateur de vitesse de parole (par défaut : 1.0). | FLOAT | Non | 0.5 à 1.5 |
| `audio` | Audio pour le lip-sync de l'avatar, jusqu'à 10 minutes. | AUDIO | Oui (lorsque speech est "audio") | - |
| `resolution` | Résolution vidéo de sortie (par défaut : "1080p"). | COMBO | Non | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Format d'image de sortie. 'auto' suit l'image d'entrée (par défaut : "auto"). | COMBO | Non | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `expressiveness` | Degré d'expressivité du visage et des gestes animés (par défaut : "low"). | COMBO | Non | `"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Non envoyé à HeyGen ; modifiez-le pour forcer une nouvelle exécution (par défaut : 42). | INT | Non | 0 à 2147483647 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Vidéo générée de la photo parlante animée avec parole synchronisée labialement. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenTalkingPhotoNode/fr.md)

---
**Source fingerprint (SHA-256):** `2181066a8c6191cfcaa15ece4f89a16c37e76aa22763d6df4007baa20336f05a`
