# Flux2Scheduler

Flux2Scheduler génère une séquence de niveaux de bruit (sigmas) pour le processus de débruitage, spécialement conçue pour le modèle Flux. Il calcule un programme basé sur le nombre d'étapes de débruitage et les dimensions de l'image cible, ce qui influence la progression de l'élimination du bruit lors de la génération d'images.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `étapes` | Le nombre d'étapes de débruitage à effectuer. Une valeur plus élevée conduit généralement à des résultats plus détaillés mais prend plus de temps à traiter (par défaut : 20). | INT | Oui | 1 à 4096 |
| `largeur` | La largeur de l'image à générer, en pixels. Cette valeur influence le calcul du programme de bruit (par défaut : 1024). | INT | Oui | 16 à 16384 |
| `hauteur` | La hauteur de l'image à générer, en pixels. Cette valeur influence le calcul du programme de bruit (par défaut : 1024). | INT | Oui | 16 à 16384 |

Remarque : Le programme est calculé à partir de la longueur de la séquence d'image, qui est dérivée de `width` et `height` comme `(width * height) / 256`, reflétant le sous-échantillonnage latent 16x du modèle. Des images plus grandes produisent des séquences plus longues, ce qui décale le programme de bruit en conséquence.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sigmas` | Une séquence de valeurs de niveau de bruit (sigmas) qui définissent le programme de débruitage pour l'échantillonneur. | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/fr.md)

---
**Source fingerprint (SHA-256):** `9606177f37f7bc03aef524623f03b7f24bcdc3d9327dcdf74863fe2befeb2b65`
