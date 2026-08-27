# Interpolation d’images

Le nœud Frame Interpolate crée de nouvelles images entre les images existantes d'une séquence, augmentant ainsi la cadence d'images. Il utilise un modèle d'IA pour prédire à quoi devraient ressembler les images intermédiaires, ce qui peut être utilisé pour créer des effets de ralenti fluides ou pour améliorer la fluidité d'une vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `interp_model` | Le modèle d'interpolation d'images à utiliser pour générer les images intermédiaires | INTERP_MODEL | Oui | - |
| `images` | Un lot d'images consécutives (frames) entre lesquelles interpoler. Nécessite au moins 2 images. Si moins de 2 images sont fournies, le nœud renvoie les images d'entrée inchangées. | IMAGE | Oui | - |
| `multiplicateur` | Le nombre de fois pour multiplier le nombre d'images. Par exemple, un multiplicateur de 2 double le nombre d'images. (défaut : 2) | INT | Oui | 2 à 16 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `IMAGE` | Un nouveau lot d'images avec les images interpolées insérées entre les images d'origine, produisant une séquence plus fluide. Le nombre total d'images en sortie est `(number of input frames - 1) * multiplier + 1`. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/fr.md)

---
**Source fingerprint (SHA-256):** `e0b9dd6ec3b09e665bcc0f95d2b7a0209d9045ba9b96828e46f126e6914f049c`
