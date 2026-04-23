> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseKeypointExtractor/fr.md)

Le nœud SDPoseKeypointExtractor détecte les points clés de pose humaine à partir d'images d'entrée en utilisant le modèle SDPose. Il peut traiter des images complètes ou des régions spécifiques définies par des boîtes englobantes et produit les points clés détectés au format OpenPose, qui inclut les coordonnées pour chaque personne et un score de confiance pour chaque point clé.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle SDPose utilisé pour la détection des points clés. Doit être un modèle possédant un attribut `heatmap_head`, spécifiquement issu du dépôt SDPose. |
| `vae` | VAE | Oui | - | Le modèle VAE utilisé pour encoder les images d'entrée dans l'espace latent pour le traitement. |
| `image` | IMAGE | Oui | - | L'image d'entrée ou le lot d'images à partir desquelles extraire les points clés de pose. |
| `batch_size` | INT | Non | 1 à 10000 | Le nombre d'images à traiter simultanément en mode image complète (c'est-à-dire lorsque `bboxes` n'est pas fourni). Cela peut accélérer le traitement. (par défaut : 16) |
| `bboxes` | BOUNDINGBOX | Non | - | Boîtes englobantes optionnelles pour des détections plus précises. Requis pour la détection multi-personnes. Si fourni, le nœud extraira les points clés de chaque région spécifiée. |

**Contraintes des paramètres :**
*   L'entrée `model` doit être un modèle SDPose spécifique. Si le modèle fourni ne possède pas d'attribut `heatmap_head`, le nœud générera une erreur.
*   Le nœud fonctionne selon deux modes distincts basés sur l'entrée `bboxes` :
    1.  **Mode Boîte Englobante :** Lorsque `bboxes` est fourni, il traite chaque région spécifiée individuellement. Ce mode est requis pour détecter plusieurs personnes dans une seule image.
    2.  **Mode Image Complète :** Lorsque `bboxes` n'est pas fourni, il traite l'image entière par lots. Le paramètre `batch_size` ne s'applique que dans ce mode.

## Sorties

| Nom de la sortie | Type de données | Description |
|-------------|-----------|-------------|
| `keypoints` | POSE_KEYPOINT | Points clés au format de trame OpenPose (canvas_width, canvas_height, people). La sortie contient les personnes détectées, chacune avec un tableau de coordonnées de points clés (x, y) et leurs scores de confiance correspondants. |