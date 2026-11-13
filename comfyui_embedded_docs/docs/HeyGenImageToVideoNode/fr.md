# HeyGen Video 1.0 Image vers vidéo

Animez une image en vidéo avec un dialogue et un son synchronisés à l'aide de HeyGen Video 1.0. L'image connectée est utilisée comme première image, et la vidéo générée conserve son rapport d'aspect. Décrivez dans le prompt ce qui doit se produire, y compris les éventuelles répliques parlées. Le nœud téléverse l'image, crée la tâche vidéo, attend qu'elle se termine et renvoie la vidéo résultante.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Version du modèle utilisée pour la génération. (par défaut : `"heygen-video-1"`) | DYNAMIC_COMBO | Oui | `"heygen-video-1"` |
| `image` | Première image de la vidéo. Une seule image est requise ; un lot est rejeté. Recadrez l'image pour modifier la forme de la vidéo, car la sortie conserve le rapport d'aspect de cette image. | IMAGE | Oui | 1 image, rapport d'aspect 1:4 à 4:1 |
| `prompt` | Description de ce qui se passe dans la vidéo, y compris tout dialogue. (par défaut : chaîne vide) | STRING | Oui | 1 à 16000 caractères |
| `duration` | Durée de la vidéo de sortie en secondes. Ignorée lorsque `auto_duration` vaut `"enabled"`. (par défaut : 5) | INT | Oui | 5 à 30 |
| `resolution` | Résolution de sortie. (par défaut : `"768p"`) | COMBO | Oui | `"768p"`<br>`"480p"`<br>`"1080p"`<br>`"2k"` |
| `seed` | Graine pour la génération. Les résultats peuvent encore varier d'une exécution à l'autre avec la même graine. (par défaut : 42) | INT | Oui | 0 à 4294967295 |
| `auto_duration` | Lorsqu'il est activé, la durée de la vidéo suit le dialogue indiqué entre guillemets dans le prompt (8 à 30 secondes) et `duration` est ignoré. (par défaut : `"disabled"`) | COMBO | Non | `"disabled"`<br>`"enabled"` |

### Contraintes des paramètres

- **Image unique :** `image` doit contenir exactement une image. Connecter un lot (batch) déclenche une erreur.
- **Rapport d'aspect de l'image :** l'image ne doit pas être plus large que 4 fois sa hauteur ni plus haute que 4 fois sa largeur (entre 1:4 et 4:1) ; sinon, l'exécution échoue.
- **Prompt requis :** le prompt doit contenir au moins un caractère non blanc et au plus 16000 caractères.
- **Graine :** la graine détermine uniquement si le nœud se réexécute ; les résultats ne sont pas reproductibles avec la même graine.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo générée avec dialogue et son synchronisés, au rapport d'aspect de l'image d'entrée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `e711d1d84c6c73a2ee177903f982042086a57b3e1afff8390c6e5b3bcd09c914`
