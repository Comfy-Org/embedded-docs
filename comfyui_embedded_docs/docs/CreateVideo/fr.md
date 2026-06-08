Voici la traduction en français de la documentation du nœud Create Video :

Le nœud Créer une vidéo génère un fichier vidéo à partir d'une séquence d'images. Vous pouvez spécifier la vitesse de lecture en utilisant les images par seconde et, éventuellement, ajouter de l'audio à la vidéo. Le nœud combine vos images dans un format vidéo pouvant être lu avec la fréquence d'images spécifiée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `images` | Les images à partir desquelles créer une vidéo. | IMAGE | Oui | - |
| `fps` | Le nombre d'images par seconde pour la vitesse de lecture de la vidéo (par défaut : 30,0). | FLOAT | Oui | 1,0 - 120,0 |
| `audio` | L'audio à ajouter à la vidéo. | AUDIO | Non | - |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré contenant les images d'entrée et l'audio optionnel. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateVideo/fr.md)

---
**Source fingerprint (SHA-256):** `6da9a09542b5e357c0180c30018ec10facf06d1bdd3e4edee8172b8426802e3d`
