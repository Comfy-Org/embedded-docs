> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingSingleImageVideoEffectNode/fr.md)

Le nœud Effet Vidéo sur Image Unique Kling crée des vidéos avec différents effets spéciaux à partir d'une seule image de référence. Il applique divers effets visuels et scènes pour transformer des images statiques en contenu vidéo dynamique. Le nœud prend en charge différentes scènes d'effets, options de modèle et durées vidéo pour obtenir le résultat visuel souhaité.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | IMAGE | Oui | - | Image de référence. URL ou chaîne encodée en Base64 (sans le préfixe data:image). La taille du fichier ne peut pas dépasser 10 Mo, la résolution ne doit pas être inférieure à 300x300 px, le rapport hauteur/largeur doit être compris entre 1:2,5 et 2,5:1 |
| `effect_scene` | COMBO | Oui | `"dizzydizzy"`<br>`"bloombloom"`<br>`"neon"`<br>`"cartoon"`<br>`"sketch"`<br>`"oil"`<br>`"watercolor"`<br>`"3d"` | Le type de scène d'effet spécial à appliquer à la génération vidéo. Certains effets peuvent avoir une tarification différente. |
| `model_name` | COMBO | Oui | `"kling-v1-5"`<br>`"kling-v1-6"` | La version spécifique du modèle à utiliser pour générer l'effet vidéo. |
| `durée` | COMBO | Oui | `"5"`<br>`"10"` | La durée de la vidéo générée en secondes. |

**Remarque :** Le paramètre `effect_scene` affecte la tarification du nœud. Les effets `dizzydizzy` et `bloombloom` coûtent 0,49 $ USD par génération, tandis que tous les autres effets coûtent 0,28 $ USD par génération.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `video_id` | VIDEO | La vidéo générée avec les effets appliqués |
| `durée` | STRING | L'identifiant unique de la vidéo générée |
| `durée` | STRING | La durée de la vidéo générée |

---
**Source fingerprint (SHA-256):** `519db2f7185f200140c746bdebf89383523e0342bbfb61538adac063295d365d`
