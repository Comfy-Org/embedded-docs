> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLora/fr.md)

Le nœud Create Hook LoRA génère des objets hook pour appliquer des modifications LoRA (Low-Rank Adaptation) aux modèles. Il charge un fichier LoRA spécifié et crée des hooks qui peuvent ajuster les forces du modèle et du CLIP, puis combine ces hooks avec tous les hooks existants qui lui sont transmis. Le nœud gère efficacement le chargement des LoRA en mettant en cache les fichiers LoRA précédemment chargés pour éviter les opérations redondantes.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `nom_lora` | STRING | Oui | Plusieurs options disponibles | Le nom du fichier LoRA à charger depuis le répertoire loras |
| `force_modele` | FLOAT | Oui | -20.0 à 20.0 | Le multiplicateur de force pour les ajustements du modèle (par défaut : 1.0) |
| `force_clip` | FLOAT | Oui | -20.0 à 20.0 | Le multiplicateur de force pour les ajustements du CLIP (par défaut : 1.0) |
| `crochets_precedents` | HOOKS | Non | N/A | Groupe de hooks existant optionnel à combiner avec les nouveaux hooks LoRA |

**Contraintes des paramètres :**
- Si `strength_model` et `strength_clip` sont tous deux définis sur 0, le nœud ignorera la création de nouveaux hooks LoRA et renverra les hooks existants inchangés
- Le nœud met en cache le dernier fichier LoRA chargé pour optimiser les performances lorsque le même LoRA est utilisé répétitivement

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `HOOKS` | HOOKS | Un groupe de hooks contenant les hooks LoRA combinés et tous les hooks précédents |