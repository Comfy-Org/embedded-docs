# StabilityAudioInpaint

Transforme une partie d'un échantillon audio existant à l'aide d'instructions textuelles. Ce nœud vous permet de modifier des sections spécifiques d'un audio en fournissant des prompts descriptifs, réalisant effectivement un « inpainting » ou une régénération des portions sélectionnées tout en préservant le reste de l'audio.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle IA à utiliser pour l'inpainting audio. | STRING | Oui | `"stable-audio-2.5"` |
| `prompt` | Description textuelle guidant la façon dont l'audio doit être transformé (par défaut : vide). La longueur maximale est de 10 000 caractères. | STRING | Oui |  |
| `audio` | Fichier audio d'entrée à transformer. L'audio doit durer entre 6 et 190 secondes. | AUDIO | Oui |  |
| `duration` | Contrôle la durée en secondes de l'audio généré (par défaut : 190). | INT | Non | 1 à 190 |
| `seed` | La graine aléatoire utilisée pour la génération (par défaut : 0). | INT | Non | 0 à 4294967294 |
| `steps` | Contrôle le nombre d'étapes d'échantillonnage (par défaut : 8). | INT | Non | 4 à 8 |
| `mask_start` | Position de début en secondes de la section audio à transformer (par défaut : 30). | INT | Non | 0 à 190 |
| `mask_end` | Position de fin en secondes de la section audio à transformer (par défaut : 190). | INT | Non | 0 à 190 |

**Remarque :** La valeur `mask_end` doit être supérieure à la valeur `mask_start`. L'audio d'entrée doit avoir une durée comprise entre 6 et 190 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `audio` | La sortie audio transformée avec la section spécifiée modifiée selon le prompt. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioInpaint/fr.md)

---
**Source fingerprint (SHA-256):** `3c180043c538311b1808cddd84b0c0ab22a6fa1d943b7f9ddc9edab0fb3413ad`
