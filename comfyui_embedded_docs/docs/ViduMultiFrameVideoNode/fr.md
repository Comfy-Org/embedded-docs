# Génération de vidéo multi-images Vidu

Ce nœud génère une vidéo en créant des transitions entre plusieurs images clés. Il démarre à partir d'une image initiale et anime une séquence d'images de fin et d'invites définies par l'utilisateur, produisant un fichier vidéo unique en sortie.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle Vidu à utiliser pour la génération vidéo. | COMBO | Oui | "viduq2-pro"<br>"viduq2-turbo" |
| `start_image` | L'image de départ. Le format d'image doit être compris entre 1:4 et 4:1. | IMAGE | Oui | Format d'image 1:4 à 4:1 |
| `seed` | Une valeur de graine (seed) pour la génération de nombres aléatoires afin d'assurer des résultats reproductibles (par défaut : 1). | INT | Oui | 0 à 2147483647 |
| `resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | "720p"<br>"1080p" |
| `frames` | Nombre de transitions d'images clés (2-9). La sélection d'une valeur révèle dynamiquement les entrées requises pour chaque image. | DYNAMIC_COMBO | Oui | "2"<br>"3"<br>"4"<br>"5"<br>"6"<br>"7"<br>"8"<br>"9" |

### Entrées des images (partagées par toutes les options de nombre d'images)

Lorsque `frames` est défini sur un nombre, les trois entrées suivantes sont affichées pour chaque image `i` de 1 à ce nombre. Par exemple, choisir « 3 » ajoute `prompt1` / `end_image1` / `duration1`, `prompt2` / `end_image2` / `duration2`, et `prompt3` / `end_image3` / `duration3`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt{i}` | Invite de texte pour la transition de l'image {i}. Champ de texte multiligne. 2000 caractères maximum. | STRING | Oui | Jusqu'à 2000 caractères |
| `end_image{i}` | Image de fin pour le segment {i}. Le format d'image doit être compris entre 1:4 et 4:1. | IMAGE | Oui | Format d'image 1:4 à 4:1 |
| `duration{i}` | Durée pour le segment {i} en secondes. | INT | Oui | 2 à 7 (par défaut : 4) |

**Remarques :**

- Toutes les entrées sont requises. `seed` possède une valeur par défaut mais reste une entrée requise.
- `start_image` et chaque `end_image{i}` doivent avoir un format d'image compris entre 1:4 et 4:1.
- Chaque `prompt{i}` a une longueur maximale de 2000 caractères.
- Chaque `duration{i}` doit être comprise entre 2 et 7 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Le fichier vidéo généré contenant toutes les transitions animées. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduMultiFrameVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `ad877532ba27444938b7b2e4634ac7f8a47db0f7fb53967d874ad38b44336dcf`
