> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageSD_3_5Node/fr.md)

Ce nœud génère des images de manière synchrone en utilisant le modèle Stable Diffusion 3.5 de Stability AI. Il crée des images à partir de descriptions textuelles et peut également modifier des images existantes lorsqu'elles sont fournies en entrée. Le nœud prend en charge différents ratios d'aspect et préréglages de style pour personnaliser le résultat.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | - | Ce que vous souhaitez voir dans l'image de sortie. Une description forte et détaillée qui définit clairement les éléments, les couleurs et les sujets donnera de meilleurs résultats. (valeur par défaut : chaîne vide) |
| `model` | COMBO | Oui | `sd3.5-large`<br>`sd3.5-large-turbo`<br>`sd3.5-medium` | Le modèle Stable Diffusion 3.5 à utiliser pour la génération. |
| `aspect_ratio` | COMBO | Oui | `16:9`<br>`1:1`<br>`21:9`<br>`2:3`<br>`3:2`<br>`4:5`<br>`5:4`<br>`9:16`<br>`9:21` | Ratio d'aspect de l'image générée. (valeur par défaut : 1:1) |
| `style_preset` | COMBO | Non | `3d-model`<br>`analog-film`<br>`anime`<br>`cinematic`<br>`comic-book`<br>`digital-art`<br>`enhance`<br>`fantasy-art`<br>`isometric`<br>`line-art`<br>`low-poly`<br>`modeling-compound`<br>`neon-punk`<br>`origami`<br>`photographic`<br>`pixel-art`<br>`tile-texture`<br>`None` | Style souhaité (facultatif) de l'image générée. Sélectionnez "None" pour aucun préréglage de style. |
| `cfg_scale` | FLOAT | Oui | 1.0 à 10.0 | Degré de fidélité du processus de diffusion au texte de la description (des valeurs plus élevées maintiennent votre image plus proche de votre description). (valeur par défaut : 4.0) |
| `seed` | INT | Oui | 0 à 4294967294 | La graine aléatoire utilisée pour créer le bruit. (valeur par défaut : 0) |
| `image` | IMAGE | Non | - | Image d'entrée facultative pour la génération image-à-image. Lorsqu'elle est fournie, le nœud passe en mode image-à-image et le paramètre `aspect_ratio` est ignoré. |
| `negative_prompt` | STRING | Non | - | Mots-clés de ce que vous ne souhaitez pas voir dans l'image de sortie. Il s'agit d'une fonctionnalité avancée. (valeur par défaut : chaîne vide) |
| `image_denoise` | FLOAT | Non | 0.0 à 1.0 | Débruitage de l'image d'entrée ; 0.0 donne une image identique à l'entrée, 1.0 équivaut à l'absence d'image fournie. (valeur par défaut : 0.5) Ce paramètre est uniquement utilisé lorsqu'une `image` est fournie. |

**Remarque :** Lorsqu'une `image` est fournie, le nœud passe en mode de génération image-à-image et le paramètre `aspect_ratio` est automatiquement déterminé à partir de l'image d'entrée. Lorsqu'aucune `image` n'est fournie, le paramètre `image_denoise` est ignoré.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `image` | IMAGE | L'image générée ou modifiée. |

---
**Source fingerprint (SHA-256):** `80dbb27f19bb3286ee988f020f7f65623a73d7cac77ca0cdfc7a428254102aa3`
