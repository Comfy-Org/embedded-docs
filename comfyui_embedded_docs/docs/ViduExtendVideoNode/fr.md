> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduExtendVideoNode/fr.md)

Voici la traduction en français de la documentation du nœud ViduExtendVideoNode :

Le nœud ViduExtendVideoNode génère des images supplémentaires pour prolonger la durée d'une vidéo existante. Il utilise un modèle d'IA spécifié pour créer une continuation fluide basée sur la vidéo source et une invite textuelle optionnelle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | COMBO | Oui | `"viduq2-pro"`<br>`"viduq2-turbo"` | Le modèle d'IA à utiliser pour l'extension vidéo. La sélection d'un modèle révèle ses paramètres spécifiques de durée et de résolution. |
| `model.duration` | INT | Oui | 1 à 7 | La durée de la vidéo étendue en secondes (par défaut : 4). Ce paramètre apparaît après la sélection d'un modèle. |
| `model.resolution` | COMBO | Oui | `"720p"`<br>`"1080p"` | La résolution de la vidéo de sortie. Ce paramètre apparaît après la sélection d'un modèle. |
| `video` | VIDEO | Oui | - | La vidéo source à étendre. |
| `prompt` | STRING | Non | - | Une invite textuelle optionnelle pour guider le contenu de la vidéo étendue (2000 caractères maximum, par défaut : vide). |
| `seed` | INT | Non | 0 à 2147483647 | Une valeur de graine pour contrôler l'aléatoire de la génération (par défaut : 1). |
| `end_frame` | IMAGE | Non | - | Une image optionnelle à utiliser comme image de fin cible pour l'extension. Si fournie, son rapport hauteur/largeur doit être compris entre 1:4 et 4:1, et ses dimensions doivent être d'au moins 128x128 pixels. |

**Remarque :** La `video` source doit avoir une durée comprise entre 4 et 55 secondes.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | Le fichier vidéo nouvellement généré contenant les images étendues. |

---
**Source fingerprint (SHA-256):** `44b942413c8aed2fc0049386a31c441f6f870ba4220b0c439dfc436079229446`
