# Kling Omni Image vers Vidéo (Pro)

Ce nœud utilise le modèle Kling AI pour générer une vidéo à partir d'une invite textuelle et jusqu'à sept images de référence. Il vous permet de contrôler le rapport d'aspect, la durée et la résolution de la vidéo, et éventuellement d'utiliser des storyboards ou de générer de l'audio. Le nœud envoie la requête à une API externe et renvoie la vidéo générée.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `model_name` | Le modèle Kling spécifique à utiliser pour la génération vidéo (par défaut : `"kling-v3-omni"`). | COMBO | Oui | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Une invite textuelle décrivant le contenu de la vidéo. Elle peut inclure des descriptions positives et négatives. Ignorée lorsque les storyboards sont activés. Les espaces réservés tels que `@image` ou `@video` (éventuellement numérotés) sont automatiquement convertis au format compatible avec l'API. Doit contenir entre 1 et 2500 caractères (peut être vide lorsque les storyboards sont activés). | STRING | Oui | 1 à 2500 caractères (0 à 2500 lorsque les storyboards sont activés) |
| `aspect_ratio` | Le rapport d'aspect souhaité pour la vidéo générée. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | La durée de la vidéo en secondes, ajustée avec un curseur (par défaut : 5). | INT | Oui | 3 à 15 |
| `reference_images` | Jusqu'à 7 images de référence. Chaque image doit faire au moins 300x300 pixels et avoir un rapport d'aspect compris entre 1:2.5 et 2.5:1. | IMAGE | Oui | 1 à 7 images |
| `resolution` | La résolution de sortie de la vidéo (par défaut : `"1080p"`). | COMBO | Non | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Génère une série de segments vidéo avec des invites et des durées individuelles. Pris en charge uniquement pour `kling-v3-omni`. Lorsque cette option est activée, le `prompt` global est ignoré, et la durée totale de tous les segments de storyboard doit être égale à la `duration` globale (par défaut : `"disabled"`). | DYNAMIC_COMBO | Non | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generate_audio` | Génère de l'audio pour la vidéo. Pris en charge uniquement pour `kling-v3-omni` (par défaut : false). | BOOLEAN | Non | `true`<br>`false` |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine (par défaut : 0). | INT | Non | 0 à 2147483647 |

### Entrées de storyboard

Lorsque `storyboards` est activé, les entrées suivantes apparaissent pour chaque segment de storyboard sélectionné. N va de 1 jusqu'au nombre sélectionné de storyboards.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `storyboard_N_prompt` | Invite pour le segment de storyboard N. 512 caractères max. | STRING | Oui | 1 à 512 caractères |
| `storyboard_N_duration` | Durée pour le segment de storyboard N en secondes (par défaut : 4). | INT | Oui | 1 à 15 |

**Remarque :** L'entrée `reference_images` accepte un maximum de 7 images. Si davantage d'images sont fournies, le nœud renvoie une erreur. Chaque image est validée pour ses dimensions minimales (300x300 pixels) et son rapport d'aspect (entre 1:2.5 et 2.5:1).

**Contraintes spécifiques au modèle :**
- `kling-video-o1` ne prend pas en charge les durées supérieures à 10 secondes.
- `kling-video-o1` ne prend pas en charge la génération audio.
- `kling-video-o1` ne prend pas en charge la résolution 4k.
- `kling-video-o1` ne prend pas en charge les storyboards.

**Contrainte des storyboards :** La durée totale de tous les segments de storyboard doit être égale à la valeur globale de `duration`. Si la somme ne correspond pas, le nœud renvoie une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `ccf7881065d2a365cdaa0e164b8b1d46c67985067866ab0fe91d492a62015f07`
