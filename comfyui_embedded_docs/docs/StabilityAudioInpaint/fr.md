> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioInpaint/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI, en respectant scrupuleusement les règles fournies :

Transforme une partie d'un échantillon audio existant à l'aide d'instructions textuelles. Ce nœud vous permet de modifier des sections spécifiques d'un fichier audio en fournissant des descriptions textuelles, effectuant ainsi un "inpainting" ou une régénération des parties sélectionnées tout en préservant le reste de l'audio.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | COMBO | Oui | "stable-audio-2.5" | Le modèle d'IA à utiliser pour l'inpainting audio. |
| `prompt` | STRING | Oui |  | Description textuelle guidant la transformation de l'audio (par défaut : vide). |
| `audio` | AUDIO | Oui |  | Fichier audio d'entrée à transformer. L'audio doit durer entre 6 et 190 secondes. |
| `duration` | INT | Non | 1-190 | Contrôle la durée en secondes de l'audio généré (par défaut : 190). |
| `seed` | INT | Non | 0-4294967294 | La graine aléatoire utilisée pour la génération (par défaut : 0). |
| `steps` | INT | Non | 4-8 | Contrôle le nombre d'étapes d'échantillonnage (par défaut : 8). |
| `mask_start` | INT | Non | 0-190 | Position de début en secondes de la section audio à transformer (par défaut : 30). |
| `mask_end` | INT | Non | 0-190 | Position de fin en secondes de la section audio à transformer (par défaut : 190). |

**Remarque :** La valeur de `mask_end` doit être supérieure à la valeur de `mask_start`. L'audio d'entrée doit avoir une durée comprise entre 6 et 190 secondes.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `audio` | AUDIO | La sortie audio transformée, avec la section spécifiée modifiée selon le texte de description. |

---
**Source fingerprint (SHA-256):** `6589fdbff8387e403055c711a61bb3000d87e5f8cd3753d6e665b723be6f43e2`
