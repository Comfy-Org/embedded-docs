> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/fr.md)

Voici la traduction en français de la documentation du nœud Frame Interpolate :

## Aperçu

Le nœud Frame Interpolate crée de nouvelles images entre les images existantes d'une séquence, augmentant ainsi efficacement la fréquence d'images. Il utilise un modèle d'IA pour prédire l'apparence des images intermédiaires, ce qui permet de créer des effets de ralenti fluides ou d'améliorer la fluidité d'une vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `interp_model` | MODEL | Oui | - | Le modèle d'interpolation d'images à utiliser pour générer les images intermédiaires |
| `images` | IMAGE | Oui | - | Un lot d'images consécutives (images) entre lesquelles interpoler. Nécessite au moins 2 images. |
| `multiplier` | INT | Oui | 2 à 16 | Le nombre de fois pour multiplier le nombre d'images. Par exemple, un multiplicateur de 2 double le nombre d'images. (par défaut : 2) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `IMAGE` | IMAGE | Un nouveau lot d'images avec les images interpolées insérées entre les images originales, résultant en une séquence plus fluide. Le nombre total d'images en sortie est `(nombre d'images d'entrée - 1) * multiplicateur + 1`. |

---
**Source fingerprint (SHA-256):** `05fdac188d9d7c7d5cac9ade55ba22cc743395b3c659a519ca03fe293b9a6e34`
