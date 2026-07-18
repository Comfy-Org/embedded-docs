Voici la traduction en français de la documentation technique du nœud ComfyUI **TripoRefineNode** :

---

Le TripoRefineNode affine les modèles 3D bruts créés spécifiquement par les modèles Tripo v1.4. Il prend un identifiant de tâche de modèle et le traite via l'API Tripo pour générer une version améliorée du modèle. Ce nœud est conçu pour fonctionner exclusivement avec les modèles bruts produits par les modèles Tripo v1.4.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `ID_tâche_modèle` | Doit être un modèle Tripo v1.4 | MODEL_TASK_ID | Oui | - |

**Remarque :** Ce nœud accepte uniquement les modèles bruts créés par les modèles Tripo v1.4. L'utilisation de modèles provenant d'autres versions peut entraîner des erreurs.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `fichier_modèle` | Le chemin d'accès ou la référence au modèle affiné (uniquement pour la rétrocompatibilité) | STRING |
| `modèle task_id` | L'identifiant de tâche pour l'opération du modèle affiné | MODEL_TASK_ID |
| `GLB` | Le modèle 3D affiné au format GLB | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRefineNode/fr.md)

---
**Source fingerprint (SHA-256):** `136093c7cdd7eb33b55e862f4b8c0554de7bde656a7e0139efb63323ad041c32`
