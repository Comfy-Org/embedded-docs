# WanMoveConcatTrack

Le nœud **WanMoveConcatTrack** combine deux ensembles de données de suivi de mouvement en une seule séquence plus longue. Il fonctionne en joignant les chemins de suivi et les masques de visibilité des pistes d’entrée le long de leurs dimensions respectives. Si une seule entrée de pistes est fournie, il transmet simplement ces données telles quelles.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `pistes_1` | Le premier ensemble de données de suivi de mouvement à concaténer. | TRACKS | Oui |  |
| `pistes_2` | Un second ensemble facultatif de données de suivi de mouvement. S’il n’est pas fourni, `tracks_1` est transmis directement à la sortie. | TRACKS | Non |  |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `tracks` | Les données de suivi de mouvement concaténées, contenant le `track_path` et la `track_visibility` combinés des entrées. | TRACKS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/fr.md)

---
**Source fingerprint (SHA-256):** `0507c42dce5d481fe5dc5aa1116c9df279f236419f548ea3eff5d824d0d22653`
