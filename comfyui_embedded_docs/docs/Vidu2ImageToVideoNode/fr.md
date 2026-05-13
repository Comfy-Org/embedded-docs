> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2ImageToVideoNode/fr.md)

Le nœud Vidu2 Image-to-Video Generation crée une séquence vidéo à partir d’une seule image d’entrée. Il utilise un modèle Vidu2 spécifié pour animer la scène en fonction d’un texte d’invite optionnel, en contrôlant la durée, la résolution et l’intensité du mouvement de la vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | COMBO | Oui | `"viduq2-pro-fast"`<br>`"viduq2-pro"`<br>`"viduq2-turbo"` | Le modèle Vidu2 à utiliser pour la génération vidéo. Différents modèles offrent des compromis variés entre vitesse et qualité. |
| `image` | IMAGE | Oui | - | Une image à utiliser comme image de départ de la vidéo générée. Une seule image est autorisée. |
| `invite` | STRING | Non | - | Un texte d’invite optionnel pour la génération vidéo (2000 caractères maximum). La valeur par défaut est une chaîne vide. |
| `durée` | INT | Oui | 1 à 10 | La durée de la vidéo générée en secondes. La valeur par défaut est 5. |
| `graine` | INT | Non | 0 à 2147483647 | Une valeur de graine pour la génération de nombres aléatoires, afin d’assurer des résultats reproductibles. La valeur par défaut est 1. |
| `résolution` | COMBO | Oui | `"720p"`<br>`"1080p"` | La résolution de sortie de la vidéo générée. Ce paramètre est avancé. |
| `amplitude du mouvement` | COMBO | Oui | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` | L’amplitude de mouvement des objets dans le cadre. Ce paramètre est avancé. |

**Contraintes :**

* L’entrée `image` doit contenir exactement une image.
* Le rapport hauteur/largeur de l’image d’entrée doit être compris entre 1:4 et 4:1.
* Le texte `prompt` est limité à un maximum de 2000 caractères.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | Le fichier vidéo généré. |

---
**Source fingerprint (SHA-256):** `204f8d2b9edf17c2c180480f98a852718416a54725d92e5fec574b8517ada398`
