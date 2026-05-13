> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentConcat/fr.md)

Le nœud LatentConcat combine deux échantillons latents en les joignant le long d'une dimension choisie. Il prend deux entrées latentes et les concatène selon l'axe x, y ou t, avec la possibilité de contrôler quel échantillon apparaît en premier. Le nœud ajuste automatiquement la taille du lot de la deuxième entrée pour correspondre à la première avant d'effectuer la concaténation.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `échantillons1` | LATENT | Oui | - | Le premier échantillon latent à concaténer |
| `échantillons2` | LATENT | Oui | - | Le deuxième échantillon latent à concaténer |
| `dim` | COMBO | Oui | `"x"`<br>`"-x"`<br>`"y"`<br>`"-y"`<br>`"t"`<br>`"-t"` | La dimension le long de laquelle concaténer les échantillons latents. Les valeurs positives (x, y, t) placent samples1 avant samples2 dans le résultat. Les valeurs négatives (-x, -y, -t) placent samples2 avant samples1. La correspondance des dimensions est : x = largeur, y = hauteur, t = temps/images |

**Remarque :** Le deuxième échantillon latent (`samples2`) est automatiquement ajusté pour correspondre à la taille du lot du premier échantillon latent (`samples1`) avant la concaténation.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | LATENT | Les échantillons latents concaténés résultant de la combinaison des deux échantillons d'entrée le long de la dimension spécifiée |

---
**Source fingerprint (SHA-256):** `46514ef85887279ec577ad88ac46f1c20f428903ee63b076888d7d5df09fde77`
