# Extension vidéo Grok

Le nœud Grok Video Extend utilise un modèle d'IA pour créer une continuation fluide d'une vidéo existante. Vous fournissez une courte vidéo et une invite texte décrivant ce qui devrait se passer ensuite, et le nœud génère un nouveau clip vidéo qui fait suite à la vidéo d'origine.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle à utiliser pour l'extension vidéo. | DYNAMIC_COMBO | Oui | `"grok-imagine-video"` |
| `invite` | Description textuelle de ce qui doit se passer ensuite dans la vidéo. | STRING | Oui | N/A |
| `vidéo` | Vidéo source à étendre. Format MP4, 2 à 15 secondes. | VIDEO | Oui | N/A |
| `graine` | Graine déterminant si le nœud doit être relancé ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0). | INT | Oui | 0 à 2147483647 |

### Entrées grok-imagine-video

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `duration` | Durée de l'extension en secondes (par défaut : 8). | INT | Oui | 2 à 10 |

**Contraintes de paramètres :**
*   L'entrée `video` doit être un fichier MP4 d'une durée comprise entre 2 et 15 secondes et ne pas dépasser 50 Mo.
*   L'entrée `prompt` doit contenir au moins un caractère (les espaces sont supprimés).
*   Le paramètre `model` est une combinaison dynamique. La sélection de l'option « grok-imagine-video » révèle le paramètre imbriqué `duration`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La nouvelle extension vidéo générée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/fr.md)

---
**Source fingerprint (SHA-256):** `bfaf56dd12afab13c820345587db9ee871db87d60b8dc003f00f035513dbdf61`
