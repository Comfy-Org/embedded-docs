# Kling Début-Fin Image vers Vidéo

Ce nœud crée une séquence vidéo qui effectue une transition entre vos images de début et de fin fournies. Il génère toutes les images intermédiaires pour produire une transformation fluide de la première à la dernière image. Ce nœud appelle l'API image-to-video mais ne prend en charge que les options d'entrée compatibles avec le champ de requête `image_tail`.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `start_frame` | Image de référence - URL ou chaîne encodée en Base64, ne peut pas dépasser 10 Mo, résolution non inférieure à 300*300 px, rapport d'aspect entre 1:2.5 ~ 2.5:1. Base64 ne doit pas inclure le préfixe data:image. | IMAGE | Oui | - |
| `end_frame` | Image de référence - Contrôle de l'image de fin. URL ou chaîne encodée en Base64, ne peut pas dépasser 10 Mo, résolution non inférieure à 300*300 px. Base64 ne doit pas inclure le préfixe data:image. | IMAGE | Oui | - |
| `prompt` | Prompt textuel positif. Ne doit pas être vide et ne peut pas dépasser 500 caractères. | STRING | Oui | - |
| `negative_prompt` | Prompt textuel négatif. Ne peut pas dépasser 500 caractères. S'il est laissé vide, il est omis de la requête. | STRING | Oui | - |
| `cfg_scale` | Contrôle la force du guidage du prompt (par défaut : 0.5). | FLOAT | Oui | 0.0-1.0 |
| `aspect_ratio` | Le rapport d'aspect de la vidéo générée (par défaut : "16:9"). | COMBO | Oui | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | La configuration à utiliser pour la génération de la vidéo selon le format : mode / durée / nom_du_modèle. (par défaut : "pro mode / 5s duration / kling-v2-5-turbo") | COMBO | Oui | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

**Contraintes d'image :**

- `start_frame` et `end_frame` sont tous deux requis et ne peuvent pas dépasser 10 Mo en taille de fichier.
- Résolution minimale : 300×300 pixels pour les deux images.
- Le rapport d'aspect de `start_frame` doit être compris entre 1:2.5 et 2.5:1.
- Les images encodées en Base64 ne doivent pas inclure le préfixe "data:image".

**Contraintes de prompt :**

- `prompt` ne doit pas être vide et ne peut pas dépasser 500 caractères.
- `negative_prompt` ne peut pas dépasser 500 caractères ; lorsqu'il est vide, il n'est pas envoyé avec la requête.

**Remarques sur le mode :**

- Les deux options de mode utilisent le mode pro avec le modèle kling-v2-5-turbo et ne diffèrent que par la durée (5 secondes ou 10 secondes).
- Tarification par génération, comme indiqué dans le badge de prix du nœud : le mode 5s coûte 0,35 USD et le mode 10s coûte 0,70 USD.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La séquence vidéo générée. | VIDEO |
| `video_id` | Identifiant unique de la vidéo générée. | STRING |
| `duration` | Durée de la vidéo générée. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `a27977226360a425614255f8330ce7fd8ba94b8c3020eb8fdddc01eb74f035c1`
