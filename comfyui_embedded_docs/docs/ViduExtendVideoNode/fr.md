Voici la traduction en français de la documentation du nœud ViduExtendVideoNode :

Le nœud ViduExtendVideoNode génère des images supplémentaires pour prolonger la durée d'une vidéo existante. Il utilise un modèle d'IA spécifié pour créer une continuation fluide basée sur la vidéo source et une invite textuelle optionnelle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d'IA à utiliser pour l'extension vidéo. La sélection d'un modèle révèle ses paramètres spécifiques de durée et de résolution. | COMBO | Oui | `"viduq2-pro"`<br>`"viduq2-turbo"` |
| `model.duration` | La durée de la vidéo étendue en secondes (par défaut : 4). Ce paramètre apparaît après la sélection d'un modèle. | INT | Oui | 1 à 7 |
| `model.resolution` | La résolution de la vidéo de sortie. Ce paramètre apparaît après la sélection d'un modèle. | COMBO | Oui | `"720p"`<br>`"1080p"` |
| `vidéo` | La vidéo source à étendre. | VIDEO | Oui | - |
| `invite` | Une invite textuelle optionnelle pour guider le contenu de la vidéo étendue (2000 caractères maximum, par défaut : vide). | STRING | Non | - |
| `graine` | Une valeur de graine pour contrôler l'aléatoire de la génération (par défaut : 1). | INT | Non | 0 à 2147483647 |
| `image_finale` | Une image optionnelle à utiliser comme image de fin cible pour l'extension. Si fournie, son rapport hauteur/largeur doit être compris entre 1:4 et 4:1, et ses dimensions doivent être d'au moins 128x128 pixels. | IMAGE | Non | - |

**Remarque :** La `video` source doit avoir une durée comprise entre 4 et 55 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo nouvellement généré contenant les images étendues. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduExtendVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `44b942413c8aed2fc0049386a31c441f6f870ba4220b0c439dfc436079229446`
