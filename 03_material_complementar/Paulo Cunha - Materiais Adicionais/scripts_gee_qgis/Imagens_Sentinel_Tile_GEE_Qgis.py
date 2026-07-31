import ee
from ee_plugin import Map

# =============================================================================
# PARÂMETROS
# =============================================================================

tile_id = "21KVA"

start_date = "2024-11-10"
end_date   = "2024-11-12"

cloud_cover = 100      # Ex.: 20, 30, 50...

# =============================================================================
# VISUALIZAÇÃO
# =============================================================================

vis_swir = {
    "bands": ["B12", "B8A", "B4"],
    "min": 600,
    "max": 8000,
    "gamma": [1, 1, 1]
}

vis_rgb = {
    "bands": ["B4", "B3", "B2"],
    "min": 500,
    "max": 5500,
    "gamma": [1, 1, 1]
}

# =============================================================================
# COLEÇÃO SENTINEL-2
# =============================================================================

S2 = (
    ee.ImageCollection("COPERNICUS/S2_SR") #COPERNICUS/S2_SR_HARMONIZED
    .filterDate(start_date, end_date)
    .filter(ee.Filter.eq("MGRS_TILE", tile_id))
    .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", cloud_cover))
    .sort("system:time_start")
)

# =============================================================================
# OBTÉM TODOS OS METADADOS APENAS UMA VEZ
# =============================================================================

features = S2.getInfo()["features"]

print(f"\nForam encontradas {len(features)} imagens Sentinel-2.\n")

if len(features) == 0:
    print("Nenhuma imagem encontrada.")
    raise SystemExit

# =============================================================================
# CENTRALIZA O MAPA NA PRIMEIRA IMAGEM
# =============================================================================

Map.centerObject(ee.Image(features[0]["id"]), 10)

# =============================================================================
# ADICIONA AS IMAGENS AO MAPA
# =============================================================================

for feature in features:

    image_id = feature["id"]
    props = feature["properties"]

    granule = props.get("GRANULE_ID", "")
    cloud = props.get("CLOUDY_PIXEL_PERCENTAGE", 0)

    data = ee.Date(props["system:time_start"]).format("YYYY-MM-dd").getInfo()

    print(f"Imagem : {granule}")
    print(f"Data   : {data}")
    print(f"Nuvens : {cloud:.2f}%")
    print()

    imagem = ee.Image(image_id)

    # SWIR
    Map.addLayer(
        imagem,
        vis_swir,
        granule,
        False
    )

    # Caso queira adicionar também o RGB, descomente:
    #
    # Map.addLayer(
    #     imagem,
    #     vis_rgb,
    #     granule + "_RGB",
    #     False
    # )

print("Concluído.")