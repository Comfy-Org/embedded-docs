# LumaRay32ImageToVideoNode

Générer une vidéo à partir d'une image de début et/ou de fin en utilisant le modèle Ray 3.2 de Luma. Les générations basées sur une image d'ancrage ont toujours une durée de 5 secondes.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Texte descriptif pour la génération vidéo. | STRING | Oui | 1 à 6000 caractères |
| `resolution` | La résolution de sortie de la vidéo générée (par défaut : "720p"). | COMBO | Oui | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `loop` | Permet de boucler la vidéo de manière fluide. Non disponible lorsqu'une `end_frame` est définie. | BOOLEAN | Oui | True<br>False |
| `seed` | Valeur de graine pour une génération reproductible. | INT | Oui | 0 à 2147483647 |
| `start_frame` | Première image de la vidéo générée. | IMAGE | Non | - |
| `end_frame` | Dernière image de la vidéo générée. | IMAGE | Non | - |

**Remarque :** Au moins l'un des paramètres `start_frame` ou `end_frame` doit être fourni. Si les deux sont fournis, la vidéo générée effectuera une transition de l'image de début à l'image de fin. L'option `loop` ne peut pas être activée lorsqu'une `end_frame` est définie.

## Sorties

| Nom de la sortie | Description | Type de données |
|------------------|-------------|-----------------|
| `video` | La sortie vidéo générée. | VIDEO |
| `generation_id` | L'identifiant unique de la demande de génération. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `ff479c196f10153ffa09af6acfb4e286d1934aa28a5e9b413613097a2cfb5f2a`
