> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRefineNode/fr.md)

Voici la traduction en français de la documentation technique du nœud ComfyUI **TripoRefineNode** :

---

Le TripoRefineNode affine les modèles 3D bruts créés spécifiquement par les modèles Tripo v1.4. Il prend un identifiant de tâche de modèle et le traite via l'API Tripo pour générer une version améliorée du modèle. Ce nœud est conçu pour fonctionner exclusivement avec les modèles bruts produits par les modèles Tripo v1.4.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `ID_tâche_modèle` | MODEL_TASK_ID | Oui | - | Doit être un modèle Tripo v1.4 |

**Remarque :** Ce nœud accepte uniquement les modèles bruts créés par les modèles Tripo v1.4. L'utilisation de modèles provenant d'autres versions peut entraîner des erreurs.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `modèle task_id` | STRING | Le chemin d'accès ou la référence au modèle affiné (uniquement pour la rétrocompatibilité) |
| `GLB` | MODEL_TASK_ID | L'identifiant de tâche pour l'opération du modèle affiné |
| `GLB` | FILE3DGLB | Le modèle 3D affiné au format GLB |

---
**Source fingerprint (SHA-256):** `136093c7cdd7eb33b55e862f4b8c0554de7bde656a7e0139efb63323ad041c32`
