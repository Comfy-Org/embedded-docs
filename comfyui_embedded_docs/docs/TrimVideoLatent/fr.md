# TrimVideoLatent

---

Le nœud TrimVideoLatent supprime les trames du début d'une représentation latente de vidéo. Il prend un échantillon vidéo latent et supprime un nombre spécifié de trames depuis le début, renvoyant la partie restante de la vidéo. Cela vous permet de raccourcir les séquences vidéo en supprimant les trames initiales.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `échantillons` | La représentation latente de la vidéo d'entrée contenant les trames vidéo à supprimer | LATENT | Oui | - |
| `quantité de découpe` | Le nombre de trames à supprimer depuis le début de la vidéo (par défaut : 0) | INT | Oui | 0 à 99999 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La représentation latente de la vidéo rognée, avec le nombre spécifié de trames supprimées depuis le début | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimVideoLatent/fr.md)

---
**Source fingerprint (SHA-256):** `33b7a899f2002e9a7008f2ca93de853c08dd0629a4c6867fb42aae4ec2eb864b`
