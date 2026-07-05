# Flux KV Cache

Le nœud Flux KV Cache permet d'activer une optimisation du cache clé-valeur (KV Cache) pour les modèles de la famille Flux. Cette optimisation améliore les performances lors de l'utilisation d'images de référence en mettant en cache certains calculs, ce qui peut accélérer le processus de génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle sur lequel appliquer l'optimisation du cache KV. | MODEL | Oui |  |


| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec l'optimisation du cache KV activée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKVCache/fr.md)

---
**Source fingerprint (SHA-256):** `530c660ae23607d4035815826ae73cdcbebe7693ba47a3b0fe98e69f329b9e86`
