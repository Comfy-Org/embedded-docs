# Extension de vidéo Vidu

Le nœud Vidu Video Extension génère des images supplémentaires pour prolonger la durée d'une vidéo existante. Il utilise un modèle d'IA spécifié pour créer une suite basée sur la vidéo source et un prompt textuel facultatif.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Modèle à utiliser pour l'extension vidéo. La sélection d'un modèle révèle ses paramètres spécifiques de durée et de résolution. | DYNAMIC_COMBO | Oui | `"viduq2-pro"`<br>`"viduq2-turbo"` |
| `vidéo` | Vidéo source à étendre. | VIDEO | Oui | - |
| `invite` | Prompt textuel facultatif pour la vidéo étendue (max 2000 caractères ; par défaut : vide). | STRING | Oui | - |
| `graine` | Valeur de graine pour contrôler le caractère aléatoire de la génération (par défaut : 1). | INT | Oui | 0 à 2147483647 |
| `image_finale` | Image facultative à utiliser comme image de fin cible pour l'extension. | IMAGE | Non | - |

### Entrées viduq2-pro et viduq2-turbo

Ces paramètres sont partagés par les deux modèles.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `duration` | Durée de la vidéo étendue en secondes (par défaut : 4). Ce paramètre apparaît après la sélection d'un modèle. | INT | Oui | 1 à 7 |
| `resolution` | Résolution de la vidéo de sortie. Ce paramètre apparaît après la sélection d'un modèle. | COMBO | Oui | `"720p"`<br>`"1080p"` |

**Remarque :** La `video` source doit avoir une durée comprise entre 4 et 55 secondes. Si `end_frame` est fourni, son rapport d'aspect doit être compris entre 1:4 et 4:1, et sa largeur et sa hauteur doivent chacune être d'au moins 128 pixels.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Le fichier vidéo nouvellement généré contenant la séquence prolongée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduExtendVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `bfa79dd1aee8a3e56d95fe7a899454b5c5f93679e098f59fc3bf58d93d290819`
