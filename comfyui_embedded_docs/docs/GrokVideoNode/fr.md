# Grok Video

Le nœud Grok Video génère une courte vidéo à partir d'une description textuelle. Il peut créer une vidéo de toutes pièces à l'aide d'un prompt, ou animer une image d'entrée unique, éventuellement guidée par un prompt. Le nœud envoie une requête à une API externe et renvoie la vidéo générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle à utiliser pour la génération vidéo. | COMBO | Oui | "grok-imagine-video"<br>"grok-imagine-video-1.5" |
| `prompt` | Description textuelle de la vidéo souhaitée. Optionnel pour grok-imagine-video-1.5 lorsqu'une image d'entrée est fournie. | STRING | Oui | - |
| `resolution` | La résolution de la vidéo de sortie. La 1080p n'est disponible que pour grok-imagine-video-1.5. | COMBO | Oui | "480p"<br>"720p"<br>"1080p" |
| `aspect_ratio` | Le rapport hauteur/largeur de la vidéo de sortie (par défaut : « auto »). | COMBO | Oui | "auto"<br>"16:9"<br>"4:3"<br>"3:2"<br>"1:1"<br>"2:3"<br>"3:4"<br>"9:16" |
| `duration` | La durée de la vidéo de sortie en secondes (par défaut : 6). | INT | Oui | 1 à 15 |
| `seed` | Graine utilisée pour déterminer si le nœud doit s'exécuter à nouveau ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0). | INT | Oui | 0 à 2147483647 |
| `image` | Image de départ facultative. Si elle est omise, la vidéo est générée à partir de la seule description textuelle. | IMAGE | Non | - |

**Remarque :**
- La résolution « 1080p » n'est disponible qu'avec le modèle `grok-imagine-video-1.5`. La sélectionner avec `grok-imagine-video` provoque une erreur.
- Une seule image d'entrée est prise en charge. Fournir plusieurs images provoque une erreur.
- Le `prompt` est requis, sauf si le modèle est défini sur `grok-imagine-video-1.5` et qu'une image d'entrée est fournie. Lorsqu'il est requis, le prompt doit contenir au moins 1 caractère après suppression des espaces.
- Le `seed` détermine uniquement si le nœud s'exécute à nouveau ; les résultats générés sont non déterministes quelle que soit la valeur du seed.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La vidéo générée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `c708c8cd78749aa533db63e2bc5938ef14fa78cf95f8ba4628d0c586f8723297`
