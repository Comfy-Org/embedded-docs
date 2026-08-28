# ConcaténationLatente

Le nœud LatentConcat combine deux échantillons latents en les joignant le long d'une dimension choisie. Il prend deux entrées latentes et les concatène le long de l'axe x, y ou t, avec la possibilité de contrôler quel échantillon apparaît en premier. Le nœud ajuste automatiquement la taille du lot de la seconde entrée pour correspondre à la première avant d'effectuer la concaténation.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `échantillons1` | Le premier échantillon latent à concaténer | LATENT | Oui | - |
| `échantillons2` | Le deuxième échantillon latent à concaténer | LATENT | Oui | - |
| `dim` | La dimension le long de laquelle concaténer les échantillons latents. Les valeurs positives (x, y, t) placent samples1 avant samples2 dans le résultat. Les valeurs négatives (-x, -y, -t) placent samples2 avant samples1. La correspondance des dimensions est : x = largeur, y = hauteur, t = temps/images | COMBO | Oui | `"x"`<br>`"-x"`<br>`"y"`<br>`"-y"`<br>`"t"`<br>`"-t"` |

**Remarque :** Le deuxième échantillon latent (`samples2`) est automatiquement répété si nécessaire pour correspondre à la taille du lot du premier échantillon latent (`samples1`) avant la concaténation.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Les échantillons latents concaténés résultant de la combinaison des deux échantillons d'entrée le long de la dimension spécifiée | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentConcat/fr.md)

---
**Source fingerprint (SHA-256):** `dfe27f76ad12e16623d62c9e7f0b2772df6ecadb543a4eee430bc38ab04a12f2`
