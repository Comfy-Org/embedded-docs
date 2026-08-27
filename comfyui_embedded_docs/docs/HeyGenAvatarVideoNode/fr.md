# Vidéo Avatar HeyGen

Générez une vidéo de présentateur parlant à partir d'un avatar HeyGen. Ce nœud crée une vidéo d'un avatar IA prononçant le texte fourni ou synchronisant les lèvres sur votre propre audio, à l'aide des moteurs de rendu de HeyGen.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `moteur` | Moteur de rendu ; chaque choix n'affiche que les avatars qui le prennent en charge. « auto » propose tous les avatars et sélectionne leur meilleur moteur (Avatar IV privilégié). Avatar V offre la plus haute fidélité, Avatar III est le plus abordable. | DYNAMIC_COMBO | Oui | `"auto"`<br>`"avatar_iv"`<br>`"avatar_iii"`<br>`"avatar_v"` |
| `identifiant_avatar_personnalisé` | ID d'apparence (look) d'avatar HeyGen optionnel. S'il est défini, il remplace l'avatar sélectionné ci-dessus. N'importe laquelle des 3000+ apparences publiques de HeyGen (ou vos avatars privés) peut être utilisée. Par défaut : chaîne vide. | STRING | Non |  |
| `parole` | Pilotez l'avatar avec un script texte (synthèse vocale HeyGen) ou votre propre audio. | DYNAMIC_COMBO | Oui | `"script"`<br>`"audio"` |
| `résolution` | Résolution vidéo de sortie. Par défaut : `"1080p"`. | COMBO | Non | `"720p"`<br>`"1080p"` |
| `format d’image` | Format d'image de sortie. « auto » suit les images sources de l'avatar. Par défaut : `"auto"`. | COMBO | Non | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `couleur de fond` | Couleur d'arrière-plan unie optionnelle, sous forme de code hexadécimal (ex. `"#00ff00"`). Laissez vide pour conserver l'arrière-plan d'origine de l'avatar. Si une valeur est fournie, elle doit commencer par `#`. Par défaut : chaîne vide. | STRING | Non |  |
| `graine` | Non envoyé à HeyGen ; modifiez-le pour forcer une nouvelle exécution. Par défaut : `42`. | INT | Non | Min : 0<br>Max : 2147483647 |

### Entrées `auto`

Lorsque `engine` est `"auto"`, le sous-paramètre suivant est disponible :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `avatar` | Apparence d'avatar pour présenter la vidéo (sélectionnée dans la bibliothèque publique de HeyGen). Le meilleur moteur pris en charge par cette apparence est choisi automatiquement. | COMBO | Oui | Plusieurs options disponibles |

### Entrées `avatar_iv`

Lorsque `engine` est `"avatar_iv"`, le sous-paramètre suivant est disponible :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `avatar` | Apparences d'avatar prenant en charge le moteur Avatar IV. | COMBO | Oui | Plusieurs options disponibles |

### Entrées `avatar_iii`

Lorsque `engine` est `"avatar_iii"`, le sous-paramètre suivant est disponible :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `avatar` | Apparences d'avatar prenant en charge le moteur Avatar III. | COMBO | Oui | Plusieurs options disponibles |

### Entrées `avatar_v`

Lorsque `engine` est `"avatar_v"`, le sous-paramètre suivant est disponible :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `avatar` | Apparences d'avatar prenant en charge le moteur Avatar V. | COMBO | Oui | Plusieurs options disponibles |

### Entrées `script`

Lorsque `speech` est `"script"`, les sous-paramètres suivants sont disponibles :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `text` | Texte que l'avatar doit prononcer (jusqu'à 5000 caractères). La parole générée doit durer au moins 1 seconde. Par défaut : chaîne vide. | STRING | Oui | Min : 1 caractère<br>Max : 5000 caractères |
| `voice` | Voix pour le script. L'option par défaut utilise la voix que HeyGen a attribuée à l'avatar. | COMBO | Oui | `"(avatar's default voice)"`<br>Plusieurs options de voix générales disponibles |
| `custom_voice_id` | ID de voix HeyGen optionnel. S'il est défini, il remplace la voix sélectionnée ci-dessus. N'importe quelle voix de la bibliothèque de HeyGen (2000+) peut être utilisée. Par défaut : chaîne vide. | STRING | Non |  |
| `voice_speed` | Multiplicateur de vitesse de parole. Par défaut : `1.0`. | FLOAT | Non | Min : 0.5<br>Max : 1.5<br>Pas : 0.05 |

### Entrées `audio`

Lorsque `speech` est `"audio"`, le sous-paramètre suivant est disponible :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `audio` | Audio pour la synchronisation labiale de l'avatar, jusqu'à 10 minutes. | AUDIO | Oui |  |

Remarque : `speech` est un sélecteur de source avec deux modes mutuellement exclusifs. En mode `"script"`, `text` est requis (1 à 5000 caractères) ; si `custom_voice_id` est fourni, il remplace `voice`. En mode `"audio"`, l'avatar synchronise ses lèvres sur le clip audio fourni. `background_color` doit être un code couleur hexadécimal commençant par `#` si une valeur est fournie. Lorsque `custom_avatar_id` est défini, il remplace la sélection `avatar`, et le `engine` sélectionné doit être pris en charge par cette apparence d'avatar ; sinon, une erreur est déclenchée (sauf si `engine` est `"auto"`).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo de présentateur avatar générée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatarVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `009bc72b841ca273af83fe6f80fb24d4b11c2efd96c011795b1ff1cf8e66ee61`
