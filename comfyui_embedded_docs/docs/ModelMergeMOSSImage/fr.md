# ModelMergeMOSSImage

Le nœud ModelMergeMOSSImage fusionne deux modèles d’image MOSS en mélangeant leurs poids correspondants bloc par bloc, de sorte qu’une partie du résultat peut provenir d’un modèle de base et le reste d’un fine-tune ou d’un second modèle. Chaque composant majeur de l’architecture possède son propre ratio : le module d’embedding vidéo, le module d’embedding texte, l’embedding temporel, la modulation de bloc partagée, les 42 couches Transformer et les têtes de sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Le premier modèle à fusionner. Tout ce que le second modèle ne fournit pas est conservé depuis ce modèle | MODEL | Oui | - |
| `model2` | Le second modèle à fusionner. Ses poids sont mélangés selon les ratios ci-dessous | MODEL | Oui | - |
| `video_embedder.` | Ratio de mélange pour le bloc du module d’embedding vidéo (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `text_embedder.proj.` | Ratio de mélange pour la couche de projection du module d’embedding texte (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `text_embedder.blocks.0.` et `text_embedder.blocks.1.` | Ratio de mélange pour chacun des deux blocs du module d’embedding texte (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `time_embedding.` | Ratio de mélange pour le bloc d’embedding temporel (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `shared_block_modulation.` | Ratio de mélange pour la couche de modulation partagée utilisée par les blocs Transformer (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `layers.0.` à `layers.41.` | Ratio de mélange pour chacune des 42 couches Transformer (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `final_norm_video.` | Ratio de mélange pour la normalisation finale du flux vidéo (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `final_linear_video.` | Ratio de mélange pour la couche linéaire finale du flux vidéo (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |
| `video_head_modulation.` | Ratio de mélange pour la couche de modulation de la tête de sortie vidéo (par défaut : 1.0) | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |

Un ratio de 0.0 conserve ce composant tel qu’il est dans `model1`, un ratio de 1.0 le prend entièrement dans `model2`, et les valeurs intermédiaires produisent un mélange pondéré. Les deux entrées doivent être des modèles d’image MOSS ayant la même architecture ; les poids qui ne correspondent à aucun des préfixes ci-dessus utilisent le ratio de `video_embedder.`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL` | Le modèle fusionné, combinant les deux entrées selon les ratios spécifiés | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMOSSImage/fr.md)

---
**Source fingerprint (SHA-256):** `3b7d9c806a8d53ad00044bf30f5e63431fea7ee565414acb70a56e3059164288`
