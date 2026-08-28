# LatentCutToBatch

Le nœud LatentCutToBatch divise une représentation latente le long d’une dimension choisie (temps, largeur ou hauteur) en tranches d’une taille spécifiée, puis les empile dans un nouveau batch. Chaque tranche devient un élément distinct du batch, ce qui permet de traiter indépendamment différentes parties d’un échantillon latent.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `samples` | La représentation latente à diviser et à regrouper en batch. | LATENT | Oui | - |
| `dim` | La dimension selon laquelle couper les échantillons latents. `"t"` correspond à la dimension temporelle (frames), `"x"` à la largeur et `"y"` à la hauteur. | COMBO | Oui | `"t"`<br>`"x"`<br>`"y"` |
| `slice_size` | La taille de chaque tranche à découper dans la dimension spécifiée. Si la taille de la dimension n’est pas parfaitement divisible par cette valeur, le reste est ignoré. (par défaut : 1) | INT | Oui | 1 à 16384 (résolution maximale) |

Remarque : L’option `"t"` n’a d’effet que si le latent comprend une dimension temporelle. Si la dimension choisie correspond à la position du batch ou du canal, ou si elle n’existe pas (par exemple, sélectionner `"t"` sur un latent sans frames), le nœud renvoie l’entrée inchangée. Si `slice_size` est supérieur à la taille de la dimension choisie, la dimension entière est utilisée comme une seule tranche. Lorsque la taille de la dimension n’est pas divisible de manière égale par `slice_size`, la partie restante à la fin est ignorée. La taille du batch de sortie est égale à la taille du batch d’entrée multipliée par le nombre de tranches, et la dimension découpée elle-même est réduite à `slice_size`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `samples` | Le batch latent résultant, contenant les échantillons découpés et empilés. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/fr.md)

---
**Source fingerprint (SHA-256):** `873c9bc8391971887f1ab636c086cab86f5504a9c653bc80b54120ee53980bdf`
