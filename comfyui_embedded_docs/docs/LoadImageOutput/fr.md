Voici la traduction en français de la documentation du nœud LoadImageOutput :

Le nœud LoadImageOutput charge des images depuis le dossier de sortie. Lorsque vous cliquez sur le bouton d'actualisation, il met à jour la liste des images disponibles et sélectionne automatiquement la première, facilitant ainsi l'itération parmi vos images générées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | Charge une image depuis le dossier de sortie. Inclut une option de téléchargement et un bouton d'actualisation pour mettre à jour la liste des images. Lorsque le bouton d'actualisation est cliqué, le nœud met à jour la liste des images et sélectionne automatiquement la première, permettant une itération facile. | COMBO | Oui | Plusieurs options disponibles |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image chargée depuis le dossier de sortie | IMAGE |
| `mask` | Le masque associé à l'image chargée | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageOutput/fr.md)

---
**Source fingerprint (SHA-256):** `d1de0140765c9d5dd393715faa84dc5c3f0e49117391b8823a51b176bcb568d8`
