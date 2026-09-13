# Interpolation d’images

Le nœud Frame Interpolate crée de nouvelles trames entre celles existantes dans une séquence d'images, ce qui augmente effectivement la fréquence d'images. Il utilise un modèle d'IA pour prédire l'apparence des trames intermédiaires, ce qui peut servir à créer des effets de ralenti fluides ou à améliorer la fluidité d'une vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `interp_model` | Le modèle d'interpolation de trames à utiliser pour générer des trames intermédiaires | INTERP_MODEL | Oui | - |
| `images` | Un lot d'images consécutives (trames) entre lesquelles interpoler. Nécessite au moins 2 images. Si moins de 2 trames sont fournies, le nœud renvoie les images d'entrée inchangées. | IMAGE | Oui | - |
| `multiplier` | Le facteur multiplicatif à appliquer au nombre de trames. Par exemple, un multiplicateur de 2 double le nombre de trames. (par défaut : 2) | INT | Oui | 2 à 16 |

**Remarque :** Le nœud nécessite au moins 2 trames d'entrée et un `multiplier` d'au moins 2. Si l'une de ces conditions n'est pas remplie, les images d'entrée sont renvoyées inchangées.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `IMAGE` | Un nouveau lot d'images avec les trames interpolées insérées entre les trames d'origine, ce qui donne une séquence plus fluide. Le nombre total de trames de sortie est `(number of input frames - 1) * multiplier + 1`. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/fr.md)

---
**Source fingerprint (SHA-256):** `e0b9dd6ec3b09e665bcc0f95d2b7a0209d9045ba9b96828e46f126e6914f049c`
