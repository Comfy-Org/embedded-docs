Voici la traduction en français de la documentation technique du nœud ComfyUI :

Génère des vidéos à partir d'une invite textuelle et de divers paramètres de génération. Ce nœud crée du contenu vidéo via l'API PixVerse, permettant de contrôler le rapport hauteur/largeur, la qualité, la durée, le style de mouvement, et plus encore.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `prompt` | Invite pour la génération vidéo (par défaut : "") | STRING | Oui | - |
| `rapport d'aspect` | Rapport hauteur/largeur de la vidéo générée | COMBO | Oui | Options de PixverseAspectRatio |
| `qualité` | Réglage de qualité vidéo (par défaut : PixverseQuality.res_540p) | COMBO | Oui | Options de PixverseQuality |
| `durée (secondes)` | Durée de la vidéo générée en secondes | COMBO | Oui | Options de PixverseDuration |
| `mode de mouvement` | Style de mouvement pour la génération vidéo | COMBO | Oui | Options de PixverseMotionMode |
| `graine` | Graine pour la génération vidéo (par défaut : 0) | INT | Oui | 0 à 2147483647 |
| `prompt négatif` | Description textuelle facultative des éléments indésirables sur une image (par défaut : "") | STRING | Non | - |
| `modèle PixVerse` | Modèle facultatif pour influencer le style de génération, créé par le nœud PixVerse Template | CUSTOM | Non | - |

**Remarque :** Lors de l'utilisation de la qualité 1080p, le mode de mouvement est automatiquement défini sur normal et la durée est limitée à 5 secondes. Pour les durées autres que 5 secondes, le mode de mouvement est également automatiquement défini sur normal.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `ab9264668f48533cb139abfb322e9a6e425a2ad7280da103a7fe0a7704158762`
