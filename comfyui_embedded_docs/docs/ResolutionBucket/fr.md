# Regroupement par résolution

Ce nœud organise une liste de latents et leurs données de conditionnement correspondantes en fonction de leur résolution. Il regroupe les éléments qui partagent la même hauteur et largeur, créant des lots séparés pour chaque résolution unique. Ce processus est utile pour préparer les données à un entraînement efficace, car il permet aux modèles de traiter ensemble plusieurs éléments de même taille.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `latents` | Liste de dictionnaires de latents à regrouper par résolution. | LATENT | Oui | N/A |
| `conditioning` | Liste de listes de conditionnement (doit correspondre à la longueur de la liste `latents`). | CONDITIONING | Oui | N/A |

**Remarque :** Le nombre d'éléments dans la liste `latents` doit correspondre exactement au nombre d'éléments dans la liste `conditioning`. Chaque dictionnaire de latents peut contenir un lot d'échantillons, et la liste de conditionnement correspondante doit contenir un nombre correspondant d'éléments de conditionnement pour ce lot.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `latents` | Liste de dictionnaires de latents regroupés en lots, un par groupe de résolution. | LATENT |
| `conditioning` | Liste de listes de conditionnement, une par groupe de résolution. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/fr.md)

---
**Source fingerprint (SHA-256):** `11687f9916895136c7c5b8146cd7519cbf6c296720e453bac52fe4da237403cd`
