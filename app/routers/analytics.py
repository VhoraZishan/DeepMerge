from fastapi import APIRouter, Query
from app.analytics.engine import CorrelationEngine


router = APIRouter(prefix="/analytics", tags=["analytics"])


@router.get("/correlate")
async def correlate(
	parameter: str = Query("sst", description="ocean parameter: sst | tide_height | chlorophyll"),
	species: str = Query("Sardinella longiceps"),
	region: str | None = Query("kerala"),
):
	engine = CorrelationEngine()
	result = await engine.correlate_parameter_with_species(parameter=parameter, region=region, species=species)
	return {
		"parameter": result.parameter,
		"species": result.species,
		"region": result.region,
		"pearson_r": result.pearson_r,
		"n": result.n,
		"paired_dates": result.paired_dates,
		"message": result.message,
	}


