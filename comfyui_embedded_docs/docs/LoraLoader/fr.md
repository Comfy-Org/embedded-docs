Ce nœud détecte automatiquement les modèles situés dans le dossier LoRA (y compris les sous-dossiers) avec le chemin de modèle correspondant `ComfyUI\models\loras`.

Le nœud Chargeur LoRA est principalement utilisé pour charger des modèles LoRA. Vous pouvez considérer les modèles LoRA comme des filtres qui peuvent donner à vos images des styles, contenus et détails spécifiques :

- Appliquer des styles artistiques spécifiques (comme la peinture à l'encre)
- Ajouter des caractéristiques de certains personnages (comme des personnages de jeux)
- Ajouter des détails spécifiques à l'image
Tout cela peut être réalisé grâce à LoRA.

Si vous devez charger plusieurs modèles LoRA, vous pouvez directement enchaîner plusieurs nœuds, comme montré ci-dessous :

## Entrées

| Nom du Paramètre | Type de Données | Fonction |
| --- | --- | --- |
| `model` | MODEL | Généralement utilisé pour se connecter au modèle de base |
| `clip` | CLIP | Généralement utilisé pour se connecter au modèle CLIP |
| `lora_name` | COMBO[STRING] | Sélectionner le nom du modèle LoRA à utiliser |
| `strength_model` | FLOAT | Plage de valeurs de -100.0 à 100.0, typiquement utilisée entre 0~1 pour la génération quotidienne d'images. Des valeurs plus élevées donnent des effets d'ajustement plus prononcés |
| `strength_clip` | FLOAT | Plage de valeurs de -100.0 à 100.0, typiquement utilisée entre 0~1 pour la génération quotidienne d'images. Des valeurs plus élevées donnent des effets d'ajustement plus prononcés |

## Sorties

| Nom du Paramètre | Type de Données | Fonction |
| --- | --- | --- |
| `model` | MODEL | Le modèle avec les ajustements LoRA appliqués |
| `clip` | CLIP | L'instance CLIP avec les ajustements LoRA appliqués |
