Voici la traduction en français de la documentation du nœud ComfyUI, en respectant scrupuleusement les règles fournies :

Transforme une partie d'un échantillon audio existant à l'aide d'instructions textuelles. Ce nœud vous permet de modifier des sections spécifiques d'un fichier audio en fournissant des descriptions textuelles, effectuant ainsi un "inpainting" ou une régénération des parties sélectionnées tout en préservant le reste de l'audio.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d'IA à utiliser pour l'inpainting audio. | COMBO | Oui | "stable-audio-2.5" |
| `prompt` | Description textuelle guidant la transformation de l'audio (par défaut : vide). | STRING | Oui |  |
| `audio` | Fichier audio d'entrée à transformer. L'audio doit durer entre 6 et 190 secondes. | AUDIO | Oui |  |
| `durée` | Contrôle la durée en secondes de l'audio généré (par défaut : 190). | INT | Non | 1-190 |
| `graine` | La graine aléatoire utilisée pour la génération (par défaut : 0). | INT | Non | 0-4294967294 |
| `étapes` | Contrôle le nombre d'étapes d'échantillonnage (par défaut : 8). | INT | Non | 4-8 |
| `début_masque` | Position de début en secondes de la section audio à transformer (par défaut : 30). | INT | Non | 0-190 |
| `fin_masque` | Position de fin en secondes de la section audio à transformer (par défaut : 190). | INT | Non | 0-190 |

**Remarque :** La valeur de `mask_end` doit être supérieure à la valeur de `mask_start`. L'audio d'entrée doit avoir une durée comprise entre 6 et 190 secondes.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `audio` | La sortie audio transformée, avec la section spécifiée modifiée selon le texte de description. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioInpaint/fr.md)

---
**Source fingerprint (SHA-256):** `6589fdbff8387e403055c711a61bb3000d87e5f8cd3753d6e665b723be6f43e2`
