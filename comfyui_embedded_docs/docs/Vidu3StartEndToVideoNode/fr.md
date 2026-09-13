# Génération vidéo Vidu Q3 à partir d'une image de début/fin

Ce nœud génère une vidéo en créant une transition entre une image de début et une image de fin, guidée par un prompt textuel. Il utilise le modèle Vidu Q3 pour interpoler entre les deux images et produit une vidéo à la durée et à la résolution choisies.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser pour la génération vidéo. La sélection d'une option révèle des paramètres de configuration supplémentaires pour `resolution`, `duration` et `audio`. | DYNAMIC_COMBO | Oui | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `first_frame` | L'image de départ de la séquence vidéo. | IMAGE | Oui | - |
| `end_frame` | L'image de fin de la séquence vidéo. | IMAGE | Oui | - |
| `prompt` | Description du prompt (max 2000 caractères). | STRING | Oui | Jusqu'à 2000 caractères |
| `seed` | Valeur de graine utilisée pour contrôler l'aléatoire de la génération. Dispose d'une option de contrôle après génération (par défaut : 1). | INT | Oui | 0 à 2147483647 |

### Entrées viduq3-pro et viduq3-turbo

Les paramètres suivants sont partagés par les deux options de modèle (`viduq3-pro` et `viduq3-turbo`). Ils apparaissent après la sélection d'un modèle.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | `"720p"`<br>`"1080p"` |
| `duration` | Durée de la vidéo de sortie en secondes (par défaut : 5). | INT | Oui | 1 à 16 |
| `audio` | Lorsqu'activé, produit une vidéo avec son (incluant dialogues et effets sonores) (par défaut : False). | BOOLEAN | Oui | `True`<br>`False` |

**Remarque :** Les images `first_frame` et `end_frame` doivent avoir des ratios d'aspect similaires. Le rapport d'aspect des deux images doit rester entre 80 % et 125 % l'un de l'autre (proximité relative entre 0,8 et 1,25).

**Remarque :** Pour `viduq3-turbo`, le prix est de 0,06 USD par seconde en 720p et de 0,08 USD par seconde en 1080p. Pour `viduq3-pro`, le prix est de 0,15 USD par seconde en 720p et de 0,16 USD par seconde en 1080p.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `c917867c5a7b68a1286f445025070f9a55d8d10091d9562960e0428cbedf25e4`
