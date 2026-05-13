> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoader/fr.md)

Ce nœud détecte automatiquement les modèles situés dans le dossier LoRA (y compris les sous-dossiers), le chemin de modèle correspondant étant `ComfyUI\models\loras`. Pour plus d'informations, veuillez consulter la section Installation des modèles LoRA.

Le nœud LoRA Loader est principalement utilisé pour charger des modèles LoRA. Vous pouvez considérer les modèles LoRA comme des filtres capables d'appliquer à vos images des styles, contenus et détails spécifiques :

- Appliquer des styles artistiques particuliers (comme la peinture à l'encre)
- Ajouter les caractéristiques de certains personnages (comme des personnages de jeux)
- Ajouter des détails spécifiques à l'image
Tout cela est réalisable grâce aux LoRA.

Si vous devez charger plusieurs modèles LoRA, vous pouvez directement chaîner plusieurs nœuds entre eux, comme illustré ci-dessous :

## Entrées

| Paramètre | Type de données | Description |
| --- | --- | --- |
| `model` | MODEL | Généralement utilisé pour se connecter au modèle de base |
| `clip` | CLIP | Généralement utilisé pour se connecter au modèle CLIP |
| `lora_name` | COMBO[STRING] | Sélectionnez le nom du modèle LoRA à utiliser |
| `strength_model` | FLOAT | Plage de valeurs de -100,0 à 100,0, généralement utilisée entre 0 et 1 pour la génération d'images courante. Des valeurs plus élevées entraînent des effets d'ajustement du modèle plus prononcés |
| `strength_clip` | FLOAT | Plage de valeurs de -100,0 à 100,0, généralement utilisée entre 0 et 1 pour la génération d'images courante. Des valeurs plus élevées entraînent des effets d'ajustement du modèle plus prononcés |

## Sorties

| Paramètre | Type de données | Description |
| --- | --- | --- |
| `model` | MODEL | Le modèle avec les ajustements LoRA appliqués |
| `clip` | CLIP | L'instance CLIP avec les ajustements LoRA appliqués |