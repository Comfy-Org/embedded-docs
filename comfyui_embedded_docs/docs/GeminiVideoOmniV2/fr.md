# Google Gemini Omni (vidéo)

Google Gemini Omni (Vidéo) génère une vidéo avec audio à partir d'une invite texte en utilisant les modèles Gemini Omni Flash de Google. Vous pouvez éventuellement joindre des images et/ou vidéos de référence pour guider le résultat ou pour modifier une séquence existante. Décrivez la durée souhaitée (3 à 10 secondes) directement dans l'invite.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `model` | Le modèle vidéo Gemini utilisé pour générer la vidéo. | DYNAMIC_COMBO | Oui | "Omni Flash 1.1"<br>"Omni Flash" |

### Entrées Omni Flash 1.1

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Décrivez la vidéo à générer, ou la modification à appliquer à une vidéo jointe. Spécifiez la durée directement dans l'invite, p. ex. « un clip de 6 secondes » ou, pour la tâche 'extend', « prolonger de 5 secondes » ; la durée générée peut être de 3 à 10 secondes et est de 10 par défaut. La sortie contient de l'audio. (défaut : "") | STRING | Oui | - |
| `resolution` | Résolution de sortie. (défaut : "720p") | COMBO | Oui | "360p"<br>"720p"<br>"1080p"<br>"4k" |
| `aspect_ratio` | Ratio d'aspect de sortie : 16:9 (paysage) ou 9:16 (portrait). Les tâches 'edit' et 'extend' conservent le ratio d'aspect de la vidéo d'entrée à la place. (défaut : "16:9") | COMBO | Oui | "16:9"<br>"9:16" |
| `task_type` | Ce qu'il faut faire de l'invite et des médias joints. Avec 'auto', le modèle décide. 'text_to_video' génère à partir de la seule invite et rejette les médias joints. 'image_to_video' anime une image, ou interpole entre une image de départ et une image de fin lorsque deux images sont jointes. 'reference_to_video' traite les médias joints comme des références de sujet. 'edit' réécrit exactement une vidéo jointe, et 'extend' lui ajoute de nouvelles séquences, de sorte que la sortie commence par la vidéo d'entrée. (défaut : "auto") | COMBO | Oui | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit"<br>"extend" |
| `seed` | La graine (seed) contrôle si le nœud doit s'exécuter à nouveau ; les résultats sont non déterministes quelle que soit la graine. (défaut : 42) | INT | Oui | 0 à 2147483647 |

### Entrées Omni Flash

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Décrivez la vidéo à générer, ou la modification à appliquer à une vidéo jointe. Spécifiez la durée directement dans l'invite, p. ex. « un clip de 6 secondes » ; la durée peut être de 3 à 10 secondes. La sortie est en 720p, 24 FPS, avec audio. (défaut : "") | STRING | Oui | - |
| `aspect_ratio` | Ratio d'aspect de sortie : 16:9 (paysage) ou 9:16 (portrait). La tâche 'edit' conserve le ratio d'aspect de la vidéo d'entrée à la place. (défaut : "16:9") | COMBO | Oui | "16:9"<br>"9:16" |
| `task_type` | Ce qu'il faut faire de l'invite et des médias joints. Avec 'auto', le modèle décide. 'text_to_video' génère à partir de la seule invite et rejette les médias joints. 'image_to_video' anime une image, ou interpole entre une image de départ et une image de fin lorsque deux images sont jointes. 'reference_to_video' traite les médias joints comme des références de sujet. 'edit' réécrit exactement une vidéo jointe. (défaut : "auto") | COMBO | Oui | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit" |
| `temperature` | Contrôle le caractère aléatoire. Une valeur plus basse donne des résultats plus ciblés/déterministes, une valeur plus élevée donne des résultats plus variés. (défaut : 1.0) | FLOAT | Oui | 0.0 à 2.0 (pas de 0.01) |
| `top_p` | Échantillonnage nucleus : échantillonner à partir du plus petit ensemble de jetons dont la probabilité cumulée atteint `top_p`. (défaut : 0.95) | FLOAT | Oui | 0.0 à 1.0 (pas de 0.01) |
| `seed` | La graine (seed) contrôle si le nœud doit s'exécuter à nouveau ; les résultats sont non déterministes quelle que soit la graine. (défaut : 42) | INT | Oui | 0 à 2147483647 |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------|----------|-------|
| `images` | Emplacement extensible : connectez jusqu'à 14 images (`image_1`...`image_14`). Image(s) de référence facultative(s) pour guider ou animer la vidéo. Avec la tâche 'image_to_video', la première est l'image de départ et une seconde facultative est l'image de fin. | IMAGE | Non | 0 à 14 images |
| `videos` | Emplacement extensible : connectez jusqu'à 3 vidéos (`video_1`...`video_3`). Vidéo(s) de référence facultative(s) pour guider ou modifier. Chacune d'une durée maximale de 10 secondes. | VIDEO | Non | 0 à 3 vidéos |

**Remarques :**
- Le paramètre `prompt` ne doit pas être vide ; le nœud lève une erreur si c'est le cas.
- La tâche `text_to_video` génère à partir de la seule invite — joindre des images ou des vidéos entraîne une erreur.
- La tâche `image_to_video` accepte uniquement des images (pas de vidéos) et nécessite exactement 1 ou 2 images : la première est l'image de départ et la seconde facultative est l'image de fin.
- La tâche `edit` (pour les deux modèles) et la tâche `extend` (Omni Flash 1.1 uniquement) nécessitent exactement une vidéo d'entrée et conservent le ratio d'aspect de cette vidéo d'entrée, en écrasant le paramètre `aspect_ratio`.
- Au maximum 14 images et 3 vidéos peuvent être jointes, et chaque vidéo jointe doit être d'une durée inférieure ou égale à 10 secondes.
- Omni Flash produit toujours une vidéo 720p à 24 FPS avec audio ; la sélection de la résolution n'est disponible qu'avec Omni Flash 1.1.
- Les contrôles `temperature` et `top_p` ne sont disponibles qu'avec le modèle Omni Flash ; Omni Flash 1.1 utilise des paramètres de génération fixes.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `video` (première sortie) | La vidéo générée avec audio. Pour Omni Flash : 720p, 24 FPS. Pour Omni Flash 1.1 : la résolution sélectionnée dans l'entrée `resolution`. | VIDEO |
| `text` (deuxième sortie) | Le contenu texte généré par le modèle avec la vidéo (peut être vide). | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmniV2/fr.md)

---
**Source fingerprint (SHA-256):** `7a0dda4bcd662c9df3c680297ec9de7886d35e618de8b3ce0cd95b9afd13a892`
