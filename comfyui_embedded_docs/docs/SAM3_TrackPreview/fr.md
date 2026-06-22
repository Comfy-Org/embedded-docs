# Aperçu du suivi SAM3

Voici la traduction en français de la documentation technique du nœud ComfyUI :

## Aperçu

Ce nœud crée un aperçu vidéo des objets suivis, en dessinant chaque objet suivi avec une superposition de couleur distincte et une étiquette numérique. Il ne produit aucun tenseur d'image ou de vidéo — à la place, il enregistre directement la vidéo d'aperçu résultante dans un fichier temporaire.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `données_suivi` | Les données de suivi contenant les masques compressés et les informations d'objets provenant d'un nœud de suivi SAM3. | TRACK_DATA | Oui | - |
| `images` | Images d'entrée facultatives à utiliser comme arrière-plan pour l'aperçu. Si non fournies, un arrière-plan noir est utilisé. | IMAGE | Non | - |
| `opacité` | L'opacité de la superposition de couleur appliquée aux objets suivis (par défaut : 0,5). | FLOAT | Non | 0,0 à 1,0 (pas : 0,05) |
| `ips` | La fréquence d'images de la vidéo de sortie (par défaut : 24,0). | FLOAT | Non | 1,0 à 120,0 (pas : 1,0) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `ui` | Un élément d'interface utilisateur qui affiche la vidéo d'aperçu générée. Aucune donnée tensorielle n'est retournée. | PREVIEW_VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackPreview/fr.md)

---
**Source fingerprint (SHA-256):** `8300d4fa89c7bbc481ac9a59868ede0e3c9413faa63d56c16a4f603ef878e877`
