# Exécuter la prédiction de corps SAM3D

SAM3D Body Prediction exécute l’estimation de pose 3D du corps et des mains sur les images d’entrée, en détectant une ou plusieurs personnes par image. Des données de suivi ou des boîtes englobantes peuvent être fournies pour améliorer la détection ; lorsque ni l’un ni l’autre n’est fourni, le nœud revient à une détection d’une seule personne sur l’image complète.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `sam3d_body_model` | Le modèle de corps SAM3D à utiliser pour la prédiction. | SAM3D_BODY_MODEL | Oui | — |
| `image` | Image ou lot d’images sur lesquelles exécuter la prédiction de corps. | IMAGE | Oui | — |
| `track_data` | Données de suivi provenant de SAM3 Video Track, requises pour la détection multi-personnes. | SAM3_TRACK_DATA | Non | — |
| `bboxes` | Boîtes englobantes par image utilisées pour une meilleure détection. Peuvent être utilisées comme alternative aux données de suivi. | BBOX | Non | — |
| `run_hand_refinement` | Améliore la pose des mains au prix d’un temps d’inférence et d’une utilisation mémoire supplémentaires. Valeur par défaut : true. | BOOLEAN | Non | true<br>false |
| `fov` | Champ de vision vertical en degrés. Affecte la profondeur prédite et l’échelle absolue. 0 = repli sur ~53° (16:9). Valeur par défaut : 0.0. | FLOAT | Non | 0.0 ou plus |
| `batch_size` | Nombre maximal de recadrages de personnes à traiter par lot. Des valeurs plus élevées utilisent plus de VRAM pour une inférence plus rapide. Valeur par défaut : 64. | INT | Non | 1 à 512 |

Remarque : lorsque `track_data` est fourni, il a priorité sur `bboxes`. Si ni `track_data` ni `bboxes` n’est fourni, le nœud revient à la détection d’une seule personne sur l’image complète. Les boîtes englobantes peuvent être fournies pour une seule image (appliquées à chaque image) ou par image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `mhr_pose_data` | Ensemble de données de pose du corps contenant les résultats de détection de pose par image, la géométrie du visage, la taille de l’image d’entrée, les couleurs canoniques des sommets et un masque de sommets des mains. | MHR_POSE_DATA |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Predict/fr.md)

---
**Source fingerprint (SHA-256):** `f1039349cd2809423053bffde1c7d119c7c42f217327d23c608b1224d183770e`
