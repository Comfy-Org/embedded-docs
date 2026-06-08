Ce nœud améliore les images basse résolution en les agrandissant en super-résolution, tout en supprimant les artefacts et le bruit. Il utilise une API externe pour traiter l'image et peut ajuster automatiquement la taille d'entrée pour respecter les limites de traitement. La taille de sortie maximale autorisée est de 4 mégapixels.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d'amélioration à utiliser. Le modèle `generative_portrait` est optimisé pour les portraits, tandis que `generative` est un modèle polyvalent. | STRING | Oui | `"generative_portrait"`<br>`"generative"` |
| `image` | L'image d'entrée à améliorer. | IMAGE | Oui | - |
| `facteur_d’agrandissement` | Le facteur d'agrandissement des dimensions de l'image. Un facteur de 1 signifie aucun agrandissement, 2 double les dimensions et 4 les quadruple. | INT | Oui | `1`<br>`2`<br>`4` |
| `réduction_automatique` | Réduit automatiquement l'image d'entrée si la sortie dépasse la limite. Lorsque cette option est activée, le nœud tentera de réduire la taille de l'image d'entrée pour respecter la limite de sortie de 4 mégapixels avant d'appliquer le facteur d'agrandissement demandé. (par défaut : `False`) | BOOLEAN | Non | - |

**Remarque :** Le nœud générera une erreur si la taille de sortie calculée (hauteur d'entrée × facteur d'agrandissement × largeur d'entrée × facteur d'agrandissement) dépasse 4 000 000 pixels (4 MP) et que `auto_downscale` est désactivé. Lorsque `auto_downscale` est activé, le nœud tentera de réduire l'image d'entrée pour respecter la limite avant d'appliquer le facteur d'agrandissement demandé. Si une réduction de plus de 2x serait nécessaire, le nœud réduira plutôt le facteur d'agrandissement.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image de sortie améliorée et agrandie. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawGeneralImageEnhance/fr.md)

---
**Source fingerprint (SHA-256):** `29f927d39777acdfba2aad107027672d281c202ec78e04942e405c2cc64fcee4`
