# ConcatenateVideo

Concatène plusieurs segments vidéo en une seule vidéo, en préservant l'ordre dans lequel ils sont connectés. Les entrées encodées compatibles sont combinées sans être décodées, et une piste audio distincte facultative peut être fournie pour remplacer l'audio d'origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `videos` | Segments vidéo à concaténer dans l'ordre d'entrée. Connectez 1 à 100 vidéos ; chaque vidéo apparaît comme un emplacement d'entrée distinct étiqueté `video_1`, `video_2`, etc. | VIDEO | Oui | 1 à 100 segments |
| `codec` | Codec utilisé pour encoder les tenseurs vidéo. Auto utilise H.264 ; les vidéos déjà encodées compatibles restent inchangées. Par défaut : « auto » | COMBO | Oui | `"auto"`<br>Les autres options sont définies par les types de codecs vidéo disponibles. |
| `complete_audio` | Bande sonore complète facultative pour la vidéo concaténée. Remplace l'audio transporté par les vidéos d'entrée. | AUDIO | Non | N/A |

**Remarque :** L'entrée `videos` accepte entre 1 et 100 segments vidéo. Si `complete_audio` est fourni, il remplace l'audio de toutes les vidéos d'entrée. Lorsque `codec` est défini sur « auto », les entrées encodées compatibles sont concaténées sans décodage.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo concaténée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConcatenateVideo/fr.md)

---
**Source fingerprint (SHA-256):** `f591aecb83754127e1c86ed0488548f9e7d99f3559c95a1c86c55fa5d430713d`
