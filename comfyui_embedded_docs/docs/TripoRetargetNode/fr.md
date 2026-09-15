# Tripo : Modèle squeletté redirigé

Le TripoRetargetNode applique une animation prédéfinie à un modèle 3D riggé existant. Il prend l'ID de tâche d'un modèle précédemment riggé, envoie une requête de retargeting à l'API Tripo et télécharge le fichier animé résultant. Le modèle animé peut être renvoyé au format GLB ou FBX, avec une géométrie de maillage optionnelle et une lecture sur place optionnelle.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `ID_tâche_modèle_original` | L'ID de tâche du modèle 3D précédemment riggé à retargeter. La tâche référencée doit être une tâche de rig. | RIG_TASK_ID | Oui | - |
| `animation` | L'animation prédéfinie à appliquer au modèle riggé. Les animations `preset:*` fonctionnent avec les deux modèles de rig. Les animations `preset:biped:*` sont conçues pour les rigs du modèle v1.0-20240301 ; un rig v2.5 accepte uniquement chop, climb, dive, fall, hurt, idle, jump, run, shoot, slash, turn et walk. | COMBO | Oui | `"preset:idle"`<br>`"preset:walk"`<br>`"preset:run"`<br>`"preset:dive"`<br>`"preset:climb"`<br>`"preset:jump"`<br>`"preset:slash"`<br>`"preset:shoot"`<br>`"preset:hurt"`<br>`"preset:fall"`<br>`"preset:turn"`<br>`"preset:quadruped:walk"`<br>`"preset:hexapod:walk"`<br>`"preset:octopod:walk"`<br>`"preset:serpentine:march"`<br>`"preset:aquatic:march"`<br>plus d'options `"preset:biped:*"` supplémentaires affichées dans l'interface |
| `out_format` | Format du fichier de sortie ; le résultat arrive sur la sortie correspondante. (par défaut : glb) | COMBO | Non | `"glb"`<br>`"fbx"` |
| `export_with_geometry` | Inclure le maillage dans l'export ; si désactivé, exporte uniquement le squelette animé. (par défaut : True) | BOOLEAN | Non | True<br>False |
| `animate_in_place` | Lire l'animation sur place, sans déplacement de la racine. (par défaut : False) | BOOLEAN | Non | True<br>False |
| `auth_token_comfy_org` | Jeton d'authentification pour l'accès à l'API Comfy.org (paramètre masqué). | AUTH_TOKEN_COMFY_ORG | Non | - |
| `api_key_comfy_org` | Clé API pour l'accès au service Comfy.org (paramètre masqué). | API_KEY_COMFY_ORG | Non | - |
| `unique_id` | Identifiant unique pour le suivi de l'opération (paramètre masqué). | UNIQUE_ID | Non | - |

Remarque : Les animations du groupe `preset:*` fonctionnent avec les deux modèles de rig. Les animations du groupe `preset:biped:*` sont conçues pour les rigs du modèle v1.0-20240301 ; un rig v2.5 accepte uniquement chop, climb, dive, fall, hurt, idle, jump, run, shoot, slash, turn et walk. Si le rig référencé a été créé avec la spécification Mixamo et une version de modèle commençant par `v1.0`, l'appel de retargeting échoue avec une erreur. Le format de sortie demandé doit être GLB ou FBX ; si le service renvoie un autre type de fichier, le nœud lève une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Le fichier de modèle 3D animé généré (uniquement pour la rétrocompatibilité). | STRING |
| `retarget task_id` | L'ID de tâche pour le suivi de l'opération de retargeting. | RETARGET_TASK_ID |
| `GLB` | Le modèle 3D animé au format GLB. Renseigné lorsque `out_format` vaut glb. | FILE3DGLB |
| `FBX` | Le modèle 3D animé au format FBX. Renseigné lorsque `out_format` vaut fbx. | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/fr.md)

---
**Source fingerprint (SHA-256):** `4814858b940ece13f85010ff81fcdac0258fe8550aebd914be2613e8f40c0e5a`
