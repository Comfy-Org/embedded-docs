> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JoinAudioChannels/fr.md)

Le nœud **Join Audio Channels** combine deux entrées audio mono distinctes en une seule sortie audio stéréo. Il prend un canal gauche et un canal droit, s'assure qu'ils ont des fréquences d'échantillonnage et des longueurs compatibles, puis les fusionne en une forme d'onde audio à deux canaux.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `audio_left` | AUDIO | Oui | | Les données audio mono à utiliser comme canal gauche dans l'audio stéréo résultant. |
| `audio_right` | AUDIO | Oui | | Les données audio mono à utiliser comme canal droit dans l'audio stéréo résultant. |

**Remarque :** Les deux flux audio en entrée doivent être mono (monocanal). S'ils ont des fréquences d'échantillonnage différentes, le canal avec la fréquence la plus basse sera automatiquement rééchantillonné pour correspondre à la fréquence la plus élevée. Si les flux audio ont des longueurs différentes, ils seront tronqués à la longueur du plus court.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `audio` | AUDIO | L'audio stéréo résultant, contenant les canaux gauche et droit fusionnés. |

---
**Source fingerprint (SHA-256):** `6dced8c2288fb8f214e04b621ed3ab934231983d7987ff08aa43da6814331be0`
