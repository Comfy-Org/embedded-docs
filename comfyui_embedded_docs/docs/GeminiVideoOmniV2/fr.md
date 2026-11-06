# Google Gemini Omni (vidéo)

Google Gemini Omni (Video) génère une vidéo avec audio à partir d'un prompt texte en utilisant les modèles Google Gemini Omni Flash. Vous pouvez éventuellement joindre des images et/ou vidéos de référence pour guider le résultat ou modifier une séquence existante. Décrivez la durée souhaitée directement dans le prompt : 3 à 10 secondes pour Omni Flash et Omni Flash 1.1, 3 à 15 secondes pour Omni Flash 1.2.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `model` | Le modèle vidéo Gemini utilisé pour générer la vidéo. | DYNAMIC_COMBO | Oui | "Omni Flash 1.2"<br>"Omni Flash 1.1"<br>"Omni Flash" |

### Entrées Omni Flash 1.2

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `prompt` | Décrivez la vidéo à générer, ou la modification à appliquer à une vidéo jointe. Spécifiez la durée directement dans le prompt, par ex. "a 6-second clip" ou, pour la tâche 'extend', "extend by 5 seconds" ; la durée générée peut être de 3 à 15 secondes, et 'extend' ajoute au plus 10 secondes. La sortie comporte de l'audio. (par défaut : "") | STRING | Oui | - |
| `resolution` | Résolution de sortie. (par défaut : "720p") | COMBO | Oui | "360p"<br>"720p"<br>"1080p"<br>"4k" |
| `aspect_ratio` | Rapport d'aspect de sortie : 16:9 (paysage) ou 9:16 (portrait). Les tâches 'edit' et 'extend' conservent plutôt le rapport d'aspect de la vidéo d'entrée. (par défaut : "16:9") | COMBO | Oui | "16:9"<br>"9:16" |
| `task_type` | Ce qu'il faut faire avec le prompt et les médias joints. Avec 'auto', le modèle décide. 'text_to_video' génère à partir du prompt seul et rejette les médias joints. 'image_to_video' anime une image, ou interpole entre une image de départ et une image de fin lorsque deux sont jointes. 'reference_to_video' traite les médias joints comme des références de sujet. 'edit' réécrit exactement une vidéo jointe, et 'extend' ajoute de nouvelles séquences, de sorte que la sortie commence par la vidéo d'entrée. (par défaut : "auto") | COMBO | Oui | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit"<br>"extend" |
| `seed` | La `seed` contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la seed. (par défaut : 42) | INT | Oui | 0 à 2147483647 |

### Entrées Omni Flash 1.1

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `prompt` | Décrivez la vidéo à générer, ou la modification à appliquer à une vidéo jointe. Spécifiez la durée directement dans le prompt, par ex. "a 6-second clip" ou, pour la tâche 'extend', "extend by 5 seconds" ; la durée générée peut être de 3 à 10 secondes et vaut 10 par défaut. La sortie comporte de l'audio. (par défaut : "") | STRING | Oui | - |
| `resolution` | Résolution de sortie. (par défaut : "720p") | COMBO | Oui | "360p"<br>"720p"<br>"1080p"<br>"4k" |
| `aspect_ratio` | Rapport d'aspect de sortie : 16:9 (paysage) ou 9:16 (portrait). Les tâches 'edit' et 'extend' conservent plutôt le rapport d'aspect de la vidéo d'entrée. (par défaut : "16:9") | COMBO | Oui | "16:9"<br>"9:16" |
| `task_type` | Ce qu'il faut faire avec le prompt et les médias joints. Avec 'auto', le modèle décide. 'text_to_video' génère à partir du prompt seul et rejette les médias joints. 'image_to_video' anime une image, ou interpole entre une image de départ et une image de fin lorsque deux sont jointes. 'reference_to_video' traite les médias joints comme des références de sujet. 'edit' réécrit exactement une vidéo jointe, et 'extend' ajoute de nouvelles séquences, de sorte que la sortie commence par la vidéo d'entrée. (par défaut : "auto") | COMBO | Oui | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit"<br>"extend" |
| `seed` | La `seed` contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la seed. (par défaut : 42) | INT | Oui | 0 à 2147483647 |

