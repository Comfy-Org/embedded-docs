> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/fr.md)

Le nœud SplitSigmasDenoise divise une séquence de valeurs sigma en deux parties en fonction d'un paramètre de force de débruitage. Il sépare les sigmas d'entrée en séquences de sigmas élevés et faibles, où le point de division est déterminé en multipliant le nombre total d'étapes par le facteur de débruitage. Cela permet de séparer l'échelle de bruit en différentes plages d'intensité pour un traitement spécialisé.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `sigmas` | SIGMAS | Oui | - | La séquence d'entrée des valeurs sigma représentant l'échelle de bruit |
| `réduction_du_bruit` | FLOAT | Oui | 0.0 - 1.0 | Le facteur de force de débruitage qui détermine où diviser la séquence sigma (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `low_sigmas` | SIGMAS | La première partie de la séquence sigma contenant les valeurs sigma les plus élevées |
| `low_sigmas` | SIGMAS | La deuxième partie de la séquence sigma contenant les valeurs sigma les plus faibles |