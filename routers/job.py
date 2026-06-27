from fastapi import APIRouter, HTTPException, status
from schemas.job import JobCreate, JobUpdate, JobResponse

router = APIRouter(prefix="/job", tags=["job"])
# store job dicts with an `id` field
jobs: list[dict] = []


@router.post("/", response_model=JobResponse, status_code=status.HTTP_201_CREATED)
def create_job(job: JobCreate):
    job_data = job.model_dump()
    job_data["id"] = len(jobs) + 1
    jobs.append(job_data)
    return job_data


@router.get("/", response_model=list[JobResponse])
def get_all_job():
    return jobs


def _find_job(job_id: int) -> dict | None:
    for j in jobs:
        if j.get("id") == job_id:
            return j
    return None


@router.get("/{job_id}", response_model=JobResponse)
def get_job(job_id: int):
    job = _find_job(job_id)
    if not job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    return job


@router.put("/{job_id}", response_model=JobResponse)
def update_job(job_id: int, job: JobUpdate):
    existing = _find_job(job_id)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    update_data = job.model_dump(exclude_unset=True)
    existing.update(update_data)
    return existing


@router.delete("/{job_id}")
def delete_job(job_id: int):
    existing = _find_job(job_id)
    if not existing:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job not found")
    jobs.remove(existing)
    return {"message": "Job deleted"}

# @router.get("/")
# def read_job():
#     return {"job": "Job root"}

# @router.get("/{job_id}")
# def read_job(job_id: int):
#     return {"job_id": job_id}