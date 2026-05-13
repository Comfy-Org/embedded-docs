> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/fr.md)

Voici la traduction en français de la documentation du nœud Kling Start-End Frame to Video :

Le nœud Kling Start-End Frame to Video crée une séquence vidéo qui effectue une transition entre vos images de début et de fin fournies. Il génère toutes les images intermédiaires pour produire une transformation fluide de la première à la dernière image. Ce nœud appelle l'API image-vers-vidéo mais ne prend en charge que les options d'entrée compatibles avec le champ de requête `image_tail`.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `start_frame` | IMAGE | Oui | - | Image de référence - URL ou chaîne encodée en Base64, ne peut pas dépasser 10 Mo, résolution minimale de 300x300 px, rapport hauteur/largeur compris entre 1:2,5 et 2,5:1. Le Base64 ne doit pas inclure le préfixe data:image. |
| `end_frame` | IMAGE | Oui | - | Image de référence - Contrôle de l'image de fin. URL ou chaîne encodée en Base64, ne peut pas dépasser 10 Mo, résolution minimale de 300x300 px. Le Base64 ne doit pas inclure le préfixe data:image. |
| `prompt` | STRING | Oui | - | Invite de texte positive |
| `negative_prompt` | STRING | Oui | - | Invite de texte négative |
| `cfg_scale` | FLOAT | Non | 0,0-1,0 | Contrôle la force du guidage par invite (par défaut : 0,5) |
| `aspect_ratio` | COMBO | Non | "16:9"<br>"9:16"<br>"1:1" | Le rapport hauteur/largeur de la vidéo générée (par défaut : "16:9") |
| `mode` | COMBO | Non | Plusieurs options disponibles | La configuration à utiliser pour la génération vidéo suivant le format : mode / durée / nom_du_modèle. (par défaut : la septième option des modes disponibles) |

**Contraintes d'image :**

- Les deux images `start_frame` et `end_frame` doivent être fournies et ne peuvent pas dépasser une taille de fichier de 10 Mo
- Résolution minimale : 300×300 pixels pour les deux images
- Le rapport hauteur/largeur de `start_frame` doit être compris entre 1:2,5 et 2,5:1
- Les images encodées en Base64 ne doivent pas inclure le préfixe "data:image"

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `video_id` | VIDEO | La séquence vidéo générée |
| `duration` | STRING | Identifiant unique de la vidéo générée |
| `duration` | STRING | Durée de la vidéo générée |

---
**Source fingerprint (SHA-256):** `1df5820b4f41ccd5afec8e2701888d90c940f164c433c7f81397b41e8fc333c6`
