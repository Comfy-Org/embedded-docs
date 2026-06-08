Le nœud ModelMergeWAN2_1 fusionne deux modèles WAN2.1 en mélangeant leurs composants à l'aide de moyennes pondérées. Il prend en charge différentes tailles de modèles, notamment les modèles 1,3B avec 30 blocs et les modèles 14B avec 40 blocs, avec un traitement spécial pour les modèles image vers vidéo qui incluent un composant d'incorporation d'image supplémentaire. Chaque composant des modèles peut être pondéré individuellement pour contrôler le rapport de mélange entre les deux modèles d'entrée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model1` | Premier modèle à fusionner | MODEL | Oui | - |
| `model2` | Deuxième modèle à fusionner | MODEL | Oui | - |
| `patch_embedding.` | Poids du composant d'incorporation par patch (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `time_embedding.` | Poids du composant d'incorporation temporelle (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `time_projection.` | Poids du composant de projection temporelle (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `text_embedding.` | Poids du composant d'incorporation de texte (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `img_emb.` | Poids du composant d'incorporation d'image, utilisé dans les modèles image vers vidéo (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.0.` | Poids du bloc 0 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.1.` | Poids du bloc 1 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.2.` | Poids du bloc 2 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.3.` | Poids du bloc 3 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.4.` | Poids du bloc 4 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.5.` | Poids du bloc 5 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.6.` | Poids du bloc 6 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.7.` | Poids du bloc 7 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.8.` | Poids du bloc 8 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.9.` | Poids du bloc 9 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.10.` | Poids du bloc 10 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.11.` | Poids du bloc 11 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.12.` | Poids du bloc 12 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.13.` | Poids du bloc 13 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.14.` | Poids du bloc 14 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.15.` | Poids du bloc 15 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.16.` | Poids du bloc 16 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.17.` | Poids du bloc 17 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.18.` | Poids du bloc 18 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.19.` | Poids du bloc 19 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.20.` | Poids du bloc 20 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.21.` | Poids du bloc 21 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.22.` | Poids du bloc 22 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.23.` | Poids du bloc 23 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.24.` | Poids du bloc 24 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.25.` | Poids du bloc 25 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.26.` | Poids du bloc 26 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.27.` | Poids du bloc 27 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.28.` | Poids du bloc 28 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.29.` | Poids du bloc 29 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.30.` | Poids du bloc 30 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.31.` | Poids du bloc 31 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.32.` | Poids du bloc 32 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.33.` | Poids du bloc 33 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.34.` | Poids du bloc 34 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.35.` | Poids du bloc 35 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.36.` | Poids du bloc 36 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.37.` | Poids du bloc 37 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.38.` | Poids du bloc 38 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `blocks.39.` | Poids du bloc 39 (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |
| `head.` | Poids du composant de tête (par défaut : 1,0) | FLOAT | Oui | 0,0 - 1,0 |

**Remarque :** Tous les paramètres de poids utilisent une plage de 0,0 à 1,0 avec des incréments de 0,01. Le nœud prend en charge jusqu'à 40 blocs pour s'adapter à différentes tailles de modèles, où les modèles 1,3B utilisent 30 blocs et les modèles 14B utilisent 40 blocs. Le paramètre `img_emb.` est spécifiquement destiné aux modèles image vers vidéo.

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle fusionné combinant les composants des deux modèles d'entrée selon les poids spécifiés | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeWAN2_1/fr.md)

---
**Source fingerprint (SHA-256):** `d550a2f62bbcb4b46ccdd8a04fab80e93f96ea63426d48acb3515d51175efc99`
