# VideoTrim

Ce nœud coupe une vidéo selon une fenêtre temporelle choisie en définissant un temps de début et une durée. Il offre également un mode strict qui déclenche une erreur lorsque la durée demandée ne peut pas être atteinte.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | La vidéo à rogner. | VIDEO | Oui | — |
| `trim` | Fenêtre de rognage utilisant des images de début/fin. La fenêtre est convertie en un temps de début (en secondes à partir du début de la vidéo) et une durée (en secondes). Lorsque le temps de début et la durée sont tous deux à 0, la vidéo est renvoyée sans aucun rognage. | VIDEO_EDIT | Oui | start_time: >= 0, default 0<br>duration: >= 0, default 0 |
| `strict_duration` | Si la valeur est True et que la durée spécifiée n'est pas réalisable, une erreur sera déclenchée. (par défaut : False) | BOOLEAN | Non | true<br>false |

Remarque : La durée de rognage doit être >= 0 ; les valeurs négatives déclenchent une erreur. La fenêtre de rognage demandée doit tenir entièrement dans la vidéo source. Si le rognage ne peut pas être appliqué, une erreur est déclenchée et rapporte la durée source, le temps de début et la durée cible.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo rognée. Lorsque la fenêtre de rognage est vide (temps de début et durée tous deux à 0), la vidéo d'origine est renvoyée inchangée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTrim/fr.md)

---
**Source fingerprint (SHA-256):** `ba8f8ccbae7e8aebda553810b81ccaa427d45523142bd00746c4e2f4e5b41a1b`
