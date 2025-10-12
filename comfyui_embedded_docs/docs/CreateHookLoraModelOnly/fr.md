> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLoraModelOnly/fr.md)

Ce nœud crée un crochet LoRA (Low-Rank Adaptation) qui s'applique uniquement au composant modèle, vous permettant de modifier le comportement du modèle sans affecter le composant CLIP. Il charge un fichier LoRA et l'applique avec une force spécifiée au modèle tout en laissant le composant CLIP inchangé. Le nœud peut être chaîné avec des crochets précédents pour créer des pipelines de modification complexes.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `nom_lora` | STRING | Oui | Plusieurs options disponibles | Le nom du fichier LoRA à charger depuis le dossier loras |
| `force_modele` | FLOAT | Oui | -20.0 à 20.0 | Le multiplicateur de force pour appliquer le LoRA au composant modèle (par défaut : 1.0) |
| `crochets_precedents` | HOOKS | Non | - | Crochets précédents optionnels à chaîner avec ce crochet |

## Sorties

| Sortie | Type de données | Description |
|-------------|-----------|-------------|
| `hooks` | HOOKS | Le crochet LoRA créé qui peut être appliqué au traitement du modèle |
