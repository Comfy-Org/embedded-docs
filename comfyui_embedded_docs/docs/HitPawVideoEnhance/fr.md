# HitPaw Amélioration Vidéo

Le nœud HitPaw Video Enhance utilise une API externe pour améliorer la qualité des vidéos. Il agrandit les vidéos basse résolution vers une résolution plus élevée, supprime les artefacts visuels et réduit le bruit. Le coût de traitement est calculé par seconde de vidéo d’entrée.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d’IA à utiliser pour l’amélioration vidéo. La sélection d’un modèle révèle un paramètre `resolution` imbriqué. Les modèles disponibles et leurs résolutions prises en charge varient. | DYNAMIC_COMBO | Oui | `"Portrait Restore Model (1x)"`<br>`"Portrait Restore Model (2x)"`<br>`"General Restore Model (1x)"`<br>`"General Restore Model (2x)"`<br>`"General Restore Model (4x)"`<br>`"Ultra HD Model (2x)"`<br>`"Generative Model (1x)"` |
| `vidéo` | Le fichier vidéo d’entrée à améliorer. | VIDEO | Oui | N/D |

### Entrées Portrait Restore, General Restore et Ultra HD Model

Ces options de résolution sont partagées par Portrait Restore Model (1x), Portrait Restore Model (2x), General Restore Model (1x), General Restore Model (2x), General Restore Model (4x) et Ultra HD Model (2x).

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `résolution` | La résolution cible de la vidéo améliorée. La sélection de `"original"` conserve la résolution de la vidéo d’entrée. | COMBO | Oui | `"original"`<br>`"720p"`<br>`"1080p"`<br>`"2K/QHD"`<br>`"4K/UHD"`<br>`"8K"` |

### Entrées Generative Model (1x)

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `résolution` | La résolution cible de la vidéo améliorée. La sélection de `"original"` conserve la résolution de la vidéo d’entrée. L’option `"8K"` n’est pas disponible pour ce modèle. | COMBO | Oui | `"original"`<br>`"720p"`<br>`"1080p"`<br>`"2K/QHD"`<br>`"4K/UHD"` |

**Remarques :**

* La vidéo `video` d’entrée doit avoir une durée comprise entre 0,5 seconde et 60 minutes (3600 secondes).
* La `resolution` sélectionnée doit être au moins aussi grande que les dimensions de la vidéo d’entrée. Pour les vidéos carrées, elle doit être au moins aussi grande que la largeur et la hauteur de la vidéo. Pour les vidéos non carrées, elle doit être au moins aussi grande que la dimension la plus courte de la vidéo. Si la résolution cible est inférieure, une erreur est générée. La sélection de `"original"` conserve la résolution de la vidéo d’entrée.
* Lorsqu’une résolution autre que `"original"` est sélectionnée, les vidéos non carrées sont mises à l’échelle afin que leur dimension la plus courte corresponde à la résolution sélectionnée, tout en préservant le rapport hauteur/largeur. Les vidéos carrées sont mises à l’échelle afin que les deux dimensions correspondent à la taille carrée cible de la résolution sélectionnée (par exemple, `"4K/UHD"` produit 2048×2048).

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | Le fichier vidéo amélioré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawVideoEnhance/fr.md)

---
**Source fingerprint (SHA-256):** `42803c7137d62dbce5021cd2bd9b9fba1a89c80e7b3f237f8a0eb03858c49967`
