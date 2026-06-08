Ce nœud génère une vidéo par interpolation entre une image de début et une image de fin fournies, guidée par une description textuelle. Il utilise un modèle Vidu spécifié pour créer une transition fluide entre les deux images sur une durée définie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle Vidu à utiliser pour la génération vidéo. | COMBO | Oui | `"viduq2-pro-fast"`<br>`"viduq2-pro"`<br>`"viduq2-turbo"` |
| `image de début` | L'image de départ pour la séquence vidéo. Une seule image est autorisée. | IMAGE | Oui | - |
| `image de fin` | L'image de fin pour la séquence vidéo. Une seule image est autorisée. | IMAGE | Oui | - |
| `invite` | Une description textuelle guidant la génération vidéo (2000 caractères maximum). | STRING | Oui | - |
| `durée` | La durée de la vidéo générée en secondes (par défaut : 5). | INT | Non | 2 à 8 |
| `graine` | Un nombre utilisé pour initialiser la génération aléatoire afin d'obtenir des résultats reproductibles (par défaut : 1). | INT | Non | 0 à 2147483647 |
| `résolution` | La résolution de sortie de la vidéo générée. | COMBO | Non | `"720p"`<br>`"1080p"` |
| `amplitude du mouvement` | L'amplitude de mouvement des objets dans le cadre. | COMBO | Non | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Remarque :** Les images `first_frame` et `end_frame` doivent avoir des rapports hauteur/largeur similaires. Le nœud vérifiera que leurs rapports hauteur/largeur se situent dans une plage relative de 0,8 à 1,25.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2StartEndToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `0a2a125fcb0a519e3aa98ed846f0c7bdc14644a27aaaab3953d55945f787de2a`