### Entrées Omni Flash

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `prompt` | Décrivez la vidéo à générer, ou la modification à appliquer à une vidéo jointe. Spécifiez la durée directement dans le prompt, par ex. "a 6-second clip" ; la durée peut être de 3 à 10 secondes. La sortie est en 720p, 24 FPS, avec audio. (par défaut : "") | STRING | Oui | - |
| `aspect_ratio` | Rapport d'aspect de sortie : 16:9 (paysage) ou 9:16 (portrait). La tâche 'edit' conserve plutôt le rapport d'aspect de la vidéo d'entrée. (par défaut : "16:9") | COMBO | Oui | "16:9"<br>"9:16" |
| `task_type` | Ce qu'il faut faire avec le prompt et les médias joints. Avec 'auto', le modèle décide. 'text_to_video' génère à partir du prompt seul et rejette les médias joints. 'image_to_video' anime une image, ou interpole entre une image de départ et une image de fin lorsque deux sont jointes. 'reference_to_video' traite les médias joints comme des références de sujet. 'edit' réécrit exactement une vidéo jointe. (par défaut : "auto") | COMBO | Oui | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit" |
| `temperature` | Contrôle le caractère aléatoire. Une valeur plus basse est plus ciblée/déterministe, une valeur plus élevée est plus variée. (par défaut : 1.0) | FLOAT | Oui | 0.0 à 2.0 (pas : 0.01) |
| `top_p` | Échantillonnage nucleus : échantillonne dans le plus petit ensemble de tokens dont la probabilité cumulée atteint top_p. (par défaut : 0.95) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `seed` | La `seed` contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la seed. (par défaut : 42) | INT | Oui | 0 à 2147483647 |

### Entrées de référence

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `images` | Emplacement extensible : connectez jusqu'à 14 images (`image_1`...`image_14`). Image(s) de référence facultative(s) pour guider ou animer la vidéo. Avec la tâche 'image_to_video', la première correspond à l'image de départ et une seconde facultative à l'image de fin. | IMAGE | Non | 0 à 14 images |
| `videos` | Emplacement extensible : connectez jusqu'à 3 vidéos (`video_1`...`video_3`). Vidéo(s) de référence facultative(s) pour guider ou modifier. Chacune d'une durée maximale de 10 secondes. | VIDEO | Non | 0 à 3 vidéos |

**Notes :**
- Le `prompt` ne doit pas être vide ; le nœud renvoie une erreur s'il l'est.
- La tâche `text_to_video` génère à partir du prompt seul — joindre des images ou des vidéos renvoie une erreur.
- La tâche `image_to_video` accepte uniquement des images (pas de vidéos) et nécessite exactement 1 ou 2 images : la première est l'image de départ et la seconde facultative est l'image de fin.
- La tâche `edit` (tous les modèles) et la tâche `extend` (Omni Flash 1.1 et 1.2 uniquement) nécessitent exactement une vidéo d'entrée et conservent le rapport d'aspect de cette vidéo d'entrée, ce qui remplace `aspect_ratio`.
- Il est possible de joindre au maximum 14 images et 3 vidéos. Chaque vidéo jointe doit durer 10 secondes ou moins, 15 secondes ou moins avec Omni Flash 1.2, et 25 secondes ou moins pour la tâche `extend`, dont le résultat peut durer au maximum 30 secondes.
- Omni Flash produit toujours une vidéo 720p à 24 FPS avec audio ; la sélection de la résolution n'est disponible qu'avec Omni Flash 1.1 et 1.2.
- Les contrôles `temperature` et `top_p` ne sont disponibles qu'avec le modèle Omni Flash ; Omni Flash 1.1 et 1.2 utilisent des paramètres de génération fixes.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` (première sortie) | La vidéo générée avec audio. Pour Omni Flash : 720p, 24 FPS. Pour Omni Flash 1.1 et 1.2 : la résolution sélectionnée dans l'entrée `resolution`. | VIDEO |
| `text` (deuxième sortie) | Le contenu texte généré par le modèle avec la vidéo (peut être vide). | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmniV2/fr.md)

---
**Source fingerprint (SHA-256):** `1fc6017d4d6fbce8f04b2f0ded496553074b8498e3b7342179550fc768698897`
