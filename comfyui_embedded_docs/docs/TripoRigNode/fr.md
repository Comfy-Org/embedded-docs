# Tripo : Modèle squeletté

Ce nœud prend un modèle 3D Tripo existant et en crée une version riggée, c'est-à-dire que le modèle reçoit un squelette pour pouvoir être animé. Vous fournissez l'ID de tâche du modèle à rigger, choisissez la version de rig, le type de squelette, le style de nommage des os et le format de fichier de sortie ; le nœud envoie la tâche à Tripo, attend qu'elle se termine, puis renvoie le résultat téléchargé.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `original_model_task_id` | L'ID de tâche du modèle 3D original à rigger. Il s'agit généralement de l'ID produit par un nœud de génération de modèle Tripo antérieur. | MODEL_TASK_ID | Oui | - |
| `model_version` | Version du modèle de rig à utiliser. v1.0 : personnages humanoïdes (bipèdes) uniquement, plus de 90 préréglages d'animation. v2.5 : créatures non humanoïdes (quadrupèdes, hexapodes, octopodes, aviaires, serpentines, aquatiques). Par défaut : `v1.0-20240301`. | COMBO | Non | "v1.0-20240301"<br>"v2.5-20260210" |
| `rig_type` | Type de squelette. « auto » exécute d'abord la vérification gratuite du rig de Tripo et utilise le type recommandé. Par défaut : « auto ». | COMBO | Non | "auto"<br>"biped"<br>"quadruped"<br>"hexapod"<br>"octopod"<br>"avian"<br>"serpentine"<br>"aquatic" |
| `spec` | Nommage des os : natif Tripo ou compatible Mixamo. Tripo ne peut pas réaffecter ses préréglages d'animation sur un rig v1.0 créé avec la spécification « mixamo » ; utilisez « tripo » pour Tripo: Retarget rigged model. Par défaut : « tripo ». | COMBO | Non | "tripo"<br>"mixamo" |
| `out_format` | Format de fichier de sortie ; le résultat arrive sur la sortie correspondante. Par défaut : « glb ». | COMBO | Non | "glb"<br>"fbx" |

**Remarque :** La version de modèle v1.0 (`v1.0-20240301`) ne prend en charge que les squelettes bipèdes. Si un `rig_type` non bipède est utilisé avec cette version, le nœud génère une erreur et vous indique d'utiliser `v2.5-20260210` à la place.

**Remarque :** Lorsque `rig_type` vaut « auto », Tripo vérifie d'abord si le modèle peut être riggé et choisit le type de squelette recommandé. Si Tripo signale que le modèle ne peut pas être riggé, le nœud échoue avec une erreur.

**Remarque :** Le nœud s'attend à ce que Tripo renvoie un fichier GLB ou FBX. Si Tripo renvoie un autre type de fichier, le nœud génère une erreur.

**Remarque :** Seule la sortie correspondant à `out_format` est alimentée : `GLB` lorsque `out_format` vaut « glb », et `FBX` lorsque `out_format` vaut « fbx ». L'autre sortie 3D est vide.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_file` | Le nom du fichier de modèle riggé généré (ID de tâche plus extension de format). Conservé uniquement pour la compatibilité ascendante. | STRING |
| `rig task_id` | L'ID de tâche pour suivre le processus de génération du rig. | RIG_TASK_ID |
| `GLB` | Le modèle riggé sous forme de fichier 3D GLB. Alimenté lorsque `out_format` vaut « glb ». | FILE3DGLB |
| `FBX` | Le modèle riggé sous forme de fichier 3D FBX. Alimenté lorsque `out_format` vaut « fbx ». | FILE3DFBX |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigNode/fr.md)

---
**Source fingerprint (SHA-256):** `b9c1b6d27b6278bcee4fc22e11c11e65cd22ea92cab3fc6c74f84d3deb2024d6`
