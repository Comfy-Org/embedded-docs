# Flux2Scheduler

Le nœud Flux2Scheduler génère une séquence de niveaux de bruit (sigmas) pour le processus de débruitage, spécifiquement adaptée au modèle Flux2. Il calcule un programme en fonction du nombre d'étapes de débruitage et des dimensions de l'image cible, ce qui influence la progression de l'élimination du bruit pendant la génération de l'image.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `steps` | Le nombre d'étapes de débruitage à effectuer. Une valeur plus élevée conduit généralement à des résultats plus détaillés mais prend plus de temps à traiter (par défaut : 20). | INT | Oui | 1 à 4096 |
| `width` | La largeur de l'image à générer, en pixels. Cette valeur influence le calcul du programme de bruit (par défaut : 1024). | INT | Oui | 16 à 16384 (MAX_RESOLUTION) |
| `height` | La hauteur de l'image à générer, en pixels. Cette valeur influence le calcul du programme de bruit (par défaut : 1024). | INT | Oui | 16 à 16384 (MAX_RESOLUTION) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sigmas` | Une séquence de valeurs de niveau de bruit (sigmas) qui définit le programme de débruitage pour l'échantillonneur. La sortie contient une valeur de plus que le nombre d'étapes (`steps + 1`). | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/fr.md)

---
**Source fingerprint (SHA-256):** `9606177f37f7bc03aef524623f03b7f24bcdc3d9327dcdf74863fe2befeb2b65`
