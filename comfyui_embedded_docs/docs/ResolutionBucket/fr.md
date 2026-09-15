# Regroupement par résolution

Ce nœud organise une liste d’images latentes et leurs données de conditionnement correspondantes par résolution. Il regroupe les éléments qui partagent la même hauteur et la même largeur, créant des lots distincts pour chaque résolution unique. Ce processus est utile pour préparer les données à un entraînement efficace, car il permet aux modèles de traiter ensemble plusieurs éléments de même taille.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `latents` | Liste de dictionnaires latents à regrouper par résolution. | LATENT | Oui | N/A |
| `conditioning` | Liste de listes de conditionnement (doit correspondre à la longueur de `latents`). | CONDITIONING | Oui | N/A |

**Remarque :** Les deux entrées sont de type liste, ce qui signifie que le nœud reçoit une liste d’éléments pour chacune. Le nombre d’éléments de la liste `latents` doit correspondre exactement au nombre d’éléments de la liste `conditioning` ; si les nombres ne correspondent pas, le nœud lève une erreur. Chaque dictionnaire latent peut contenir un lot d’échantillons, et la liste de conditionnement correspondante doit contenir un nombre correspondant d’éléments de conditionnement pour ce lot, puisque chaque échantillon du lot est associé à sa propre entrée de conditionnement. Les échantillons latents peuvent avoir une forme (B, C, H, W) pour les images ou (B, T, C, H, W) pour les vidéos ; le nœud les regroupe uniquement par hauteur et largeur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `latents` | Liste de dictionnaires latents mis en lots, un par groupe de résolution. | LATENT |
| `conditioning` | Liste de listes de conditionnement, une par groupe de résolution. | CONDITIONING |

**Remarque :** Les deux sorties sont de type liste. Chaque liste de sortie contient une entrée par résolution unique (hauteur et largeur) trouvée dans l’entrée, dans l’ordre où les résolutions ont été rencontrées pour la première fois. Les latents de chaque groupe sont empilés selon une nouvelle dimension de lot.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/fr.md)

---
**Source fingerprint (SHA-256):** `11687f9916895136c7c5b8146cd7519cbf6c296720e453bac52fe4da237403cd`
