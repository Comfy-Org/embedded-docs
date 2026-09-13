# KlingSingleImageVideoEffectNode

Le nœud Kling Single Image Video Effect crée des vidéos avec différents effets spéciaux à partir d'une seule image de référence. Il applique divers effets visuels et scènes pour transformer des images statiques en contenu vidéo dynamique. Le nœud prend en charge différentes scènes d'effets, options de modèle et durées vidéo pour obtenir le résultat visuel souhaité.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | Image de référence. URL ou chaîne encodée en Base64 (sans le préfixe data:image). La taille du fichier ne peut pas dépasser 10 Mo, la résolution ne doit pas être inférieure à 300 x 300 px, le rapport d'aspect doit être compris entre 1:2.5 et 2.5:1 | IMAGE | Oui | - |
| `effect_scene` | Type de scène d'effet spécial à appliquer à la génération de la vidéo. Certains effets peuvent avoir une tarification différente. | COMBO | Oui | `"dizzydizzy"`<br>`"bloombloom"`<br>`"neon"`<br>`"cartoon"`<br>`"sketch"`<br>`"oil"`<br>`"watercolor"`<br>`"3d"` |
| `model_name` | Version spécifique du modèle à utiliser pour générer l'effet vidéo. | COMBO | Oui | `"kling-v1-5"`<br>`"kling-v1-6"` |
| `duration` | Durée de la vidéo générée, en secondes. | COMBO | Oui | `"5"`<br>`"10"` |

**Remarque :** Le paramètre `effect_scene` affecte la tarification du nœud. Les effets `dizzydizzy` et `bloombloom` coûtent 0,49 USD par génération, tandis que tous les autres effets coûtent 0,28 USD par génération.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La vidéo générée avec les effets appliqués | VIDEO |
| `video_id` | L'identifiant unique de la vidéo générée | STRING |
| `duration` | La durée de la vidéo générée | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingSingleImageVideoEffectNode/fr.md)

---
**Source fingerprint (SHA-256):** `fb4a8b044daa99154a58d6926ff746bd2397b71ea32f1fafc851589f163ab51a`
