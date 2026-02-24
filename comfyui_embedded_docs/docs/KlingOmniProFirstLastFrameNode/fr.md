> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProFirstLastFrameNode/fr.md)

Ce nœud utilise le modèle Kling AI pour générer une vidéo. Il nécessite une image de départ et une description textuelle. Vous pouvez optionnellement fournir une image de fin ou jusqu'à six images de référence pour guider le contenu et le style de la vidéo. Le nœud traite ces entrées pour créer une vidéo d'une durée et d'une résolution spécifiées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Oui | `"kling-video-o1"` | Le modèle Kling AI spécifique à utiliser pour la génération de vidéo. |
| `prompt` | STRING | Oui | - | Une description textuelle du contenu de la vidéo. Elle peut inclure à la fois des descriptions positives et négatives. |
| `duration` | INT | Oui | 3 à 10 | La durée souhaitée de la vidéo générée en secondes (par défaut : 5). |
| `first_frame` | IMAGE | Oui | - | L'image de départ pour la séquence vidéo. |
| `end_frame` | IMAGE | Non | - | Une image de fin optionnelle pour la vidéo. Elle ne peut pas être utilisée simultanément avec `reference_images`. |
| `reference_images` | IMAGE | Non | - | Jusqu'à 6 images de référence supplémentaires. |
| `resolution` | COMBO | Non | `"1080p"`<br>`"720p"` | La résolution de sortie pour la vidéo générée (par défaut : "1080p"). |

**Contraintes importantes :**

* L'entrée `end_frame` ne peut pas être utilisée en même temps que l'entrée `reference_images`.
* Si vous ne fournissez pas d'`end_frame` ou d'`reference_images`, la `duration` ne peut être définie qu'à 5 ou 10 secondes.
* Toutes les images d'entrée (`first_frame`, `end_frame` et toutes les `reference_images`) doivent avoir une dimension minimale de 300 pixels en largeur et en hauteur.
* Le rapport d'aspect de toutes les images d'entrée doit être compris entre 1:2,5 et 2,5:1.
* Un maximum de 6 images peut être fourni via l'entrée `reference_images`.
* Le texte du `prompt` doit comporter entre 1 et 2500 caractères.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output` | VIDEO | Le fichier vidéo généré. |
