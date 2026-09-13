# Génération de vidéo multi-images Vidu

Ce nœud génère une vidéo en créant des transitions entre plusieurs images clés. Il part d'une image initiale et anime une séquence d'images finales et de prompts définis par l'utilisateur, produisant un seul fichier vidéo en sortie.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle Vidu à utiliser pour la génération vidéo. | COMBO | Oui | "viduq2-pro"<br>"viduq2-turbo" |
| `start_image` | L'image de trame de départ. Le rapport d'aspect doit être compris entre 1:4 et 4:1. | IMAGE | Oui | Rapport d'aspect 1:4 à 4:1 |
| `seed` | Une valeur de graine pour la génération de nombres aléatoires afin de garantir des résultats reproductibles (par défaut : 1). | INT | Oui | 0 à 2147483647 |
| `resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | "720p"<br>"1080p" |
| `frames` | Nombre de transitions entre images clés (2-9). La sélection d'une valeur révèle dynamiquement les entrées requises pour chaque trame. | DYNAMIC_COMBO | Oui | "2"<br>"3"<br>"4"<br>"5"<br>"6"<br>"7"<br>"8"<br>"9" |

### Entrées de trame (partagées par toutes les options de nombre de trames)

Lorsque `frames` est défini sur un nombre, les trois entrées suivantes sont affichées pour chaque trame `i`, de 1 à ce nombre. Par exemple, choisir "3" ajoute `prompt1` / `end_image1` / `duration1`, `prompt2` / `end_image2` / `duration2` et `prompt3` / `end_image3` / `duration3`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt{i}` | Prompt textuel pour la transition de la trame {i}. Champ de texte multiligne. Maximum 2000 caractères. | STRING | Oui | Jusqu'à 2000 caractères |
| `end_image{i}` | Image de trame de fin pour le segment {i}. Le rapport d'aspect doit être compris entre 1:4 et 4:1. | IMAGE | Oui | Rapport d'aspect 1:4 à 4:1 |
| `duration{i}` | Durée du segment {i} en secondes (par défaut : 4). | INT | Oui | 2 à 7 |

**Notes :**

- Toutes les entrées sont requises. `seed` possède une valeur par défaut mais reste une entrée requise.
- `start_image` et chaque `end_image{i}` doivent avoir un rapport d'aspect compris entre 1:4 et 4:1.
- Chaque `prompt{i}` a une longueur maximale de 2000 caractères.
- Chaque `duration{i}` doit être comprise entre 2 et 7 secondes.
- Le nombre de trames peut être compris entre 2 et 9, donc les indices de trame possibles vont de 1 à 9.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Le fichier vidéo généré contenant toutes les transitions animées. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduMultiFrameVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `ad877532ba27444938b7b2e4634ac7f8a47db0f7fb53967d874ad38b44336dcf`
