# Extension vidéo Grok

Le nœud Grok Video Extend étend une vidéo existante avec une continuation fluide basée sur un prompt textuel. Fournissez une courte vidéo source et décrivez ce qui doit se produire ensuite ; le nœud renvoie un nouveau clip vidéo qui continue à partir de l’original.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `modèle` | Le modèle à utiliser pour l’extension vidéo. La sélection de l’option `"grok-imagine-video"` révèle ses paramètres spécifiques au modèle. | DYNAMIC_COMBO | Oui | `"grok-imagine-video"` |
| `invite` | Description textuelle de ce qui doit se produire ensuite dans la vidéo. | STRING | Oui | N/A |
| `vidéo` | Vidéo source à étendre. Format MP4, 2 à 15 secondes. | VIDEO | Oui | MP4, 2 à 15 secondes, maximum 50 Mo |
| `graine` | Graine pour déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0). | INT | Oui | 0 à 2147483647 |

### Entrées grok-imagine-video

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `duration` | Durée de l’extension en secondes (par défaut : 8). | INT | Oui | 2 à 10 |

**Contraintes des paramètres :**
*   L’entrée `video` doit être un fichier MP4 d’une durée comprise entre 2 et 15 secondes et ne doit pas dépasser 50 Mo.
*   Le `prompt` doit contenir au moins un caractère après suppression des espaces.
*   Le paramètre `model` est un combo dynamique. La sélection de l’option `"grok-imagine-video"` révèle le paramètre imbriqué `duration`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | L’extension vidéo nouvellement générée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoExtendNode/fr.md)

---
**Source fingerprint (SHA-256):** `5009c007b6f93cd44f2742b024b65f1ac92ab9bca3b85a55554b1d99649e323b`
