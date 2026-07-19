# Extension vidéo Grok

Le nœud Grok Video Extend utilise un modèle d’IA pour créer une continuation fluide d’une vidéo existante. Vous fournissez une courte vidéo et une description textuelle de ce qui doit se passer ensuite, et le nœud génère un nouveau clip vidéo qui fait suite à l’original.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `invite` | Description textuelle de ce qui doit se passer ensuite dans la vidéo. | STRING | Oui | N/A |
| `vidéo` | Vidéo source à étendre. Format MP4, 2 à 15 secondes. | VIDEO | Oui | N/A |
| `modèle` | Le modèle à utiliser pour l’extension vidéo. Lorsqu’il est sélectionné, il révèle un paramètre `duration` imbriqué. | COMBO | Oui | `"grok-imagine-video"` |
| `graine` | Graine déterminant si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0). | INT | Non | 0 à 2147483647 |

**Contraintes des paramètres :**
*   L’entrée `video` doit être un fichier MP4 d’une durée comprise entre 2 et 15 secondes et ne peut pas dépasser 50 Mo.
*   Le `prompt` doit contenir au moins un caractère (les espaces blancs sont supprimés).
*   Le paramètre `model` est une liste déroulante dynamique. La sélection de l’option "grok-imagine-video" révèle un paramètre `duration` imbriqué, qui contrôle la durée de l’extension en secondes (par défaut : 8, plage : 2 à 10).

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La nouvelle extension vidéo générée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/fr.md)

---
**Source fingerprint (SHA-256):** `a33383be0eb6857538a75e1b901ee58df0153dfeaf95a7ee19933d651b745b5f`
