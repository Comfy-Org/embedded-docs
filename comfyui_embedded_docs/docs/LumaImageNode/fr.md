Génère des images de manière synchrone en fonction d’un prompt textuel et d’un rapport hauteur/largeur. Ce nœud crée des images à partir de descriptions textuelles et permet de contrôler les dimensions et le style de l’image via diverses entrées de référence, notamment des images de personnage et de style.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `invite` | Prompt pour la génération d’image (par défaut : chaîne vide). Doit comporter au moins 3 caractères. | STRING | Oui | - |
| `modèle` | Sélection du modèle pour la génération d’image. Différents modèles ont des coûts différents. | COMBO | Oui | `photon-flash-1`<br>`photon-1`<br>`photon` |
| `ratio_d'aspect` | Rapport hauteur/largeur de l’image générée (par défaut : `16:9`) | COMBO | Oui | `16:9`<br>`1:1`<br>`4:3`<br>`3:2`<br>`21:9`<br>`9:16`<br>`3:4`<br>`2:3`<br>`9:21` |
| `graine` | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0) | INT | Oui | 0 à 18446744073709551615 |
| `poids_image_de_style` | Poids de l’image de style. Ignoré si aucune `image_de_style` n’est fournie (par défaut : 1.0) | FLOAT | Non | 0.0 à 1.0 |
| `référence_image_luma` | Connexion du nœud de référence Luma pour influencer la génération avec des images d’entrée ; jusqu’à 4 images peuvent être prises en compte. | LUMA_REF | Non | - |
| `image_de_style` | Image de référence de style ; une seule image sera utilisée. | IMAGE | Non | - |
| `image_de_personnage` | Images de référence de personnage ; peut être un lot de plusieurs images, jusqu’à 4 images peuvent être prises en compte. | IMAGE | Non | - |

**Contraintes des paramètres :**

- Le `prompt` doit comporter au moins 3 caractères après suppression des espaces.
- Le paramètre `image_luma_ref` peut accepter jusqu’à 4 images de référence.
- Le paramètre `character_image` peut accepter jusqu’à 4 images de référence de personnage.
- Le paramètre `style_image` n’accepte qu’une seule image de référence de style.
- Le paramètre `style_image_weight` n’est utilisé que lorsque `style_image` est fournie.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | L’image générée en fonction des paramètres d’entrée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode/fr.md)

---
**Source fingerprint (SHA-256):** `f7878cd4df62c2f364e4e404215b18bf2f5745fb071ae2cd931d5e34b84eab46`
