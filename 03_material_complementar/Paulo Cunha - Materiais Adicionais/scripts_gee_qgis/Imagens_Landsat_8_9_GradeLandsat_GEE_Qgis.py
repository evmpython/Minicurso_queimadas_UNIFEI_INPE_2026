import ee
from ee_plugin import Map

# =============================================================================
# PARÂMETROS
# =============================================================================

orb = 223
pto = 67

start_date = "2024-09-01"
end_date   = "2024-09-30"

cloud_cover = 100

# =============================================================================
# VISUALIZAÇÃO
# =============================================================================

vis_rgb = {
    "bands": ["B7", "B5", "B4"],
    "min": 500,
    "max": 26550,
    "gamma": [1, 1, 0.8]
}

# =============================================================================
# LANDSAT 8 + 9
# =============================================================================

landsat = (
    ee.ImageCollection("LANDSAT/LC08/C02/T1")
    .merge(
        ee.ImageCollection("LANDSAT/LC09/C02/T1")
    )
    .filterDate(start_date, end_date)
    .filter(ee.Filter.eq("WRS_PATH", orb))
    .filter(ee.Filter.eq("WRS_ROW", pto))
    .filter(ee.Filter.lt("CLOUD_COVER", cloud_cover))
    .sort("system:time_start")
)

# =============================================================================
# OBTÉM APENAS OS ATRIBUTOS NECESSÁRIOS
# =============================================================================

ids = landsat.aggregate_array("system:id").getInfo()
nomes = landsat.aggregate_array("system:index").getInfo()
satelites = landsat.aggregate_array("SPACECRAFT_ID").getInfo()
nuvens = landsat.aggregate_array("CLOUD_COVER").getInfo()

datas = (
    landsat.aggregate_array("system:time_start")
    .map(lambda d: ee.Date(d).format("YYYY-MM-dd"))
    .getInfo()
)

print(f"\nForam encontradas {len(ids)} imagens Landsat.\n")

if not ids:
    print("Nenhuma imagem encontrada.")
    raise SystemExit

# =============================================================================
# CENTRALIZA O MAPA
# =============================================================================

Map.centerObject(ee.Image(ids[0]), 10)

# =============================================================================
# ADICIONA AO MAPA
# =============================================================================

for image_id, nome, satelite, data, cloud in zip(
    ids,
    nomes,
    satelites,
    datas,
    nuvens
):

    print("----------------------------------------")
    print(f"Satélite : {satelite}")
    print(f"Imagem   : {nome}")
    print(f"Data     : {data}")
    print(f"Nuvens   : {cloud:.2f}%")

    Map.addLayer(
        ee.Image(image_id),
        vis_rgb,
        nome,
        False
    )

print("\nConcluído.")