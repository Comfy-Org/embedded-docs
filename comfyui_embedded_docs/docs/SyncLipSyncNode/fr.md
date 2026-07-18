# SyncLipSyncNode

Ce nœud resynchronise les mouvements de la bouche dans une vidéo avec un nouveau fichier audio de parole via l'API sync.so. Il gère automatiquement les gros plans, les profils et les obstructions tout en préservant l'expression de l'orateur. Le coût est proportionnel à la durée de la sortie.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | Séquence vidéo de l'orateur à resynchroniser. Jusqu'en 4K (4096x2160) ; une fréquence d'images constante de 24/25/30 ips donne les meilleurs résultats. | VIDEO | Oui | - |
| `audio` | Audio de la parole pour synchroniser la bouche. | AUDIO | Oui | - |
| `seed` | La graine détermine si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine (par défaut : 42). | INT | Oui | 0 à 2147483647 |
| `model` | Modèle de génération sync.so. | COMBO | Oui | Voir ci-dessous |

Le paramètre `model` est une liste déroulante dynamique qui inclut les sous-paramètres suivants :

| Sous-paramètre | Description | Type de données | Requis | Plage |
|----------------|-------------|-----------------|--------|-------|
| `sync_mode` | Comment gérer une différence de durée entre la vidéo et l'audio ; cela définit également la longueur de la sortie (par défaut : "bounce"). | COMBO | Oui | `"bounce"`<br>`"cut_off"`<br>`"loop"`<br>`"silence"`<br>`"remap"` |
| `speaker_selection` | Quel visage synchroniser lorsque plusieurs personnes sont visibles (par défaut : "default"). | COMBO | Oui | `"default"`<br>`"auto-detect"`<br>`"coordinates"` |
| `speaker_frame` | Image vidéo utilisée pour localiser l'orateur. Utilisé uniquement lorsque `speaker_selection` est "coordinates" (par défaut : 0). | INT | Non | 0 à 1000000 |
| `speaker_x` | Coordonnée X en pixels du visage de l'orateur. Utilisé uniquement lorsque `speaker_selection` est "coordinates" (par défaut : 0). | INT | Non | 0 à 4096 |
| `speaker_y` | Coordonnée Y en pixels du visage de l'orateur. Utilisé uniquement lorsque `speaker_selection` est "coordinates" (par défaut : 0). | INT | Non | 0 à 4096 |

**Options du mode de synchronisation :**
- `bounce` : La vidéo est lue en avant puis en arrière jusqu'à la fin de l'audio (sortie = longueur de l'audio)
- `loop` : La vidéo redémarre jusqu'à la fin de l'audio (sortie = longueur de l'audio)
- `remap` : La vidéo est étirée temporellement pour correspondre à l'audio (sortie = longueur de l'audio)
- `cut_off` : La piste la plus longue est rognée (sortie = longueur la plus courte)
- `silence` : Rien n'est rogné ; la piste la plus courte est complétée par du silence (sortie = longueur la plus longue)

**Options de sélection de l'orateur :**
- `default` : Laisser le modèle décider quel visage synchroniser
- `auto-detect` : Détecter et suivre l'orateur actif
- `coordinates` : Cibler le visage aux coordonnées en pixels (`speaker_x`, `speaker_y`) dans l'image choisie par `speaker_frame`

**Contraintes :**
- La résolution vidéo ne doit pas dépasser 4K (4096x2160). Les vidéos dépassant cette limite généreront une erreur.
- La durée audio ne doit pas dépasser 600 secondes (10 minutes).
- Les paramètres `speaker_frame`, `speaker_x` et `speaker_y` sont uniquement utilisés lorsque `speaker_selection` est défini sur "coordinates".

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo resynchronisée avec les mouvements de la bouche correspondant à l'audio fourni. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SyncLipSyncNode/fr.md)

---
**Source fingerprint (SHA-256):** `b41f8c9bf0d55059f081a66af20636ec96462c3fd9caeb685cab10278f84678a`
