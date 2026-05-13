> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomNoise/fr.md)

Le nœud RandomNoise génère des motifs de bruit aléatoires basés sur une valeur de graine. Il crée un bruit reproductible pouvant être utilisé pour diverses tâches de traitement et de génération d'images. La même graine produira toujours le même motif de bruit, permettant d'obtenir des résultats cohérents sur plusieurs exécutions.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `graine_de_bruit` | INT | Oui | 0 à 18446744073709551615 | La valeur de graine utilisée pour générer le motif de bruit aléatoire (par défaut : 0). La même graine produira toujours la même sortie de bruit. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `noise` | NOISE | Le motif de bruit aléatoire généré en fonction de la valeur de graine fournie. |

---
**Source fingerprint (SHA-256):** `893d3eefdef78592ba3cc403ec1e4bf3a672607abe79f05db1b65078d6b9ea20`
