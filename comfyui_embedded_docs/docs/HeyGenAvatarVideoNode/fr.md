# Vidéo Avatar HeyGen

```markdown
Générez une vidéo de présentateur parlant à partir d'un avatar HeyGen. Ce nœud crée une vidéo d'un avatar IA prononçant votre texte ou effectuant une synchronisation labiale sur votre propre audio, à l'aide des moteurs de rendu de HeyGen.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `moteur` | Moteur de rendu ; chaque choix ne répertorie que les avatars qui le prennent en charge. « auto » propose tous les avatars et choisit son meilleur moteur (Avatar IV préféré). Avatar V offre la plus haute fidélité, Avatar III est le plus abordable. | DYNAMIC_COMBO | Oui | `"auto"`<br>`"avatar_iv"`<br>`"avatar_iii"`<br>`"avatar_v"` |
| `identifiant_avatar_personnalisé` | Identifiant d'apparence d'avatar HeyGen facultatif. S'il est défini, il remplace l'avatar sélectionné ci-dessus. N'importe laquelle des plus de 3000 apparences publiques de HeyGen (ou vos avatars privés) peut être utilisée. Défaut : `""`. | STRING | Non |  |
| `parole` | Pilotez l'avatar avec un script texte (synthèse vocale HeyGen) ou votre propre audio. Nom d'affichage : « source de la parole ». | DYNAMIC_COMBO | Oui | `"script"`<br>`"audio"` |
| `résolution` | Résolution vidéo de sortie. Défaut : `"1080p"`. | COMBO | Non | `"720p"`<br>`"1080p"` |
| `format d’image` | Format d'image de sortie. « auto » suit la séquence source de l'avatar. Défaut : `"auto"`. | COMBO | Non | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `couleur de fond` | Couleur d'arrière-plan unie facultative sous forme de code hexadécimal (par ex. `"#00ff00"`). Laissez vide pour conserver l'arrière-plan d'origine de l'avatar. Si vous la fournissez, la valeur doit commencer par `#`. Défaut : `""`. | STRING | Non |  |
| `graine` | Non envoyé à HeyGen ; modifiez-le pour forcer une nouvelle exécution. Défaut : `42`. | INT | Non | Min : 0<br>Max : 2147483647 |

### Entrées `auto`

Lorsque `engine` est `"auto"`, le sous-paramètre suivant est disponible :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `avatar` | Apparence d'avatar pour présenter la vidéo (sélectionnée parmi la bibliothèque publique de HeyGen). Le meilleur moteur pris en charge par cette apparence est choisi automatiquement. | COMBO | Oui | Plusieurs options disponibles |

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
| `text` | Texte que l'avatar doit prononcer (jusqu'à 5000 caractères). La parole générée doit durer au moins 1 seconde. Défaut : `""`. | STRING | Oui | Min : 1 caractère<br>Max : 5000 caractères |
| `voice` | Voix pour le script. L'option par défaut utilise la voix attribuée à l'avatar par HeyGen. Ignorée si `custom_voice_id` est défini. | COMBO | Oui | `"(avatar's default voice)"`<br>Plusieurs options vocales générales disponibles |
| `custom_voice_id` | Identifiant de voix HeyGen facultatif. S'il est défini, il remplace la voix sélectionnée ci-dessus. N'importe quelle voix de la bibliothèque de HeyGen (2000+) peut être utilisée. Défaut : `""`. | STRING | Non |  |
| `voice_speed` | Multiplicateur de vitesse de parole. Défaut : `1.0`. | FLOAT | Non | Min : 0.5<br>Max : 1.5<br>Pas : 0.05 |

### Entrées `audio`

Lorsque `speech` est `"audio"`, le sous-paramètre suivant est disponible :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `audio` | Audio pour la synchronisation labiale de l'avatar, jusqu'à 10 minutes. | AUDIO | Oui |  |

Remarque : `engine` et `speech` sont des sélecteurs qui révèlent différents sous-paramètres selon la valeur choisie. Le sélecteur `speech` a deux modes mutuellement exclusifs : en mode `"script"`, `text` est requis ; si `custom_voice_id` est fourni, il remplace `voice`. En mode `"audio"`, l'avatar synchronise les lèvres sur le clip audio fourni. `background_color` doit être un code couleur hexadécimal commençant par `#` lorsqu'elle est fournie. Lorsque `custom_avatar_id` est défini, il remplace la sélection `avatar`, et le moteur `engine` sélectionné doit être pris en charge par cette apparence d'avatar ; sinon, une erreur est levée, sauf si `engine` est `"auto"`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo de présentateur avatar générée. | VIDEO |
```

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatarVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `86dc799d3a8cf2666449b0d422853b12feffb81ce002f84594f9b925d58b522a`
