# Tripo : Vérification d’armature

Ce nœud envoie l'ID d'une tâche de modèle 3D Tripo terminée à l'API Tripo et vérifie si ce modèle peut être riggé. Il attend la fin de la vérification, puis renvoie un résultat oui/non ainsi que le type de squelette recommandé par Tripo pour le modèle.

<Note>
Tripo conserve les enregistrements de tâches sur ses serveurs pendant 7 jours (à compter du 1er décembre 2026). Un ID de tâche plus ancien ne peut plus être résolu, donc relancer un workflow enregistré après ce délai échoue sur ce nœud. Pour continuer, relancez le nœud Tripo précédent pour créer un nouvel ID de tâche, ou réimportez le modèle que vous avez déjà téléchargé avec **Tripo : Importer un modèle**.
</Note>

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_task_id` | L'ID de tâche Tripo du modèle à analyser. Il identifie un modèle qui a été précédemment généré, importé ou autrement créé via une tâche Tripo. | MODEL_TASK_ID | Oui | N/A |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `riggable` | Indique si le modèle peut être riggé. | BOOLEAN |
| `rig_type` | Squelette recommandé : biped, quadruped, hexapod, octopod, avian, serpentine ou aquatic ; 'others' lorsque le modèle n'est pas riggable. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRigCheckNode/fr.md)

---
**Source fingerprint (SHA-256):** `3aa0bc194e887804b92ca1f9f2b12997c73e111fb282c5de96e55f664c21545e`
