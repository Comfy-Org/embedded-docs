# HeyGen Video 1.0 Image to Video

Animez une image pour en faire une vidéo avec un dialogue et un son synchronisés à l’aide de HeyGen Video 1.0. L’image connectée est utilisée comme première image, et la vidéo générée conserve son rapport d’aspect. Décrivez dans le prompt ce qui doit se produire, y compris les éventuelles répliques parlées. Le nœud téléverse l’image, crée la tâche vidéo, attend qu’elle se termine et renvoie la vidéo résultante.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Version du modèle utilisée pour la génération. (par défaut : `"heygen-video-1"`) | DYNAMIC_COMBO | Oui | `"heygen-video-1"` |
| `image` | Première image de la vidéo. Exactement une image est requise ; un lot est rejeté. Recadrez l’image pour modifier la forme de la vidéo, car la sortie conserve le rapport d’aspect de cette image. | IMAGE | Oui | 1 image, rapport d’aspect 1:4 à 4:1 |
| `prompt` | Description de ce qui se passe dans la vidéo, y compris tout dialogue. (par défaut : chaîne vide) | STRING | Oui | 1 à 32000 caractères |
| `duration` | Durée de la vidéo de sortie en secondes. (par défaut : 5) | INT | Oui | 5 à 15 |
| `resolution` | Résolution de sortie. (par défaut : `"768p"`) | COMBO | Oui | `"768p"`<br>`"480p"` |
| `seed` | Graine pour la génération. Les résultats peuvent encore varier entre les exécutions avec la même graine. (par défaut : 42) | INT | Oui | 0 à 4294967295 |

### Contraintes des paramètres

- **Image unique :** `image` doit contenir exactement une image. Connecter un lot déclenche une erreur.
- **Rapport d’aspect de l’image :** l’image ne doit pas être plus large que 4 fois sa hauteur ni plus haute que 4 fois sa largeur (entre 1:4 et 4:1) ; sinon l’exécution échoue.
- **Prompt requis :** le prompt doit contenir au moins un caractère non blanc et au plus 32000 caractères.
- **Graine :** la graine détermine uniquement si le nœud se réexécute ; les résultats ne sont pas reproductibles avec la même graine.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo générée avec un dialogue et un son synchronisés, au rapport d’aspect de l’image d’entrée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `1de530dcc98f2324f6ef4e2cfe309a717a12116382e9885aca14a8ae0be4de39`
