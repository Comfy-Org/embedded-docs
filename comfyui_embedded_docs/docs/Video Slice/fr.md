# Découpage Vidéo

Le nœud Video Slice vous permet d'extraire un segment spécifique d'une vidéo. Vous pouvez définir un temps de début et une durée pour découper la vidéo, ou simplement ignorer les premières frames. Si la durée demandée est plus longue que la vidéo restante, le nœud peut soit retourner ce qui est disponible, soit lever une erreur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vidéo` | La vidéo d'entrée à découper. | VIDEO | Oui | - |
| `heure_de_début` | Temps de début en secondes (défaut : 0.0). | FLOAT | Oui | -1e5 à 1e5 |
| `durée` | Durée en secondes, ou 0 pour une durée illimitée (défaut : 0.0). | FLOAT | Oui | 0.0 et plus |
| `durée_stricte` | Si True, une erreur sera levée lorsque la durée spécifiée n'est pas possible (défaut : False). | BOOLEAN | Oui | - |

**Remarque :** Si la vidéo ne peut pas être découpée pour `start_time` et `duration` donnés, le nœud lève une erreur. Lorsque `strict_duration` est False, le nœud retourne la portion disponible de la vidéo si la durée demandée dépasse la longueur restante ; lorsque True, il lève une erreur à la place.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | Le segment vidéo découpé. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/fr.md)

---
**Source fingerprint (SHA-256):** `439b76528742c1fbe230eee9502e945847ae99a58a9bd81a7a7dc3b20e15d450`
