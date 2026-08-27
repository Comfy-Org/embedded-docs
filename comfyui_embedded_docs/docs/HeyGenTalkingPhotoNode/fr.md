# HeyGen Talking Photo

Animez une image fixe d'une personne pour en faire une vidéo parlante avec synchronisation labiale grâce à la technologie Avatar IV de HeyGen. Vous pouvez piloter l'animation avec un script texte que HeyGen convertit en parole, ou fournir votre propre audio pour que l'avatar synchronise les lèvres.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | Image d'une personne à animer. Redimensionnée automatiquement à la baisse si elle dépasse 2K. | IMAGE | Oui | - |
| `speech` | Pilotez l'avatar avec un script texte (synthèse vocale HeyGen) ou votre propre audio. | DYNAMIC_COMBO | Oui | `"script"`<br>`"audio"` |
| `resolution` | Résolution vidéo de sortie (par défaut : `"1080p"`). | COMBO | Non | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Ratio d'aspect de sortie. `"auto"` suit l'image d'entrée (par défaut : `"auto"`). | COMBO | Non | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `expressiveness` | Niveau d'expressivité du visage et des gestes animés (par défaut : `"low"`). | COMBO | Non | `"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Non envoyé à HeyGen ; modifiez-le pour forcer une nouvelle exécution (par défaut : 42). | INT | Non | 0 à 2147483647 |

### Entrées de script

Affichées lorsque `speech` est `"script"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `text` | Texte que l'avatar doit prononcer (jusqu'à 5000 caractères). La parole générée doit durer au moins 1 seconde. (par défaut : vide) | STRING | Oui | 1 à 5000 caractères |
| `voice` | Voix pour le script (les voix les plus populaires de HeyGen). | COMBO | Oui | Plusieurs options disponibles |
| `custom_voice_id` | Identifiant de voix HeyGen facultatif. Lorsqu'il est défini, il remplace la voix sélectionnée ci-dessus. Toute voix de la bibliothèque HeyGen (2000+) peut être utilisée. (par défaut : vide) | STRING | Non | - |
| `voice_speed` | Multiplicateur de vitesse de parole (par défaut : 1.0). | FLOAT | Non | 0,5 à 1,5 (pas de 0,05) |

### Entrées audio

Affichées lorsque `speech` est `"audio"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `audio` | Audio pour que l'avatar synchronise les lèvres, jusqu'à 10 minutes. | AUDIO | Oui | Jusqu'à 10 minutes |

Remarque : lorsque `speech` est `"script"`, `text` doit être spécifié, et une voix est requise via le sélecteur `voice` (en choisissant une voix autre que celle par défaut de l'avatar) ou un `custom_voice_id`. Lorsque `speech` est `"audio"`, `audio` est requis à la place.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Vidéo générée de la photo parlante animée avec une synchronisation labiale. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenTalkingPhotoNode/fr.md)

---
**Source fingerprint (SHA-256):** `2181066a8c6191cfcaa15ece4f89a16c37e76aa22763d6df4007baa20336f05a`
