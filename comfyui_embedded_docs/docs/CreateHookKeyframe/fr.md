> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframe/fr.md)

Le nœud Créer une image clé de hook vous permet de définir des points spécifiques dans un processus de génération où le comportement du hook change. Il crée des images clés qui modifient la force des hooks à des pourcentages particuliers de l'avancement de la génération, et ces images clés peuvent être chaînées ensemble pour créer des schémas de planification complexes.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `strength_mult` | FLOAT | Oui | -20.0 à 20.0 | Multiplicateur de la force du hook à cette image clé (par défaut : 1.0) |
| `start_percent` | FLOAT | Oui | 0.0 à 1.0 | Le point de pourcentage dans le processus de génération où cette image clé prend effet (par défaut : 0.0) |
| `prev_hook_kf` | HOOK_KEYFRAMES | Non | - | Groupe d'images clés de hook précédent facultatif auquel ajouter cette image clé |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `HOOK_KF` | HOOK_KEYFRAMES | Un groupe d'images clés de hook incluant l'image clé nouvellement créée |

---
**Source fingerprint (SHA-256):** `51893311a0623cafcf8c2d8af00e4005ca2fea2df9474e87d7d4b332b38435c3`
