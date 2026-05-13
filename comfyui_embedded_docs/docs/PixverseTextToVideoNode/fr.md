> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/fr.md)

Voici la traduction en français de la documentation technique du nœud ComfyUI :

Génère des vidéos à partir d'une invite textuelle et de divers paramètres de génération. Ce nœud crée du contenu vidéo via l'API PixVerse, permettant de contrôler le rapport hauteur/largeur, la qualité, la durée, le style de mouvement, et plus encore.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `prompt` | STRING | Oui | - | Invite pour la génération vidéo (par défaut : "") |
| `rapport d'aspect` | COMBO | Oui | Options de PixverseAspectRatio | Rapport hauteur/largeur de la vidéo générée |
| `qualité` | COMBO | Oui | Options de PixverseQuality | Réglage de qualité vidéo (par défaut : PixverseQuality.res_540p) |
| `durée (secondes)` | COMBO | Oui | Options de PixverseDuration | Durée de la vidéo générée en secondes |
| `mode de mouvement` | COMBO | Oui | Options de PixverseMotionMode | Style de mouvement pour la génération vidéo |
| `graine` | INT | Oui | 0 à 2147483647 | Graine pour la génération vidéo (par défaut : 0) |
| `prompt négatif` | STRING | Non | - | Description textuelle facultative des éléments indésirables sur une image (par défaut : "") |
| `modèle PixVerse` | CUSTOM | Non | - | Modèle facultatif pour influencer le style de génération, créé par le nœud PixVerse Template |

**Remarque :** Lors de l'utilisation de la qualité 1080p, le mode de mouvement est automatiquement défini sur normal et la durée est limitée à 5 secondes. Pour les durées autres que 5 secondes, le mode de mouvement est également automatiquement défini sur normal.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | Le fichier vidéo généré |

---
**Source fingerprint (SHA-256):** `ab9264668f48533cb139abfb322e9a6e425a2ad7280da103a7fe0a7704158762`
