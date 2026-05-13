> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/fr.md)

Ce document a été généré par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/en.md)

Le nœud WanMoveConcatTrack combine deux ensembles de données de suivi de mouvement en une seule séquence plus longue. Il fonctionne en joignant les chemins de suivi et les masques de visibilité des pistes d'entrée le long de leurs dimensions respectives. Si une seule piste d'entrée est fournie, il transmet simplement ces données sans modification.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `pistes_1` | TRACKS | Oui | | Premier ensemble de données de suivi de mouvement à concaténer. |
| `pistes_2` | TRACKS | Non | | Second ensemble facultatif de données de suivi de mouvement. S'il n'est pas fourni, `pistes_1` est transmis directement à la sortie. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `tracks` | TRACKS | Les données de suivi de mouvement concaténées, contenant les `track_path` et `track_visibility` combinés des entrées. |

---
**Source fingerprint (SHA-256):** `d9b4c00291c6fa8e17bf54ecdcd16f7f6874159fe8cebebe66568dc2a744868f`
