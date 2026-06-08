Le nœud Flux2Scheduler génère une séquence de niveaux de bruit (sigmas) pour le processus de débruitage, spécialement conçue pour le modèle Flux. Il calcule un échantillonnage basé sur le nombre d'étapes de débruitage et les dimensions de l'image cible, ce qui influence la progression de l'élimination du bruit lors de la génération d'images.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `étapes` | Le nombre d'étapes de débruitage à effectuer. Une valeur plus élevée produit généralement des résultats plus détaillés, mais le traitement prend plus de temps (par défaut : 20). | INT | Oui | 1 à 4096 |
| `largeur` | La largeur de l'image à générer, en pixels. Cette valeur influence le calcul de l'échantillonnage du bruit (par défaut : 1024). | INT | Oui | 16 à 16384 |
| `hauteur` | La hauteur de l'image à générer, en pixels. Cette valeur influence le calcul de l'échantillonnage du bruit (par défaut : 1024). | INT | Oui | 16 à 16384 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `sigmas` | Une séquence de valeurs de niveaux de bruit (sigmas) qui définissent l'échantillonnage de débruitage pour l'échantillonneur. | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/fr.md)

---
**Source fingerprint (SHA-256):** `dbe44a6eb454dd61ab22df5770ad5ac559e03b20fd36d17d33730cdb835f7ede`
