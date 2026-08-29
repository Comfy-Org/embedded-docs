# Google Gemini Omni (Vidéo)

Générez une vidéo avec du son à partir d'une invite texte à l'aide du modèle Gemini Omni Flash de Google. Vous pouvez éventuellement fournir des images et/ou vidéos de référence pour guider ou modifier le résultat. Décrivez la durée souhaitée (3-10 s) et le format d'image (16:9 ou 9:16) directement dans l'invite.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle vidéo Gemini utilisé pour générer la vidéo. | DYNAMIC_COMBO | Oui | "Omni Flash" |
| `seed` | La graine (seed) contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine (défaut : 42). | INT | Oui | 0 à 2147483647 |

### Entrées Omni Flash

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Décrivez la vidéo à générer. Spécifiez la durée et le format directement dans l'invite, par exemple « une séquence de 6 secondes en 16:9 ». La durée peut être de 3 à 10 secondes ; le format doit être 16:9 (paysage) ou 9:16 (portrait). La sortie est en 720p, 24 FPS, avec du son. | STRING | Oui | Minimum 1 caractère après suppression des espaces blancs |
| `temperature` | Contrôle le caractère aléatoire. Une valeur plus basse donne un résultat plus ciblé/déterministe, une valeur plus élevée donne plus de variété (défaut : 1,0). | FLOAT | Non | 0.0 à 2.0 |
| `top_p` | Échantillonnage nucleus : échantillonner à partir du plus petit ensemble de jetons dont la probabilité cumulée atteint `top_p` (défaut : 0,95). | FLOAT | Non | 0.0 à 1.0 |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Emplacement extensible : connectez une ou plusieurs images de référence (`image_1`...`image_14`) pour guider ou animer la vidéo. Jusqu'à 14 images au total. | IMAGE | Non | 0 à 14 images |
| `videos` | Emplacement extensible : connectez une ou plusieurs vidéos de référence (`video_1`...`video_3`) pour guider ou modifier. Jusqu'à 3 vidéos, chacune d'une durée maximale de 10 secondes. | VIDEO | Non | 0 à 3 vidéos, chacune max 10 secondes |

Notes :
- Si une entrée d'image contient plusieurs frames, chaque frame compte dans le maximum de 14 images.
- Lorsque des images ou vidéos de référence sont fournies, la taille totale des médias encodés doit rester inférieure à environ 90 Mo ; sinon le nœud génère une erreur.
- Lorsqu'aucune image ou vidéo de référence n'est fournie, le nœud génère la vidéo à partir de la seule invite texte.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo générée avec le son du modèle Gemini. | VIDEO |
| `STRING` | Toute réponse textuelle du modèle, telle que des raisonnements ou des explications. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/fr.md)

---
**Source fingerprint (SHA-256):** `648844868affb68298d2eac8ac20095bfe378d32e721396781de330ef6a6d69f`
