# Charger le jeu de données d'entraînement

```markdown
Ce nœud charge un ensemble de données d'entraînement encodé (latents et conditionnement) depuis le disque pour une utilisation en entraînement. Après avoir sélectionné un dossier d'ensemble de données préalablement sauvegardé, il lit tous les fichiers shard qu'il contient et renvoie les vecteurs latents combinés et les données de conditionnement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `folder_name` | Ensemble de données sauvegardé à charger, depuis le répertoire des ensembles de données. | COMBO | Oui | Rempli dynamiquement avec tous les dossiers d'ensembles de données trouvés dans les répertoires d'ensembles de données enregistrés. Seuls les dossiers contenant un fichier `metadata.json` ou des fichiers `.safetensors` sont répertoriés. |

**Remarque :** Le dossier d'ensemble de données sélectionné doit être un sous-dossier d'un répertoire d'ensembles de données enregistré et doit contenir au moins un fichier shard nommé `shard_*.pkl` ; sinon le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `latents` | Liste de dicts latents chargés depuis les fragments de l'ensemble de données, chacun contenant un tenseur `samples`. | LATENT |
| `conditioning` | Liste de listes de conditionnement chargées depuis les fragments de l'ensemble de données, une par échantillon. | CONDITIONING |
```

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/fr.md)

---
**Source fingerprint (SHA-256):** `9f914b27f067460f6f3b54f3f2a7bb793c65b99c85e8aa14ab64894be26bd816`
