# Audio latent YuE2 vide

Ce nœud crée un latent audio vide pour YuE2, dimensionné selon une durée et une taille de lot choisies. Il produit des données audio silencieuses de remplacement que les nœuds suivants peuvent remplir lors de la génération audio.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `seconds` | Longueur du latent audio à créer, en secondes (valeur par défaut : 120.0). Le nombre de trames latentes est calculé à partir de cette valeur, avec un minimum de 1 trame. | FLOAT | Oui | 0.04 à 1000.0 (pas de 0.04) |
| `batch_size` | Nombre de latents audio à créer dans un lot (valeur par défaut : 1). | INT | Oui | 1 à 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `LATENT` | Un latent audio vide contenant un tenseur de zéros, dimensionné par `batch_size` et le nombre de trames dérivé de `seconds`. Il est étiqueté comme type audio avec un ratio de réduction temporelle de 1920. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyYuE2LatentAudio/fr.md)

---
**Source fingerprint (SHA-256):** `3397e3feb534c87d9790bbfe36e8e641476d9b6aa00d75a4e6d0c32f4a948563`
