# Appliquer Anima LLLite

AnimaLLLiteApply applique un patch d'animation léger à un modèle de diffusion, permettant une génération image à image contrôlée avec une force et un minutage réglables. Il intègre un patch de modèle préconfiguré avec une image d'entrée et un masque facultatif, en modifiant les couches d'attention et MLP du modèle afin d'influencer le processus de génération.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle de diffusion de base auquel appliquer le patch | MODEL | Oui | |
| `correctif du modèle` | Le patch d'animation préconfiguré à appliquer | MODEL_PATCH | Oui | |
| `image` | L'image de référence pour guider la génération. Seuls les 3 premiers canaux de couleur (RVB) sont utilisés | IMAGE | Oui | |
| `intensité` | La force de l'effet du patch (par défaut : 1.0, pas : 0.01) | FLOAT | Oui | -10.0 à 10.0 |
| `pourcentage de début` | Le pourcentage du processus de débruitage auquel le patch commence à prendre effet (par défaut : 0.0, pas : 0.001) | FLOAT | Oui | 0.0 à 1.0 |
| `pourcentage de fin` | Le pourcentage du processus de débruitage auquel le patch cesse de prendre effet (par défaut : 1.0, pas : 0.001) | FLOAT | Oui | 0.0 à 1.0 |
| `masque` | Un masque facultatif pour limiter l'effet du patch à des zones spécifiques de l'image | MASK | Non | |

**Note sur les contraintes des paramètres :** Si le `model_patch` possède 4 canaux d'entrée et qu'aucun `mask` n'est fourni, un masque nul est automatiquement créé pour correspondre aux dimensions de l'image. Si le `model_patch` ne possède pas 4 canaux d'entrée, le paramètre `mask` est ignoré et défini sur `None`. Seuls les 3 premiers canaux de couleur de l'image d'entrée sont utilisés. Ce nœud est marqué comme expérimental dans ComfyUI.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `MODEL` | Le modèle de diffusion corrigé avec le patch d'animation appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AnimaLLLiteApply/fr.md)

---
**Source fingerprint (SHA-256):** `48e455b767509a5a8c329365d5ffded86d6f4545d575c9fdc5ffbaf4da7c2287`
