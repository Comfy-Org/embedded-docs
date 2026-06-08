Le nœud SDPoseKeypointExtractor détecte les points clés de pose humaine à partir d'images d'entrée en utilisant le modèle SDPose. Il peut traiter des images entières ou des régions spécifiques définies par des boîtes englobantes et produit les points clés détectés au format OpenPose, qui inclut les coordonnées pour chaque personne ainsi qu'un score de confiance pour chaque point clé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle SDPose utilisé pour la détection des points clés. Doit être un modèle possédant un attribut `heatmap_head`, spécifiquement issu du dépôt SDPose. | MODEL | Oui | - |
| `vae` | Le modèle VAE utilisé pour encoder les images d'entrée dans l'espace latent avant traitement. | VAE | Oui | - |
| `image` | L'image d'entrée ou le lot d'images à partir duquel extraire les points clés de pose. | IMAGE | Oui | - |
| `batch_size` | Le nombre d'images à traiter simultanément en mode image entière (c'est-à-dire lorsque `bboxes` n'est pas fourni). Cela peut accélérer le traitement. (par défaut : 16) | INT | Non | 1 à 10000 |
| `bboxes` | Boîtes englobantes optionnelles pour des détections plus précises. Requises pour la détection multi-personnes. Si fournies, le nœud extrait les points clés de chaque région spécifiée. | BOUNDINGBOX | Non | - |

**Contraintes des paramètres :**
*   L'entrée `model` doit être un modèle SDPose spécifique. Si le modèle fourni ne possède pas d'attribut `heatmap_head`, le nœud générera une erreur.
*   Le nœud fonctionne selon deux modes distincts en fonction de l'entrée `bboxes` :
    1.  **Mode Boîte Englobante :** Lorsque `bboxes` est fourni, il traite chaque région spécifiée individuellement. Ce mode est requis pour détecter plusieurs personnes dans une seule image.
    2.  **Mode Image Entière :** Lorsque `bboxes` n'est pas fourni, il traite l'image entière par lots. Le paramètre `batch_size` s'applique uniquement dans ce mode.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `keypoints` | Points clés au format de trame OpenPose (largeur_canvas, hauteur_canvas, personnes). La sortie contient les personnes détectées, chacune avec un tableau de coordonnées de points clés (x, y) et leurs scores de confiance correspondants. | POSE_KEYPOINT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseKeypointExtractor/fr.md)

---
**Source fingerprint (SHA-256):** `7903b51c9137aa08bb8843362740fcf93cea9c09d142bd1db3b5eee945c853e4`
