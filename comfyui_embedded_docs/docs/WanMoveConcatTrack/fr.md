# WanMoveConcatTrack

Le nœud WanMoveConcatTrack combine deux ensembles de données de suivi de mouvement en une seule séquence plus longue. Il fonctionne en joignant les trajectoires de suivi et les masques de visibilité des pistes d'entrée selon leurs dimensions respectives. Si une seule entrée de piste est fournie, il transmet simplement ces données sans modification.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `tracks_1` | Le premier ensemble de données de suivi de mouvement à concaténer. | TRACKS | Oui |  |
| `tracks_2` | Un second ensemble optionnel de données de suivi de mouvement. S'il n'est pas fourni, `tracks_1` est transmis directement à la sortie. | TRACKS | Non |  |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `tracks` | Les données de suivi de mouvement concaténées, contenant le `track_path` et le `track_visibility` combinés provenant des entrées. Renvoie `tracks_1` inchangé lorsque `tracks_2` n'est pas connecté. | TRACKS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/fr.md)

---
**Source fingerprint (SHA-256):** `0507c42dce5d481fe5dc5aa1116c9df279f236419f548ea3eff5d824d0d22653`
