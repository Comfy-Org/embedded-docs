# Découper la vidéo (avancé)

Ce nœud découpe une vidéo sur une fenêtre temporelle choisie en définissant un temps de début et une durée. Il propose également un mode strict qui lève une erreur lorsque la durée demandée ne peut pas être atteinte.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | La vidéo à découper. | VIDEO | Oui | — |
| `trim` | Fenêtre de découpe utilisant des images de début/fin. La fenêtre est convertie en un temps de début (en secondes depuis le début de la vidéo) et une durée (en secondes). Lorsque le temps de début et la durée sont tous les deux à 0, la vidéo est renvoyée sans aucune découpe. | VIDEO_EDIT | Oui | start_time : >= 0, par défaut 0<br>duration : >= 0, par défaut 0 |
| `strict_duration` | Si True, lorsqu'il est impossible d'atteindre la durée spécifiée, une erreur est levée. (par défaut : False) | BOOLEAN | Non | true<br>false |

Remarque : La durée de découpe doit être >= 0 ; les valeurs négatives génèrent une erreur. La fenêtre de découpe demandée doit tenir dans la vidéo source. Si la découpe ne peut pas être appliquée, une erreur est levée indiquant la durée source, le temps de début et la durée cible.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo découpée. Lorsque la fenêtre de découpe est vide (temps de début et durée tous les deux à 0), la vidéo d'origine est renvoyée sans modification. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTrim/fr.md)

---
**Source fingerprint (SHA-256):** `ba8f8ccbae7e8aebda553810b81ccaa427d45523142bd00746c4e2f4e5b41a1b`
