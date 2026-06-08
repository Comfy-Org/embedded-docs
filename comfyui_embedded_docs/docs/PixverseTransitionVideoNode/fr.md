Génère une vidéo de transition entre deux images d'entrée à l'aide de l'API PixVerse. Vous fournissez une image de départ et une image de fin, et le nœud crée une vidéo fluide qui passe de l'une à l'autre, guidée par votre invite textuelle et les paramètres choisis.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `première image` | Image de départ pour la transition vidéo | IMAGE | Oui | - |
| `dernière image` | Image de fin pour la transition vidéo | IMAGE | Oui | - |
| `prompt` | Invite pour la génération vidéo (par défaut : chaîne vide) | STRING | Oui | - |
| `qualité` | Réglage de la qualité vidéo (par défaut : `"540p"`) | COMBO | Oui | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `durée (secondes)` | Durée de la vidéo en secondes | COMBO | Oui | `5`<br>`8` |
| `mode de mouvement` | Style de mouvement pour la transition (par défaut : `"normal"`) | COMBO | Oui | `"normal"`<br>`"fast"` |
| `seed` | Graine pour la génération vidéo (par défaut : 0) | INT | Oui | 0 à 2147483647 |
| `prompt négatif` | Description textuelle facultative des éléments indésirables sur une image (par défaut : chaîne vide) | STRING | Non | - |

**Remarque sur les contraintes des paramètres :** Lors de l'utilisation de la qualité 1080p, le mode de mouvement est automatiquement défini sur `"normal"` et la durée est limitée à 5 secondes. Pour toute durée autre que 5 secondes, le mode de mouvement est également automatiquement défini sur `"normal"`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La vidéo de transition générée | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTransitionVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `0b7f1e11d513c543df144031452bd9cd80e73c596aee8ffe9701bf471bf5983c`
