# Vidéo Avatar HeyGen

Génère une vidéo de présentateur parlant à partir d'un avatar HeyGen. Ce nœud crée une vidéo d'un avatar IA prononçant le texte que vous fournissez ou synchronisant ses lèvres avec votre propre audio, à l'aide des moteurs de rendu de HeyGen.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `engine` | Moteur de rendu ; chaque choix ne liste que les avatars qui le prennent en charge. `"auto"` propose tous les avatars et sélectionne son meilleur moteur (Avatar IV privilégié). Avatar V offre la plus haute fidélité, Avatar III est le plus abordable. | DYNAMIC_COMBO | Oui | `"auto"`<br>`"avatar_iv"`<br>`"avatar_iii"`<br>`"avatar_v"` |
| `custom_avatar_id` | ID d'apparence d'avatar HeyGen facultatif. Lorsqu'il est défini, remplace l'avatar sélectionné ci-dessus. N'importe laquelle des plus de 3000 apparences publiques de HeyGen (ou vos avatars privés) peut être utilisée. Valeur par défaut : `""`. | STRING | Non |  |
| `speech` | Pilotez l'avatar avec un script texte (synthèse vocale HeyGen) ou votre propre audio. Nom d'affichage : « speech source ». | DYNAMIC_COMBO | Oui | `"script"`<br>`"audio"` |
| `resolution` | Résolution de la vidéo de sortie. Valeur par défaut : `"1080p"`. | COMBO | Non | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Format d'image de la vidéo de sortie. `"auto"` suit la séquence source de l'avatar. Valeur par défaut : `"auto"`. | COMBO | Non | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `background_color` | Couleur d'arrière-plan unie facultative sous forme de code hexadécimal (par ex. `"#00ff00"`). Laissez vide pour conserver l'arrière-plan propre à l'avatar. Si fournie, la valeur doit commencer par `#`. Valeur par défaut : `""`. | STRING | Non |  |
| `seed` | Non envoyé à HeyGen ; modifiez-le pour forcer une nouvelle exécution. Valeur par défaut : `42`. | INT | Non | Min : 0<br>Max : 2147483647 |

### Entrées `auto`

Lorsque `engine` vaut `"auto"`, le sous-paramètre suivant est disponible :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `avatar` | Apparence d'avatar pour présenter la vidéo (sélectionnée dans la bibliothèque publique de HeyGen). Le meilleur moteur pris en charge par cette apparence est choisi automatiquement. | COMBO | Oui | Plusieurs options disponibles |

### Entrées `avatar_iv`

Lorsque `engine` vaut `"avatar_iv"`, le sous-paramètre suivant est disponible :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `avatar` | Apparences d'avatar prenant en charge le moteur Avatar IV. | COMBO | Oui | Plusieurs options disponibles |

### Entrées `avatar_iii`

Lorsque `engine` vaut `"avatar_iii"`, le sous-paramètre suivant est disponible :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `avatar` | Apparences d'avatar prenant en charge le moteur Avatar III. | COMBO | Oui | Plusieurs options disponibles |

### Entrées `avatar_v`

Lorsque `engine` vaut `"avatar_v"`, le sous-paramètre suivant est disponible :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `avatar` | Apparences d'avatar prenant en charge le moteur Avatar V. | COMBO | Oui | Plusieurs options disponibles |

### Entrées `script`

Lorsque `speech` vaut `"script"`, les sous-paramètres suivants sont disponibles :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `text` | Texte que l'avatar doit prononcer (jusqu'à 5000 caractères). La parole générée doit durer au moins 1 seconde. Valeur par défaut : `""`. | STRING | Oui | Min : 1 caractère<br>Max : 5000 caractères |
| `voice` | Voix pour le script. L'option par défaut utilise la voix que HeyGen a attribuée à l'avatar. Ignorée si `custom_voice_id` est défini. | COMBO | Oui | `"(avatar's default voice)"`<br>Plusieurs options de voix générales disponibles |
| `custom_voice_id` | ID de voix HeyGen facultatif. Lorsqu'il est défini, remplace la voix sélectionnée ci-dessus. N'importe quelle voix de la bibliothèque HeyGen (plus de 2000) peut être utilisée. Valeur par défaut : `""`. | STRING | Non |  |
| `voice_speed` | Multiplicateur de vitesse de la parole. Valeur par défaut : `1.0`. | FLOAT | Non | Min : 0.5<br>Max : 1.5<br>Pas : 0.05 |

### Entrées `audio`

Lorsque `speech` vaut `"audio"`, le sous-paramètre suivant est disponible :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `audio` | Audio que l'avatar doit synchroniser avec ses lèvres, jusqu'à 10 minutes. | AUDIO | Oui |  |

Remarque : `engine` et `speech` sont des sélecteurs qui révèlent différents sous-paramètres selon la valeur choisie. Le sélecteur `speech` possède deux modes mutuellement exclusifs : en mode `"script"`, `text` est requis ; si `custom_voice_id` est fourni, il remplace `voice`. En mode `"audio"`, l'avatar synchronise ses lèvres avec le clip audio fourni. `background_color` doit être un code couleur hexadécimal commençant par `#` lorsqu'il est fourni. Lorsque `custom_avatar_id` est défini, il remplace la sélection `avatar`, et le `engine` sélectionné doit être pris en charge par cette apparence d'avatar ; sinon une erreur est levée, sauf si `engine` vaut `"auto"`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo de présentateur avec avatar générée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatarVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `86dc799d3a8cf2666449b0d422853b12feffb81ce002f84594f9b925d58b522a`
