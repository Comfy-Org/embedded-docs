# SkipLayerGuidanceSD3

Le nœud SkipLayerGuidanceSD3 améliore le guidage vers une structure détaillée en appliquant un ensemble supplémentaire de guidage sans classifieur avec des couches ignorées. Cette implémentation expérimentale s'inspire du guidage par attention perturbée (Perturbed Attention Guidance) et fonctionne en contournant sélectivement certaines couches pendant le processus de conditionnement négatif afin d'améliorer les détails structurels dans la sortie générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel appliquer le guidage par couches ignorées | MODEL | Oui | - |
| `couches` | Liste d'indices de couches à ignorer, séparés par des virgules (par défaut : "7, 8, 9") | STRING | Oui | - |
| `échelle` | L'intensité de l'effet de guidage par couches ignorées (par défaut : 3.0) | FLOAT | Oui | 0.0 - 10.0 |
| `pourcentage_de_départ` | Le point de départ de l'application du guidage, exprimé en pourcentage du nombre total d'étapes (par défaut : 0.01) | FLOAT | Oui | 0.0 - 1.0 |
| `pourcentage_de_fin` | Le point d'arrêt de l'application du guidage, exprimé en pourcentage du nombre total d'étapes (par défaut : 0.15) | FLOAT | Oui | 0.0 - 1.0 |


| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec le guidage par couches ignorées appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceSD3/fr.md)

---
**Source fingerprint (SHA-256):** `97c8220abd223bd35b4d0274c2b4536ffb6be7954ccd917943905bd22f60c1a5`
