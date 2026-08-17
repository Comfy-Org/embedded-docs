# Découpage Vidéo

Le nœud Video Slice vous permet d'extraire un segment spécifique d'une vidéo. Vous pouvez définir un temps de début et une durée pour découper la vidéo, ou simplement ignorer les premières images. Si la durée demandée est plus longue que la vidéo restante, le nœud peut soit retourner ce qui est disponible, soit lever une erreur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `video` | La vidéo d'entrée à découper. | VIDEO | Oui | - |
| `start_time` | Temps de début en secondes (défaut : 0.0). | FLOAT | Non | -1e5 to 1e5 |
| `duration` | Durée en secondes, ou 0 pour une durée illimitée (défaut : 0.0). | FLOAT | Non | 0.0 and above |
| `strict_duration` | Si True, une erreur est levée lorsque la durée spécifiée n'est pas possible (défaut : False). | BOOLEAN | Non | - |

Remarque : Lorsque `duration` est 0, le nœud découpe depuis `start_time` jusqu'à la fin de la vidéo. Si le segment demandé ne peut pas être créé — par exemple, parce que `start_time` est au-delà de la fin de la vidéo — le nœud lève une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | Le segment vidéo découpé. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/fr.md)

---
**Source fingerprint (SHA-256):** `439b76528742c1fbe230eee9502e945847ae99a58a9bd81a7a7dc3b20e15d450`
