# Génération vidéo Vidu à partir d'image

Voici la traduction de la documentation du nœud ViduImageToVideoNode :

Le nœud Vidu Image To Video Generation crée une courte vidéo à partir d'une image de départ et d'une description textuelle optionnelle. Il utilise un modèle d'IA pour générer un contenu vidéo qui prolonge l'image fournie, et retourne la vidéo résultante.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Nom du modèle (par défaut : viduq1) | COMBO | Oui | `viduq1` |
| `image` | Image utilisée comme première image de la vidéo générée | IMAGE | Oui | - |
| `prompt` | Description textuelle pour la génération vidéo (par défaut : vide) | STRING | Non | - |
| `durée` | Durée de la vidéo de sortie en secondes (par défaut : 5, fixée à 5 secondes) | INT | Non | 5-5 |
| `graine` | Graine pour la génération vidéo (0 pour aléatoire) (par défaut : 0) | INT | Non | 0-2147483647 |
| `résolution` | Les valeurs prises en charge peuvent varier selon le modèle et la durée (par défaut : 1080p) | COMBO | Non | `1080p` |
| `amplitude_mouvement` | L'amplitude de mouvement des objets dans l'image (par défaut : auto) | COMBO | Non | `auto`<br>`small`<br>`medium`<br>`large` |

**Contraintes :**

- Une seule image d'entrée est autorisée (ne peut pas traiter plusieurs images).
- L'image d'entrée doit avoir un rapport hauteur/largeur compris entre 1:4 et 4:1.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La vidéo générée en sortie | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `064b3efba8219770595e68a6607a6f8113d1be7c9f3863a4740ee5c3a146d91e`
