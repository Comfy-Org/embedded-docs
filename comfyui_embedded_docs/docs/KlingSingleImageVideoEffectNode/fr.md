> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingSingleImageVideoEffectNode/fr.md)

Le nœud Kling Single Image Video Effect crée des vidéos avec différents effets spéciaux basés sur une seule image de référence. Il applique divers effets visuels et scènes pour transformer des images statiques en contenu vidéo dynamique. Le nœud prend en charge différentes scènes d'effets, options de modèle et durées vidéo pour obtenir le résultat visuel souhaité.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Oui | - | Image de référence. URL ou chaîne encodée en Base64 (sans le préfixe data:image). La taille du fichier ne peut pas dépasser 10 Mo, la résolution ne doit pas être inférieure à 300*300 px, le rapport d'aspect doit être compris entre 1:2,5 et 2,5:1 |
| `effect_scene` | COMBO | Oui | Options de KlingSingleImageEffectsScene | Le type de scène d'effet spéciaux à appliquer à la génération de la vidéo |
| `model_name` | COMBO | Oui | Options de KlingSingleImageEffectModelName | Le modèle spécifique à utiliser pour générer l'effet vidéo |
| `durée` | COMBO | Oui | Options de KlingVideoGenDuration | La durée de la vidéo générée |

**Remarque :** Les options spécifiques pour `effect_scene`, `model_name` et `duration` sont déterminées par les valeurs disponibles dans leurs classes d'énumération respectives (KlingSingleImageEffectsScene, KlingSingleImageEffectModelName et KlingVideoGenDuration).

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `video_id` | VIDEO | La vidéo générée avec les effets appliqués |
| `durée` | STRING | L'identifiant unique de la vidéo générée |
| `durée` | STRING | La durée de la vidéo générée |