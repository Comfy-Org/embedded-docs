> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduImageToVideoNode/fr.md)

Voici la traduction de la documentation du nœud ViduImageToVideoNode :

Le nœud Vidu Image To Video Generation crée une courte vidéo à partir d'une image de départ et d'une description textuelle optionnelle. Il utilise un modèle d'IA pour générer un contenu vidéo qui prolonge l'image fournie, et retourne la vidéo résultante.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | COMBO | Oui | `viduq1` | Nom du modèle (par défaut : viduq1) |
| `image` | IMAGE | Oui | - | Image utilisée comme première image de la vidéo générée |
| `prompt` | STRING | Non | - | Description textuelle pour la génération vidéo (par défaut : vide) |
| `durée` | INT | Non | 5-5 | Durée de la vidéo de sortie en secondes (par défaut : 5, fixée à 5 secondes) |
| `graine` | INT | Non | 0-2147483647 | Graine pour la génération vidéo (0 pour aléatoire) (par défaut : 0) |
| `résolution` | COMBO | Non | `1080p` | Les valeurs prises en charge peuvent varier selon le modèle et la durée (par défaut : 1080p) |
| `amplitude_mouvement` | COMBO | Non | `auto`<br>`small`<br>`medium`<br>`large` | L'amplitude de mouvement des objets dans l'image (par défaut : auto) |

**Contraintes :**

- Une seule image d'entrée est autorisée (ne peut pas traiter plusieurs images).
- L'image d'entrée doit avoir un rapport hauteur/largeur compris entre 1:4 et 4:1.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | VIDEO | La vidéo générée en sortie |

---
**Source fingerprint (SHA-256):** `064b3efba8219770595e68a6607a6f8113d1be7c9f3863a4740ee5c3a146d91e`
