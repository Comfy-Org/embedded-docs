# Creatify Aurora 2.0 Avatar

Creatify Aurora 2.0 Avatar transforme une photo accompagnée d'un extrait de parole ou de chant en une vidéo où la personne parle ou chante. La vidéo a la même durée que l'audio connecté et conserve cet audio inchangé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | Photo de la personne à animer. Au moins 256 pixels sur chaque côté et un rapport d'aspect compris entre 1:4 et 4:1 ; la vidéo conserve le rapport d'aspect de la photo. | IMAGE | Oui | - |
| `audio` | Parole ou chant qui pilote la bouche et la durée de la vidéo. Jusqu'à 60 secondes, ou 14 secondes en `"2k"` ; facturé par seconde entamée. | AUDIO | Oui | Jusqu'à 60 secondes |
| `resolution` | Résolution de la vidéo de sortie (par défaut : `"720p"`). | COMBO | Oui | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"2k"` |
| `text_prompt` | Scène, caméra, éclairage, expression ou mouvement pour la prise de vue. Une valeur vide conserve la photo telle quelle (par défaut : chaîne vide). | STRING | Oui | Texte quelconque |
| `seed` | `seed` contrôle si le nœud est réexécuté. Les résultats sont non déterministes quel que soit le seed (par défaut : 42). | INT | Oui | 0 à 2147483647 |

**Contraintes :** une photo de moins de 256 pixels par côté, ou dont le rapport d'aspect sort de la plage 1:4 à 4:1, déclenche une erreur. Un audio plus long que la limite de la résolution choisie est rejeté : 60 secondes normalement et 14 secondes en `"2k"`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo parlante ou chantante, avec l'audio connecté. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreatifyAurora2AvatarNode/fr.md)

---
**Source fingerprint (SHA-256):** `29c83246ebed4bc7a9f3daf3612cd6f34bf2d5a2f1fde7612614a2da6a5010be`
