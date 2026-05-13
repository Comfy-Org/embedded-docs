> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageToVideoNode/fr.md)

Ce nœud utilise le modèle Kling AI pour générer une vidéo à partir d’un prompt textuel et de jusqu’à sept images de référence. Il permet de contrôler le format d’image, la durée, la résolution de la vidéo, et éventuellement d’utiliser des storyboards ou de générer de l’audio. Le nœud envoie la requête à une API externe et retourne la vidéo générée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model_name` | COMBO | Oui | `"kling-v3-omni"`<br>`"kling-video-o1"` | Le modèle Kling spécifique à utiliser pour la génération vidéo (par défaut : "kling-v3-omni"). |
| `prompt` | STRING | Oui | - | Un prompt textuel décrivant le contenu de la vidéo. Peut inclure des descriptions positives et négatives. Le texte est automatiquement normalisé et doit contenir entre 1 et 2500 caractères. Ignoré lorsque les storyboards sont activés. |
| `aspect_ratio` | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Le format d’image souhaité pour la vidéo générée. |
| `duration` | INT | Oui | 3 à 15 | La durée de la vidéo en secondes. La valeur peut être ajustée avec un curseur (par défaut : 5). |
| `reference_images` | IMAGE | Oui | - | Jusqu’à 7 images de référence. Chaque image doit faire au moins 300x300 pixels et avoir un rapport hauteur/largeur compris entre 1:2.5 et 2.5:1. |
| `resolution` | COMBO | Non | `"4k"`<br>`"1080p"`<br>`"720p"` | La résolution de sortie de la vidéo. Ce paramètre est facultatif (par défaut : "1080p"). |
| `storyboards` | DYNAMIC_COMBO | Non | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` | Génère une série de segments vidéo avec des prompts et durées individuels. Uniquement pris en charge pour `kling-v3-omni`. Lorsque cette option est activée, le `prompt` global est ignoré et la durée totale de tous les segments de storyboard doit correspondre à la `duration` globale. |
| `générer l'audio` | BOOLEAN | Non | `true`<br>`false` | Génère l’audio pour la vidéo. Uniquement pris en charge pour `kling-v3-omni` (par défaut : false). |
| `seed` | INT | Non | 0 à 2147483647 | La graine contrôle si le nœud doit être réexécuté ; les résultats restent non déterministes quelle que soit la graine (par défaut : 0). |

**Remarque :** L’entrée `reference_images` accepte un maximum de 7 images. Si davantage sont fournies, le nœud générera une erreur. Chaque image est validée pour ses dimensions minimales et son rapport hauteur/largeur.

**Contraintes spécifiques au modèle :**
- `kling-video-o1` ne prend pas en charge les durées supérieures à 10 secondes.
- `kling-video-o1` ne prend pas en charge la génération audio.
- `kling-video-o1` ne prend pas en charge la résolution 4k.
- `kling-video-o1` ne prend pas en charge les storyboards.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | Le fichier vidéo généré. |

---
**Source fingerprint (SHA-256):** `80f4568be81b23c75bfff2bd3f21a61b242563c3c9fb1985a03e76ace24dceb2`
