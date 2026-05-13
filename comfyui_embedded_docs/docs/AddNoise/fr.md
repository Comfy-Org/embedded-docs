> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddNoise/fr.md)

Ce nœud ajoute un bruit contrôlé à une image latente en utilisant un générateur de bruit spécifié et des valeurs sigma. Il traite l'entrée via le système d'échantillonnage du modèle pour appliquer une mise à l'échelle du bruit adaptée à la plage sigma donnée, et renvoie une nouvelle représentation latente avec le bruit appliqué.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle contenant les paramètres d'échantillonnage et les fonctions de traitement |
| `bruit` | NOISE | Oui | - | Le générateur de bruit qui produit le motif de bruit de base |
| `sigmas` | SIGMAS | Oui | - | Valeurs sigma contrôlant l'intensité de la mise à l'échelle du bruit. Si vide, le nœud renvoie l'image latente d'origine inchangée. Lorsque plusieurs sigmas sont fournis, l'échelle de bruit est calculée comme la différence absolue entre la première et la dernière valeur sigma. Lorsqu'un seul sigma est fourni, cette valeur est utilisée directement comme échelle. |
| `image_latente` | LATENT | Oui | - | La représentation latente d'entrée à laquelle le bruit sera ajouté. Les images latentes vides (ne contenant que des zéros) ne sont pas décalées pendant le traitement. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `LATENT` | LATENT | La représentation latente modifiée avec le bruit ajouté. Toute valeur NaN ou infinie dans la sortie est convertie en zéro pour des raisons de stabilité. |

---
**Source fingerprint (SHA-256):** `8f387f95aeec2780d27bee5b954ad2c6cd6daa9242a1ea15697455b157bc80d5`
