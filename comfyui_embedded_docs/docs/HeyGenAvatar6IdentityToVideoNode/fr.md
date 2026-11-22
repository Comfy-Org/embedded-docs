# HeyGen Avatar 6 Identity to Video

Générez une vidéo parlante d'un avatar HeyGen avec Avatar 6. Choisissez l'une des apparences intégrées compatibles avec Avatar 6 ou collez votre propre ID d'avatar HeyGen, puis pilotez-le avec un script texte ou votre propre audio.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Sélecteur de modèle. `"heygen-avatar-6-turbo"` est le palier moins cher et plus rapide ; les deux modèles acceptent les mêmes entrées et résolutions. | COMBO | Oui | `"heygen-avatar-6"`<br>`"heygen-avatar-6-turbo"` |
| `avatar` | Apparence d'avatar à présenter. Les 19 apparences intégrées compatibles avec Avatar 6 sont listées directement ; `custom avatar` révèle `custom_avatar_id` pour une apparence que vous avez créée dans HeyGen. | DYNAMIC_COMBO | Oui | 19 apparences intégrées<br>`custom avatar` |
| `parole` | Pilotez l'avatar avec un script texte (synthèse vocale HeyGen) ou votre propre audio. Nom affiché : source vocale. | DYNAMIC_COMBO | Oui | `"script"`<br>`"audio"` |
| `résolution` | Résolution de la vidéo de sortie. Par défaut : `"1080p"`. | COMBO | Oui | `"1080p"`<br>`"2k"` |
| `aspect_ratio` | Format d'image de la vidéo de sortie. `"auto"` suit la séquence vidéo d'origine de l'apparence d'avatar. Par défaut : `"auto"`. | COMBO | Oui | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `motion_prompt` | Indications facultatives pour les gestes, l'expression, la posture et les mouvements de caméra. Par défaut : chaîne vide. | STRING | Oui | Texte multiligne |
| `motion_expressiveness` | `"less"` produit des gestes moins nombreux et plus petits. Le prompt de mouvement prévaut là où les deux se chevauchent. Par défaut : `"default"`. | COMBO | Oui | `"less"`<br>`"default"` |
| `graine` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

### Entrées `custom avatar`

Ces entrées apparaissent lorsque `avatar` est défini sur `custom avatar`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `custom_avatar_id` | ID d'apparence d'avatar HeyGen compatible avec Avatar 6, par exemple une apparence créée avec HeyGen Create Avatar. Par défaut : chaîne vide. | STRING | Oui | - |

### Entrées de parole `script`

Ces entrées apparaissent lorsque `speech` est défini sur `"script"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `text` | Texte que l'avatar doit prononcer. Par défaut : chaîne vide. | STRING | Oui | Jusqu'à 5000 caractères |
| `voice` | Voix pour le script. L'option par défaut utilise la voix attribuée à l'avatar par HeyGen ; les avatars créés avec HeyGen Create Avatar n'en ont aucune, il faut donc leur choisir une voix. | COMBO | Oui | `"(avatar's default voice)"` ainsi que la liste générale des voix de HeyGen |
| `custom_voice_id` | ID de voix HeyGen facultatif. Lorsqu'il est défini, il remplace la voix sélectionnée ci-dessus. Par défaut : chaîne vide. | STRING | Non | - |
| `voice_speed` | Multiplicateur de vitesse de la parole. Par défaut : 1.0. | FLOAT | Non | 0.5 à 1.5 (pas : 0.05) |

### Entrées de parole `audio`

Ces entrées apparaissent lorsque `speech` est défini sur `"audio"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `audio` | Parole pour l'avatar. La durée de la vidéo suit celle de l'audio. | AUDIO | Oui | 0.5 seconde à 10 minutes |

**Contraintes et comportement :**

* `custom avatar` nécessite un ID d'avatar non vide, sinon le nœud génère une erreur.
* Un script est limité à 5000 caractères, et l'audio à 10 minutes.
* La tarification est calculée par seconde de vidéo de sortie et dépend du modèle et de la résolution.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo parlante générée, téléchargée depuis HeyGen une fois le rendu terminé. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatar6IdentityToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `952146c3790333883ad08b7031853eb7021c8d18c59e58389b5d57b548820944`
