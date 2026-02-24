> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProEditVideoNode/fr.md)

Le nœud Kling Omni Edit Video (Pro) utilise un modèle d'IA pour modifier une vidéo existante en fonction d'une description textuelle. Vous fournissez une vidéo source et une instruction, et le nœud génère une nouvelle vidéo de même durée avec les modifications demandées. Il peut optionnellement utiliser des images de référence pour guider le style et conserver l'audio original de la vidéo source.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Oui | `"kling-video-o1"` | Le modèle d'IA à utiliser pour l'édition vidéo. |
| `prompt` | STRING | Oui | | Une instruction textuelle décrivant le contenu de la vidéo. Elle peut inclure à la fois des descriptions positives et négatives. |
| `video` | VIDEO | Oui | | La vidéo à éditer. La durée de la vidéo de sortie sera identique. |
| `keep_original_sound` | BOOLEAN | Oui | | Détermine si l'audio original de la vidéo d'entrée est conservé dans la sortie (par défaut : True). |
| `reference_images` | IMAGE | Non | | Jusqu'à 4 images de référence supplémentaires. |
| `resolution` | COMBO | Non | `"1080p"`<br>`"720p"` | La résolution pour la vidéo de sortie (par défaut : "1080p"). |

**Contraintes et limitations :**

* Le `prompt` doit compter entre 1 et 2500 caractères.
* La `video` d'entrée doit avoir une durée comprise entre 3,0 et 10,05 secondes.
* Les dimensions de la `video` d'entrée doivent être comprises entre 720x720 et 2160x2160 pixels.
* Un maximum de 4 `reference_images` peut être fourni lorsqu'une vidéo est utilisée.
* Chaque `reference_image` doit mesurer au moins 300x300 pixels.
* Chaque `reference_image` doit avoir un rapport d'aspect compris entre 1:2,5 et 2,5:1.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `video` | VIDEO | La vidéo éditée générée par le modèle d'IA. |
