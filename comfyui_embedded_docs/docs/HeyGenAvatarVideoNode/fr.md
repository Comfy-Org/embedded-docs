# HeyGenAvatarVideoNode

Générer une vidéo de présentateur parlant à partir d'un avatar HeyGen. Ce nœud crée une vidéo d'un avatar IA récitant le texte que vous fournissez ou synchronisant les lèvres sur votre propre audio, en utilisant les moteurs de rendu de HeyGen.

## Entrées

| Paramètre | Description | Type de Données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `moteur` | Moteur de rendu ; chaque choix liste uniquement les avatars qui le prennent en charge. 'auto' propose tous les avatars et sélectionne son meilleur moteur (Avatar IV privilégié). Avatar V offre la plus haute fidélité, Avatar III est le plus abordable. | COMBO | Oui | `"auto"`<br>`"avatar_iv"`<br>`"avatar_iii"`<br>`"avatar_v"` |
| `identifiant_avatar_personnalisé` | Identifiant optionnel d'apparence d'avatar HeyGen. Lorsqu'il est défini, il remplace l'avatar sélectionné ci-dessus. N'importe laquelle des 3000+ apparences publiques de HeyGen (ou vos avatars privés) peut être utilisée. | STRING | Non |  |
| `parole` | Pilote l'avatar avec un script textuel (synthèse vocale HeyGen) ou votre propre audio. | COMBO | Oui | `"script"`<br>`"audio"` |
| `résolution` | Résolution de la vidéo de sortie (par défaut : "1080p"). | COMBO | Non | `"720p"`<br>`"1080p"` |
| `format d’image` | Format d'image de sortie. 'auto' suit le format de la source de l'avatar (par défaut : "auto"). | COMBO | Non | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `couleur de fond` | Couleur de fond unie optionnelle sous forme de code hexadécimal (ex. '#00ff00'). Laissez vide pour conserver le fond d'origine de l'avatar. | STRING | Non |  |
| `graine` | N'est pas envoyé à HeyGen ; modifiez-le pour forcer une nouvelle exécution (par défaut : 42). | INT | Non | Min : 0<br>Max : 2147483647 |

Lorsque `speech` est réglé sur `"script"`, les sous-paramètres suivants sont disponibles :

| Paramètre | Description | Type de Données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `text` | Texte que l'avatar doit prononcer (jusqu'à 5000 caractères). La parole générée doit durer au moins 1 seconde. | STRING | Oui |  |
| `voice` | Voix pour le script. L'option par défaut utilise la voix que HeyGen a attribuée à l'avatar. | COMBO | Oui | Plusieurs options disponibles |
| `custom_voice_id` | Identifiant vocal HeyGen optionnel. Lorsqu'il est défini, il remplace la voix sélectionnée ci-dessus. N'importe quelle voix de la bibliothèque HeyGen (2000+) peut être utilisée. | STRING | Non |  |
| `voice_speed` | Multiplicateur de vitesse de parole (par défaut : 1.0). | FLOAT | Non | Min : 0.5<br>Max : 1.5<br>Pas : 0.05 |

Lorsque `speech` est réglé sur `"audio"`, le sous-paramètre suivant est disponible :

| Paramètre | Description | Type de Données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `audio` | Audio pour la synchronisation labiale de l'avatar, jusqu'à 10 minutes. | AUDIO | Oui |  |

## Sorties

| Nom de Sortie | Description | Type de Données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo générée du présentateur avatar. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatarVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `009bc72b841ca273af83fe6f80fb24d4b11c2efd96c011795b1ff1cf8e66ee61`
