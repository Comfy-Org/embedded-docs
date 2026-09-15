# NormalizeVideoLatentStart

Ce nœud ajuste les premières trames d'un latent vidéo afin qu'elles ressemblent davantage aux trames qui les suivent. Il calcule la moyenne et la variation à partir d'un ensemble de trames de référence situées plus loin dans la vidéo et applique ces mêmes caractéristiques aux trames de début. Cela aide à réduire les différences entre les trames de début et le reste de la vidéo, créant une transition plus fluide et plus cohérente.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `latent` | La représentation latente vidéo à traiter. | LATENT | Oui | - |
| `start_frame_count` | Nombre de trames latentes à normaliser, compté depuis le début (par défaut : 4). | INT | Oui | 1 à 16384 (résolution maximale) |
| `reference_frame_count` | Nombre de trames latentes après les trames de début à utiliser comme référence (par défaut : 5). | INT | Oui | 1 à 16384 (résolution maximale) |

**Remarque :** Les trames de référence sont prises immédiatement après les trames correspondant à `start_frame_count`. S'il y a moins de trames disponibles que ce que demande `reference_frame_count`, le nœud utilise toutes celles qui sont disponibles (au maximum une de moins que le nombre total de trames du latent). Si le latent vidéo ne contient qu'une seule trame, aucune normalisation n'est effectuée et le latent d'origine est renvoyé inchangé.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `latent` | Le latent vidéo traité avec les trames de début normalisées. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/fr.md)

---
**Source fingerprint (SHA-256):** `383e5a19ee4cd8bdea5983567ddbdc30bb09c373142a1a934cea985f1b9d1b0d`
