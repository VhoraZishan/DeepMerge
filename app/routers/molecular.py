from fastapi import APIRouter, Query
from app.ingestion.ncbi import NCBIClient, NCBIRecord

router = APIRouter(prefix="/molecular", tags=["molecular"])


@router.get("/edna")
async def search_marine_edna(
	location: str = Query("India", description="Geographic location for eDNA search"),
	limit: int = Query(10, description="Number of results to return")
):
	"""Search for marine eDNA data in NCBI SRA"""
	client = NCBIClient()
	try:
		records = await client.search_marine_edna(location, limit)
		return {
			"items": [r.model_dump() for r in records], 
			"location": location,
			"source": "NCBI SRA"
		}
	except Exception as e:
		return {
			"items": [], 
			"location": location, 
			"error": str(e),
			"note": "NCBI E-utilities may be rate-limited"
		}

