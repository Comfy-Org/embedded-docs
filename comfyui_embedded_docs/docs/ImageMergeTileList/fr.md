# Fusionner une liste de tuiles en image

Ce nœud prend une liste de tuiles d'image et les fusionne en une seule image plus grande. Il est conçu pour reconstruire une image qui a été préalablement divisée en une grille de tuiles se chevauchant, en utilisant une technique de mélange pondéré pour créer un résultat final homogène.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `liste_d'images` | Une liste de tuiles d'image à fusionner. La première tuile de la liste est utilisée pour déterminer les dimensions des tuiles et le type de données pour l'ensemble du processus. | IMAGE | Oui | N/A |
| `largeur_finale` | La largeur de l'image fusionnée finale en pixels (valeur par défaut : 1024). | INT | Oui | 64 - 32768 |
| `hauteur_finale` | La hauteur de l'image fusionnée finale en pixels (valeur par défaut : 1024). | INT | Oui | 64 - 32768 |
| `chevauchement` | La quantité de chevauchement entre les tuiles adjacentes en pixels. Une valeur supérieure à 0 permet un effet de mélange homogène aux jonctions des tuiles (valeur par défaut : 128). | INT | Oui | 0 - 4096 |

**Remarque :** `image_list` est une liste d'entrée dynamique. Le nœud traite les tuiles dans l'ordre où elles sont fournies, jusqu'au nombre nécessaire pour remplir la grille définie par `final_width`, `final_height` et les dimensions de la première tuile. Si la liste contient plus de tuiles que nécessaire, les tuiles supplémentaires sont ignorées.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image fusionnée finale, reconstruite à partir des tuiles d'entrée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageMergeTileList/fr.md)

---
**Source fingerprint (SHA-256):** `f8f770ca2e9806d2feb55bb1dfe2c26b09d7a3506caf664990d8536ec5660c92`
