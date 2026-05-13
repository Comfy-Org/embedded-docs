> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/fr.md)

Ce nœud organise une liste d'images latentes et leurs données de conditionnement correspondantes en fonction de leur résolution. Il regroupe les éléments partageant la même hauteur et largeur, créant des lots séparés pour chaque résolution unique. Ce processus est utile pour préparer les données en vue d'un entraînement efficace, car il permet aux modèles de traiter ensemble plusieurs éléments de même taille.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `latents` | LATENT | Oui | N/A | Liste de dictionnaires latents à regrouper par résolution. |
| `conditioning` | CONDITIONING | Oui | N/A | Liste de listes de conditionnement (doit correspondre à la longueur des latents). |

**Remarque :** Le nombre d'éléments dans la liste `latents` doit correspondre exactement au nombre d'éléments dans la liste `conditioning`. Chaque dictionnaire latent peut contenir un lot d'échantillons, et la liste de conditionnement correspondante doit contenir un nombre équivalent d'éléments de conditionnement pour ce lot.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `latents` | LATENT | Liste de dictionnaires latents regroupés en lots, un par groupe de résolution. |
| `conditioning` | CONDITIONING | Liste de listes de conditionnement, une par groupe de résolution. |

---
**Source fingerprint (SHA-256):** `2858de5f0827812002ca72ba5d7ce56411d1ef97e9a12a65fc4bea193a1a0ec0`
