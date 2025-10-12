> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomNoise/fr.md)

Le nœud RandomNoise génère des motifs de bruit aléatoire basés sur une valeur de seed. Il crée un bruit reproductible qui peut être utilisé pour diverses tâches de traitement et de génération d'images. La même seed produira toujours le même motif de bruit, permettant d'obtenir des résultats cohérents sur plusieurs exécutions.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `graine_de_bruit` | INT | Oui | 0 à 18446744073709551615 | La valeur de seed utilisée pour générer le motif de bruit aléatoire (par défaut : 0). La même seed produira toujours la même sortie de bruit. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `noise` | NOISE | Le motif de bruit aléatoire généré basé sur la valeur de seed fournie. |