# AjouterBruit

Ce nœud ajoute un bruit contrôlé à une image latente en utilisant un générateur de bruit spécifié et des valeurs sigma. Il traite l'entrée via le système d'échantillonnage du modèle pour appliquer une mise à l'échelle du bruit adaptée à la plage sigma donnée, renvoyant une nouvelle représentation latente avec le bruit appliqué. Ce nœud est actuellement marqué comme expérimental.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle contenant les paramètres d'échantillonnage et les fonctions de traitement | MODEL | Oui | - |
| `bruit` | Le générateur de bruit qui produit le motif de bruit de base | NOISE | Oui | - |
| `sigmas` | Les valeurs sigma contrôlant l'intensité de la mise à l'échelle du bruit. Si vide, le nœud renvoie l'image latente d'origine inchangée. Lorsque plusieurs sigmas sont fournis, l'échelle du bruit est calculée comme la différence absolue entre la première et la dernière valeur sigma. Lorsqu'un seul sigma est fourni, cette valeur est utilisée directement comme échelle. | SIGMAS | Oui | - |
| `image_latente` | La représentation latente d'entrée à laquelle le bruit sera ajouté. Les images latentes vides (contenant uniquement des zéros) ne sont pas modifiées pendant le traitement. | LATENT | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `LATENT` | La représentation latente modifiée avec le bruit ajouté. Toute valeur NaN ou infinie dans la sortie est convertie en zéros par souci de stabilité. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddNoise/fr.md)

---
**Source fingerprint (SHA-256):** `6b11db10af9a2b8ea24dbf3b40c08d7e37de39df746e3966e5bfc94b84dee068`
