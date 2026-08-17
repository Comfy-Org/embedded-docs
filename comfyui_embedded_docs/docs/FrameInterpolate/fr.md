# Interpolation d’images

Le nœud Frame Interpolate crée de nouvelles images entre celles d'une séquence, augmentant ainsi la fréquence d'images. Il utilise un modèle d'IA pour prédire à quoi devraient ressembler les images intermédiaires, ce qui peut être utilisé pour créer des effets de ralenti fluides ou pour augmenter la fluidité d'une vidéo. Pour chaque paire d'images consécutives, le nœud génère `multiplier - 1` nouvelles images et les insère entre les images d'origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `interp_model` | Le modèle d'interpolation de trames à utiliser pour générer les images intermédiaires (par exemple, les modèles RIFE ou FILM) | INTERP_MODEL | Oui | - |
| `images` | Un lot d'images consécutives (trames) entre lesquelles interpoler. Nécessite au moins 2 images ; si moins sont fournies, le nœud renvoie les images d'entrée inchangées. | IMAGE | Oui | - |
| `multiplier` | Le facteur par lequel multiplier le nombre d'images. Par exemple, un multiplicateur de 2 double le nombre d'images. (par défaut : 2) | INT | Oui | 2 à 16 |

Remarque : Le lot d'images d'entrée doit contenir au moins 2 trames, car l'interpolation se fait entre les paires de trames consécutives. Le nombre total de trames en sortie est `(number of input frames - 1) * multiplier + 1`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `IMAGE` | Un nouveau lot d'images avec les trames interpolées insérées entre les trames d'origine, ce qui donne une séquence plus fluide. Le nombre total de trames en sortie est `(number of input frames - 1) * multiplier + 1`. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/fr.md)

---
**Source fingerprint (SHA-256):** `e0b9dd6ec3b09e665bcc0f95d2b7a0209d9045ba9b96828e46f126e6914f049c`
